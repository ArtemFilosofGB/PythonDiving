"""
Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


txt = "Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию"
def string_to_unicode(string):
    return sorted(set([ord(i) for i in string]), reverse=True)

print(string_to_unicode(txt))