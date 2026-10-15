
def get_product(products, index):
    try:
        return products[index]
    except IndexError:
        return "Product index is out of range"


def get_settings_value(settings, key):
    try:
        return settings[key]
    except KeyError:
        return "Setting was not found"


def calculate_total_price(price, quantity):
    if not isinstance(price, (str, int, float)) or not isinstance(quantity, (str, int, float)):
        raise TypeError("Invalid data type")

    try:
        price = float(price)
        quantity = float(quantity)
    except ValueError:
        raise ValueError("Value must be a number")

    return price * quantity


def read_temperature():
    try:
        temperature = float(input("Enter temperature: "))
        print("Temperature was entered successfully")
        return temperature
    except ValueError:
        print("Invalid temperature")
        return None
    finally:
        print("Program finished")


def validate_discount(discount):
    if discount < 0:
        raise ValueError("Discount cannot be negative")
    if discount > 100:
        raise ValueError("Discount cannot be greater than 100")
    return discount


if __name__ == "__main__":
    products = ["coffee", "tea", "milk"]

    assert get_product(products, 0) == "coffee"
    assert get_product(products, 7) == "Product index is out of range"

    settings = {
        "language": "English",
        "theme": "dark"
    }

    assert get_settings_value(settings, "theme") == "dark"
    assert get_settings_value(settings, "font") == "Setting was not found"

    assert calculate_total_price("12.5", "4") == 50.0

    try:
        calculate_total_price("coffee", "4")
    except ValueError as error:
        assert str(error) == "Value must be a number"
    else:
        assert False, "ValueError was not raised"

    try:
        calculate_total_price(None, 4)
    except TypeError as error:
        assert str(error) == "Invalid data type"
    else:
        assert False, "TypeError was not raised"

    assert validate_discount(20) == 20
    assert validate_discount(0) == 0
    assert validate_discount(100) == 100

    try:
        validate_discount(-1)
    except ValueError as error:
        assert str(error) == "Discount cannot be negative"
    else:
        assert False, "ValueError was not raised"

    try:
        validate_discount(101)
    except ValueError as error:
        assert str(error) == "Discount cannot be greater than 100"
    else:
        assert False, "ValueError was not raised"

    print("All checks passed!")
    read_temperature()
