'''
Завдання 1
Напишіть функцію, яка обчислює добуток елементів списку цілих.
Список передається як параметр. Отриманий результат повертається із функції.
'''
def product_of_elements(lst):
    result = 1
    for element in lst:
        result *= element
    return result

input_list =[1,2,3,4,5]
print ("product_of_elements is:",product_of_elements(input_list))

'''
Завдання 2
Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
'''
def find_minimum(lst):
    return min(lst)

input_list =[1,2,3,4,5]
print ("min element of the list is:",find_minimum(input_list))

''' 
Завдання 3
Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
'''
def count_primes(lst):

    count = 0

    for number in lst:
        if number <= 1:
            continue
        if number <= 3:
            count += 1
            continue
        if number % 2 == 0 or number % 3 == 0:
            continue
        is_prime_number = True
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                is_prime_number = False
                break
            i += 6
        if is_prime_number:
            count += 1

    return count


input_list =[1,2,3,4,5]
print ("Count of prime numbers of the list is:",count_primes(input_list))
'''
Завдання 4
Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість видаленних елементів.
'''
def remove_element(lst, num_to_remove):
    count = lst.count(num_to_remove)
    while num_to_remove in lst:
        lst.remove(num_to_remove)
    return count

input_list =[1,2,3,4,5]
num_to_remove=3
print ("Count of removed elements is:",remove_element(input_list, 3))
'''
Завдання 5
Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
'''
def combine_lists(list1, list2):
    return list1 + list2


list1 =[1,2,3,4,5]
list2 =[9,9,7,8,7]

print ("Combinet list of two lists:",combine_lists(list1, list2))
'''
Завдання 6
Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр, список також передається як параметр. Функція повертає новий список, який містить отримані результати.
'''
def power_elements(lst, power):
    return [x ** power for x in lst]



list2 =[9,9,7,8,7]

print ("Power of elements in the list:",power_elements(list1, 4))