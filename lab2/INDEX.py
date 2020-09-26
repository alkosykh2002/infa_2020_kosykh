import turtle as t
t.penup()

File = 'Turtle2.txt'
print('Выпiши числа через пробел')
line = 'nol'
index = input()

print('напиши числа через пробел')
index = input().split()
Index = []
for i in range(len(index)):
    Index.append(int(index[i]))


with open(File, "r") as File:
    while line:
        line = File.readline()
        line = line.rstrip()
        print(line)
        eval(line)
    File.close()