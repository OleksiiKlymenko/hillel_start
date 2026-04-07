# 1
def string_length(string):
    return len(string)


print(string_length("hello"))


# 1.2
def two_strings(str1, str2):
    return str1 + " " + str2


print(two_strings("Hello", "World"))

# 2
n = 5


def square_number(n):
    return n**2


print(f"Квадрат числа {n}: {square_number(5)}")

# 2.2
a = 3
b = 5


def sum_two_numbers(a, b):
    return a + b


print(f"Сума {a}, {b}: {sum_two_numbers(a, b)}")

# 2.3
n = 7
m = 9


def divide(n, m):
    res1 = n // m
    res2 = n % m
    return res1, res2


q, r = divide(n, m)
print(f"Ділення {n} на {m}: ціла частина = {q}, залишок = {r}")

# 3
test_list = [13, 27, 38, 45]


def average(test_list):
    return sum(test_list) / len(test_list)


print(f"Середнє значення списку {test_list}: {average(test_list)}")

# 3.2
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]


def get_common_elements(list_a, list_b):
    common = list(set(list_a) & set(list_b))
    return common


print(f"Спільні елементи {list_a} та {list_b}: {get_common_elements(list_a, list_b)}")


# 4
def get_dictionary_keys(data_dict):
    return list(data_dict.keys())


person = {"name": "John", "age": 25, "city": "Kyiv"}
print(f"Ключі словника {person}: {get_dictionary_keys(person)}")


# 4.2
def merge_dictionaries(dict1, dict2):
    return dict1 | dict2


first_dict = {"a": 1, "b": 2}
second_dict = {"c": 3, "d": 4}

merged = merge_dictionaries(first_dict, second_dict)
print(f"Об'єднаний словник: {merged}")


# 5
def merge_sets(set1, set2):
    return set1 | set2


s1 = {1, 2, 3}
s2 = {3, 4, 5}

result = merge_sets(s1, s2)
print(f"Об'єднання множин {s1} та {s2}: {result}")


# 5.2
def is_subset(set1, set2):
    return set1.issubset(set2)


first_set = {1, 2}
second_set = {1, 2, 3, 4}

print(f"{first_set} є підмножиною {second_set}? : {is_subset(first_set, second_set)}")


# 6
def check_even_odd(number):
    if number % 2 == 0:
        return "Парне"
    else:
        return "Непарне"


num = 6
print(f"Число {num} є: {check_even_odd(num)}")


# 6.2
def filter_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list


test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Тільки парні зі списку {test_numbers}: {filter_numbers(test_numbers)}")


# 7
check_parity = lambda n: "парне" if n % 2 == 0 else "не парне"

num1 = 10
num2 = 7

print(f"Число {num1}: {check_parity(num1)}")
print(f"Число {num2}: {check_parity(num2)}")
