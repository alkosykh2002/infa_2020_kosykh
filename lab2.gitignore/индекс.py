import turtle as t

print('напиши числа через пробел')
index = input().split()
Index = []
for i in range(len(index)):
    Index.append(int(index[i]))

t.speed(1)
t.penup()
t.backward(300)
t.pendown()


def number0(i):
    t.goto(-300 + 100 * i, 0)
    t.pendown()
    t.goto(-300 + 100 * i, 100)
    t.goto(-300 + 100 * i + 50, 100)
    t.goto(-300 + 100 * i + 50, 0)
    t.goto(-300 + 100 * i, 0)
    t.penup()


def number1(i):
    t.penup()
    t.goto(-300 + 100 * i, 50)
    t.pendown()
    t.goto(-300 + 100 * i, 50)
    t.goto(-300 + 100 * i + 50, 100)
    t.goto(-300 + 100 * i + 50, 0)
    t.penup()


def number2(i):
    t.goto(-300 + 100 * i + 50, 0)
    t.pendown()
    t.goto(-300 + 100 * i, 0)
    t.goto(-300 + 100 * i + 50, 50)
    t.goto(-300 + 100 * i + 50, 100)
    t.goto(-300 + 100 * i, 100)
    t.penup()


def number3(i):
    t.goto(-300 + 100 * i, 0)
    t.pendown()
    t.goto(-300 + 100 * i + 50, 50)
    t.goto(-300 + 100 * i, 50)
    t.goto(-300 + 100 * i + 50, 100)
    t.goto(-300 + 100 * i, 100)
    t.penup()


def number4(i):
    t.penup()
    t.goto(-300 + 100 * i, 100)
    t.pendown()
    t.goto(-300 + 100 * i, 50)
    t.goto(-300 + 100 * i + 50, 50)
    t.goto(-300 + 100 * i + 50, 100)
    t.goto(-300 + 100 * i + 50, 0)
    t.penup()


def number5(i):
    t.goto(-300 + 100 * i, 0)
    t.pendown()
    t.goto(-300 + 100 * i + 50, 0)
    t.goto(-300 + 100 * i + 50, 50)
    t.goto(-300 + 100 * i, 50)
    t.goto(-300 + 100 * i, 100)
    t.goto(-300 + 100 * i + 50, 100)
    t.penup()


def number6(i):
    t.goto(-300 + 100 * i, 0)
    t.pendown()
    t.goto(-300 + 100 * i, 50)
    t.goto(-300 + 100 * i + 50, 100)
    t.goto(-300 + 100 * i, 50)
    t.goto(-300 + 100 * i + 50, 50)
    t.goto(-300 + 100 * i + 50, 0)
    t.goto(-300 + 100 * i, 0)
    t.penup()


def number7(i):
    t.goto(-300 + 100 * i, 0)
    t.pendown()
    t.goto(-300 + 100 * i, 50)
    t.goto(-300 + 100 * i + 50, 100)
    t.goto(-300 + 100 * i, 100)
    t.penup()


def number8(i):
    t.goto(-300 + 100 * i, 0)
    t.pendown()
    t.goto(-300 + 100 * i, 100)
    t.goto(-300 + 100 * i + 50, 100)
    t.goto(-300 + 100 * i + 50, 0)
    t.goto(-300 + 100 * i, 0)
    t.goto(-300 + 100 * i, 50)
    t.goto(-300 + 100 * i + 50, 50)
    t.penup()


def number9(i):
    t.goto(-300 + 100 * i, 0)
    t.pendown()
    t.goto(-300 + 100 * i + 50, 50)
    t.goto(-300 + 100 * i + 50, 100)
    t.goto(-300 + 100 * i, 100)
    t.goto(-300 + 100 * i, 50)
    t.goto(-300 + 100 * i + 50, 50)
    t.penup()
    t.goto(-300 + 100 * i + 100, 0)
    t.penup()


print(Index)
for i in range(len(Index)):
    if Index[i] == 0:
        number0(i)
    if Index[i] == 1:
        number1(i)
    if Index[i] == 2:
        number2(i)
    if Index[i] == 3:
        number3(i)
    if Index[i] == 4:
        number4(i)
    if Index[i] == 5:
        number5(i)
    if Index[i] == 6:
        number6(i)
    if Index[i] == 7:
        number7(i)
    if Index[i] == 8:
        number8(i)
    if Index[i] == 9:
        number9(i)