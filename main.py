
my_list = [1, 2, 2, 3, 4]

my_list.append(7)
print("Після додавання елемента 7:", my_list)

if 3 in my_list:
    my_list.remove(3)
print("Після видалення елемента 3:", my_list)

print("Довжина списку зараз:", len(my_list))

print("Зміна з першої папки")

print("Зміна з другої папки")


no_duplicates = list(set(my_list))
print("Без дублікатів:", no_duplicates)


reversed_list = my_list[::-1]
print("Розвернутий список:", reversed_list)

Зміна через вебінтерфейс GitHub

a = 2
b = 3
sum_ab = a + b
print("Сума 2 + 3:", sum_ab)
