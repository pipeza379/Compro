num = str(input())
roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
         'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
value = x = 0
while x < len(num):
    if num[x:x+2] in roman:
        value += roman[num[x:x+2]]
        x += 1
    else:
        value += roman[num[x]]
    x += 1
print(value)

value = 0
for i in range(0, len(num)):
    if num[i:i+2] in roman:
        value += roman[num[i:i+2]]
    else:
        value += roman[num[i]]
print(value)
