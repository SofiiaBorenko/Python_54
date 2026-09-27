# 1

def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list):
        print("Wrong list")
        return

    for i in range(len(lst) - 1, -1, -1):
        print(lst[i], end=" ")
    print()


# 2

def is_valid_point(point):
    if point is None or point == ():
        return None

    if not isinstance(point, tuple):
        return False

    if len(point) != 2:
        return False

    if not isinstance(point[0], (int, float)):
        return False

    if not isinstance(point[1], (int, float)):
        return False

    return True


# 3

def print_sublist_reverse(lst, start, finish):
    if (
        lst is None
        or not isinstance(lst, list)
        or not isinstance(start, int)
        or not isinstance(finish, int)
        or start < 0
        or finish < 0
        or start >= len(lst)
        or finish >= len(lst)
        or start > finish
    ):
        print("Wrong args")
        return

    result = lst[:]

    while start <= finish:
        result[start] = lst[finish]
        start += 1
        finish -= 1

    print(result)


# 4

def get_students_by_grade(students):
    if students is None or not isinstance(students, dict) or students == {}:
        return {}

    result = {}

    for name, grade in students.items():
        if grade not in result:
            result[grade] = []

        result[grade].append(name)

    return result