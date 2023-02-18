# Dictionary mapping nums to plain english
nums_to_plain = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    21: "twenty-one",
    22: "twenty-two",
    23: "twenty-three",
    24: "twenty-four",
    25: "twenty-five",
    26: "twenty-six",
    27: "twenty-seven",
    28: "twenty-eight",
    29: "twenty-nine",
    30: "thirty",
    31: "thirty-one",
    32: "thirty-two",
    33: "thirty-three",
    34: "thirty-four",
    35: "thirty-five",
    36: "thirty-six",
    37: "thirty-seven",
    38: "thirty-eight",
    39: "thirty-nine",
    40: "forty",
    41: "forty-one",
    42: "forty-two",
    43: "forty-three",
    44: "forty-four",
    45: "forty-five",
    46: "forty-six",
    47: "forty-seven",
    48: "forty-eight",
    49: "forty-nine",
    50: "fifty",
    51: "fifty-one",
    52: "fifty-two",
    53: "fifty-three",
    54: "fifty-four",
    55: "fifty-five",
    56: "fifty-six",
    57: "fifty-seven",
    58: "fifty-eight",
    59: "fifty-nine"
}


def civi_to_24hour(civi):
    try:
        AM_PM = civi[-2:]
        time = civi[0:-2]
        hours, mins = time.split(":")
        hours = int(hours)
        mins = int(mins)
        if hours == 12:
            if AM_PM == "AM":
                hours = 0

        if AM_PM == "PM":
            if hours != 12:
                hours += 12
    except:
        raise Exception("Invalid Time Please Insert in the Following Format: X:XX(AM/PM)")

    return hours, mins

def convert_to_military(hours_mins):
    #UNPACK TUPLE
    hours, mins = hours_mins
    military_speak = ""

    if hours < 10 and hours != 0:
        military_speak += "zero "

    military_speak += nums_to_plain[hours]

    military_speak += " "

    if mins == 0:
        military_speak += "hundred hours"
        return military_speak

    if mins < 10:
        military_speak += "zero "
        military_speak += nums_to_plain[mins]
    else:
        military_speak += nums_to_plain[mins]

    return military_speak




if __name__ == "__main__":
    civi_time = input("Input Time:")
    civi_time = civi_to_24hour(civi_time)
    print(convert_to_military(civi_time))
