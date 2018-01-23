from collections import OrderedDict

digits = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

romans = OrderedDict()
romans[1000] = "M"
romans[900] = "CM"
romans[500] = "D"
romans[400] = "CD"
romans[100] = "C"
romans[90] = "XC"
romans[50] = "L"
romans[40] = "XL"
romans[10] = "X"
romans[9] = "IX"
romans[5] = "V"
romans[4] = "IV"
romans[1] = "I"


def toDigit(roman):
    final = 0
    string = roman[::-1]
    for i in range(0, len(string)-1):
        if i == len(string)-1:
            break
        value1 = digits[string[i].upper()]
        value2 = digits[string[i+1].upper()]
        if i == 0:
            final = value1
        if value1 <= value2:
            final += value2
        elif value1 > value2:
            final -= value2

    return final


def toRoman(num):
    num = int(num)
    for r in romans.keys():
        x, y = divmod(num, r)
        yield romans[r] * x
        num -= y
        if num > 0:
            toRoman(num)
        else:
            break


def main():
    while True:
        number = input("1. Roman to Integer\n2. Integer to Roman \n")
        if number == '1':
            num = input("Enter your Roman numeral: ")
            if len(num) == 1:
                print("Integer " + num.upper() + " : " + str(digits[num.upper()]) + "\n\n")
            else:
                print("Integer " + num.upper() + " : " + str(toDigit(num)) + "\n\n")

        elif number == '2':
            num = str(input("Enter an Integer number: "))
            print("Roman " + num + " : " + "".join([a for a in toRoman(num)]) + "\n\n")
main()
