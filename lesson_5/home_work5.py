import csv
import json
from pathlib import Path


def save_test_ids(test_ids):
    with open("tests.txt", "w", encoding="utf-8") as file:
        for test_id in test_ids:
            file.write(test_id + "\n")


def add_test_id(test_id):
    with open("tests.txt", "a", encoding="utf-8") as file:
        file.write(test_id + "\n")


def load_test_ids(filename):
    test_ids = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            test_id = line.strip()

            if test_id != "":
                test_ids.append(test_id)

    return test_ids


def get_test_statistics(filename):
    total = 0
    passed = 0
    failed = 0
    total_duration_ms = 0
    failed_ids = []

    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += 1
            status = row["status"]
            duration = int(row["duration_ms"])

            if status == "PASSED":
                passed += 1

            if status == "FAILED":
                failed += 1
                failed_ids.append(row["test_id"])

            total_duration_ms += duration

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "total_duration_ms": total_duration_ms,
        "failed_ids": failed_ids
    }


def save_test_config(environment, base_url, timeout):
    config = {
        "environment": environment,
        "base_url": base_url,
        "timeout": timeout
    }

    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)


def load_test_config(filename):
    with open(filename, "r", encoding="utf-8") as file:
        config = json.load(file)

    return config


def build_run_report(project_name, csv_filename):
    total = 0
    passed = 0
    failed = 0
    total_duration_ms = 0
    failed_ids = []

    with open(csv_filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += 1
            status = row["status"]
            duration = int(row["duration_ms"])

            if status == "PASSED":
                passed += 1

            if status == "FAILED":
                failed += 1
                failed_ids.append(row["test_id"])

            total_duration_ms += duration

    report_folder = Path("reports") / project_name
    report_folder.mkdir(parents=True, exist_ok=True)

    summary = {
        "project": project_name,
        "total": total,
        "passed": passed,
        "failed": failed,
        "total_duration_ms": total_duration_ms
    }

    with open(report_folder / "summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    with open(report_folder / "failed_tests.txt", "w", encoding="utf-8") as file:
        for test_id in failed_ids:
            file.write(test_id + "\n")

    return summary


if __name__ == "__main__":
    save_test_ids(["QA-1001", "QA-1002", "QA-1003"])
    add_test_id("QA-1004")

    assert load_test_ids("tests.txt") == [
        "QA-1001",
        "QA-1002",
        "QA-1003",
        "QA-1004"
    ]

    statistics = get_test_statistics("results.csv")

    assert statistics == {
        "total": 3,
        "passed": 2,
        "failed": 1,
        "total_duration_ms": 500,
        "failed_ids": ["QA-1002"]
    }

    save_test_config("staging", "https://example.com", 30)
    config = load_test_config("config.json")

    assert config["environment"] == "staging"
    assert config["base_url"] == "https://example.com"
    assert config["timeout"] == 30
    assert type(config["timeout"]) == int

    report = build_run_report("Shop", "results.csv")

    assert report == {
        "project": "Shop",
        "total": 3,
        "passed": 2,
        "failed": 1,
        "total_duration_ms": 500
    }

    print("All checks passed!")