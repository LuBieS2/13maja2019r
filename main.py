
from math import   *


File = open("liczby.txt", "r")
numbers = list(map(str.strip,File.readlines()))
d = []
for i in range(0, len(numbers)):
    root=3
    root=root**int(i)
    d.append(root)
RootOfThree = []

for i in numbers:
    if int(i) in d:
        RootOfThree.append(i)
#print(len(RootOfThree))
Digits=[]
for number in numbers:
    temp_digits=[]
    for i in number:
        temp_digits.append(i)
    Digits.append(temp_digits)
fct=0
number2=""
fct_s=0
#print(factorial(2))
for n, number in enumerate(Digits):
    number2="".join(map(str, number))
    for c in number:
        fct=int(factorial(int(c)))
        fct_s=fct_s+fct
    if int(number2) == int(float(fct_s)):
        print(Digits.index(number), number2)
        Digits.pop(n)
    fct_s=0
    number2=""
longest_list=[]
list=[]
counter=numbers[0]

last=0

#print(nwdb)
for i in numbers:
    if len(list)==0:
        list.append(i)
    else:
        counter=list[0]
        for x in list:
            counter=gcd(int(counter), int(x))
        if gcd(counter, int(i))!=1:
            list.append(i)
        else:
            last=list[-1]
            if len(list) > len(longest_list):
                longest_list=list.copy()
                list=[i]
            else:
                list=[i]
            if gcd(int(i), int(last)) > 1:
                list=[last, i]
print(longest_list)
NWD=longest_list[0]
print(longest_list[0])
for x in longest_list:
    print(NWD)
    NWD=gcd(int(NWD), int(x))
print(longest_list[0])
print(number[-1])