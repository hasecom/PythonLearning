#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
import cgi
import sys
import io
print("Content-type: text/html; charset=utf-8")
print("")
val1 = 0 + 1 + 2
print(val1)

val2 = bool(0)
print(val2)

val3 = "string"
print(val3)

val4 = 1 + 0.5 + 0.75
print(val4)

val5 = 0b11
print(val5)

val6 = int("1") + int("10")
print(val6)

print( '''
aa\n
bb
cc
''')
print("<br>")

list = [1,2,3]
print(list[2])

kk = [1,[1,2,3],4,5,[6,7,[8,9],10],11]
print(kk)


bb = dict(one=1,two=2,three=3)
print(bb)

cc = 2

if cc == 2:
    print("0です")
elif cc==1:
    print("1です　")
else:
    print("その他です")

def sample(num):
    print(str(num) + "です　。")

sample(50)
samples = list
for aa in samples:
        print(aa)
