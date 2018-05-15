
def roman_to_number(s):
    output = 0
    for i, item in enumerate(s):
        if item == 'I':
            output += 1
        elif item == 'V':
            output += 5
            if s[i-1] == 'I':
                output -= 2
        elif item == 'X':
            output += 10
            if s[i-1] == 'I':
                output -= 2
        elif item == 'L':
            output += 50
            if s[i-1] == 'X':
                output -= 20
        elif item == 'C':
            output += 100
            if s[i-1] == 'X':
                output -= 20
        elif item == 'D':
            output += 500
            if s[i-1] == 'C':
                output -= 200
        elif item == 'M':
            output += 1000
            if s[i-1] == 'C':
                output -= 200
    return output

def number_to_roman(i):
    output = ""
    if not i:
        return "ZERO"
    while i > 0:
        if i >= 1000:
            i -= 1000
            output += "M"
        elif i >= 900:
            i -= 900
            output += "CM"
        elif i >= 500:
            i -= 500
            output += "D"
        elif i >= 400:
            i -= 400
            output += "CD"
        elif i >= 100:
            i -= 100
            output += "C"
        elif i >= 90:
            i -= 90
            output += "XC"
        elif i >= 50:
            i -= 50
            output += "L"
        elif i >= 40 :
            i -= 40
            output += "XL"
        elif i >= 10 :
            i -= 10
            output += "X"
        elif i >= 9:
            i -= 9
            output += "IX"
        elif i >= 5:
            i -= 5
            output += "V"
        elif i >= 4:
            i -= 4
            output += "IV"
        else:
            i -= 1
            output += "I"
    return output
a = input()
while not a == '#':
    x, y = a.split()
    print(number_to_roman(abs(roman_to_number(x) - roman_to_number(y))))
    a = input()
