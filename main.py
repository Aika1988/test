# file = open('test1.txt', 'w') дозаписывает
# # file.write('Hello\n')
# # file.writelines('Hello')
# # file.write('World')
# file.write('Hello')
# file.close()

# file = open('test1.txt', 'a') добавляет
# file.write('Hello')
# print(file.read())
# file.close()

# file = open('test1.txt', 'r') # читает
# # file.write('Hello')
# f = file.read(2)
# print(f)
# print(f)

# file.close()


# file = open('test1.txt', 'r') 
# # file.write('Hello')
# print(file.readline()) он читает только строку
# file.close()


# print(file.readlines()) # он читает весь список
# file.close()

# with open('test1.txt') as file:
#     print(file.read())
# print(file.read()) # выведет ошибку что файл уже закрыт, еще нельзя принт писать все строки файла  

# сериализация (с питона в json)-> dump, dumps,
# десерилиазация (с json в питон)->  load, loads

# import json
# d = {'Hello': True, 'age': 2, 'name': None}
# json_obj = json.dumps(d)
# print(json_obj)
# python_obj = json.loads(json_obj)
# print(python_obj)

# import json
# with open('data.json', 'r') as file:
#     # python_obj = json.loads(file.read()) # loads-работает со строкой
#     python_obj = json.load(file) # load -он работает с файлами
#     print(python_obj)

# Существует 5 приципов ООП:
# 1)Наследование
# 2)Инкапсуляция
# 3)Полиморфизм
# 4)Абстракция - это выделение определенных методов
# class A(ABC):

#     @abstractmethod
#     def f():
#         pass
# 5)Ассоциация 


# super()  - это родительский класс 




