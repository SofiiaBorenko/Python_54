def clean_cart(cart):
    i = 0

    while i < len(cart):
        if cart[i] == "sold out":
            cart.remove("sold out")
        else:
            i += 1

    return cart


def temperature_report(temperatures):
    result = []

    for temperature in temperatures:
        if temperature > 25:
            result.append(temperature)

    return result


def fix_balances(balances):
    for i in range(len(balances)):
        if balances[i] < 0:
            balances[i] = 0

    return balances


def unique_items(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result


def longest_word(words):
    best_word = words[0]

    for word in words:
        if len(word) > len(best_word):
            best_word = word

    return best_word


print(clean_cart(["milk", "sold out", "bread", "sold out", "coffee"]))
print(temperature_report([21, 28, 19, 31, 25, 27]))
print(fix_balances([120, -30, 50, -5, 0, 200]))
print(unique_items(["red", "blue", "red", "green", "blue"]))
print(longest_word(["cat", "elephant", "python", "coffee"]))