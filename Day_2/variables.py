# day 2: 30 days programming in Python
# level 1
name = "Anna"
shurename = "Chikmareva"
country = "Russia"
city = "Sevastopol"
age = 16.5
year = 2025
is_light_on = True

# level 2

print(type(name))
print(type(shurename))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_light_on))

name_len = len(name)
shurename_len = len(shurename)
print(name_len > shurename_len)

num_one = 5
num_two = 4
total = num_one, num_two
diff = num_two - num_one
product = num_one * num_two
division = num_two / num_one
remainder = num_two // num_one
exp = num_one ** num_two
floor_division = num_one // num_two

r = 30
area_or_circle = 3.14 * (r ** 2)
circum_of_circle = 3.14 * (2 * r)

user_name = input("Your name: ")
u_shurename = input("Your shurename: ")
u_country = input("Your country: ")
u_year = int(input("How old are you: "))