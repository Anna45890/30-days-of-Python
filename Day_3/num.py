# day 3: 30 days programming in Python

years = 16
height = 161.5
base = float(input("dase: "))
hei = float(input("height: "))
area = 0.5 * base * hei
print("Thearea   ofthetriangle is", area)

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
print("Theperimeter   ofthetriangle is", a + b + c) 

leng = int(input("Enter length: "))
wid = int(input("Enter width: "))
print("Perimeter:", 2 * (leng + wid))

r = int(input("Radius: "))
print("square:", 3.14 * r ** 2)

x = int(input("Enter x: "))
print("y = ", x ** 2 + 6 * x + 9)

len_py = len("Python")
len_dr = len("Dragon")
print(len_py != len_dr)
print("on" not in (len_py, len_dr))
print(float(len_py))
print(str(len_py))

jargon = "Надеюсь, в этом курсе не будет жаргона."
print("жаргон" in jargon)

num = int(input("Enter num: "))
if num % 2 == 0:
    print("It's even number.")
else:
    print("It isn't even number.")

print((7 / 3) == int(2.7))

print(type("10") == type(10))

print(int(9.8) == 10)

hour = float(input("ВВедите часы работы: "))
m_h = float(input("Введите стоимость в час: "))
print("Ваш ежедневный заработок составляет: ", hour * m_h)

y_o = int(input("Введите число лет, которое вы прожили: "))
print(f"Вы прожили {31536000 * y_o} лет.")

for i in range(1, 6):
    a = 1
    b = i
    c = i ** 2
    d = i ** 3

    print(i, a, b, c, d)