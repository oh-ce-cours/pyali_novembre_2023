def fizzbuzz_1():
    for number in range(1, 101):
        res = fizzbuzz_1_for_number(number)
        print(res)


def fizzbuzz_1_for_number(number: int) -> str:
    res = ""
    if number % 3 == 0 and number % 5 == 0:
        res = "fizzbuzz"
    elif number % 3 == 0:
        res = "fizz"
    elif number % 5 == 0:
        res = "buzz"
    else:
        res = number
    return res


def fizz_buzz_2():
    for number in range(1, 101):
        res = ""
        if number % 3 == 0:
            res += "fizz"
        if number % 5 == 0:
            res += "buzz"
        if number % 7 == 0:
            res += "bazz"
        if not res:
            res = str(number)
        print(res)


def fizz_buzz_3():
    for number in range(1, 101):
        match number % 3, number % 5:
            case 0, 0:
                print("fizzbuzz")
            case 0, _:
                print("fizz")
            case _, 0:
                print("buzz")
            case _, _:
                print(number)


fizz_buzz_3()
