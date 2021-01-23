def digit_to_write(x):
    yazi = ""
    if x == 1:
        yazi += "one"
    elif x == 2:
        yazi += "two"
    elif x == 3:
        yazi += "three"
    elif x== 4:
        yazi += "four"
    elif x == 5:
        yazi += "five"
    elif x == 6:
        yazi += "six"
    elif x == 7:
        yazi += "seven"
    elif x == 8:
        yazi += "eigth"
    elif x == 9:
        yazi += "nine"
    elif x == 10:
        yazi += "ten"
    elif x == 11:
        yazi += "eleven"
    elif x == 12:
        yazi += "twelve"
    elif x == 13:
        yazi += "thirteen"
    elif x == 14:
        yazi += "fourteen"
    elif x == 15:
        yazi += "fifteen"
    elif x == 16:
        yazi += "sixteen"
    elif x == 17:
        yazi += "seventeen"
    elif x == 18:
        yazi += "eighteen"
    elif x == 19:
        yazi += "nineteen"
    elif x == 20:
        yazi += "twenty"
    elif x == 30:
        yazi += "thirty"
    elif x == 40:
        yazi += "forty"
    elif x == 50:
        yazi += "fifty"
    elif x == 60:
        yazi += "sixty"
    elif x == 70:
        yazi += "seventy"
    elif x == 80:
        yazi += "eighty"
    elif x == 90:
        yazi += "ninety"
    elif x == 100:
        yazi += "onehundred"
    elif x == 200:
        yazi += "twohundred"
    elif x == 300:
        yazi += "threehundred"
    elif x == 400:
        yazi += "fourhundred"
    elif x == 500:
        yazi += "fivehundred"
    elif x == 600:
        yazi += "sixhundred"
    elif x == 700:
        yazi += "sevenhundred"
    elif x == 800:
        yazi += "eighthundred"
    elif x == 900:
        yazi += "ninehundred"
    elif x == 1000:
        yazi += "onethousand"
    return yazi

def number_to_write(x):
    yazi = ""
    num_str = str(x)
    if len(num_str) > 3:
        yazi += digit_to_write(x)
    elif len(num_str) > 2:
        hundred = x // 100
        x -= hundred * 100
        yazi += digit_to_write(hundred)
        if x != 0:
            yazi += "and"
            if digit_to_write(x) == "":
                tenth = x // 10
                x -= tenth * 10
                












