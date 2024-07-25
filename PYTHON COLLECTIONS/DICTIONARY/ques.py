"""Write out numbers in english  using dictionary"""

ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
        12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninty'}


def number_word(num):
    if 0 < num < 999:
        return three_digit_number(num)
    else:
        return "Invalid"


def two_digit_number(num):
    if num < 20:
        return ones[num]
    else:
        ten = num // 10
        one = num % 10
        return tens[ten * 10] + (" " if one == 0 else " " + ones[one])


def three_digit_number(num):
    hundred = num // 100
    rem = num % 100
    if hundred == 0:
        return two_digit_number(num)
    else:
        return ones[hundred] + " hundred" + (" " if rem == 0 else " " + two_digit_number(rem))


def main_fun():
    num = int(input("Enter the number :"))
    print(number_word(num))


main_fun()
