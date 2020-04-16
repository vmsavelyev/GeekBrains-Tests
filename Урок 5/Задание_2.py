"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке"""

f = open("Задание_2.txt", 'r', encoding='utf-8')
content = f.readlines()
print(len(content))
a = sum([len(i) for i in content])
print(a-len(content))
f.close()
