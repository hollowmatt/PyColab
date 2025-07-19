#maps
_1to9dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

_10to19dict = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}
_20to90dict = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
} 

def num2word(num):
    if num < 1 or num > 100:
        return "Number out of range"
    elif num < 10:
        return _1to9dict[num]
    elif num < 20:
        return _10to19dict[num]
    elif num < 100:
        tens = (num // 10) * 10
        ones = num % 10
        if ones == 0:
            return _20to90dict[tens]
        else:
            return f"{_20to90dict[tens]}-{_1to9dict[ones]}"
    else:  # num == 100
        return "one hundred" 