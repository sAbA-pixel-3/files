# Работа с файлами

# file = open("test.txt", "r", encoding='utf - 8') # писать полную директорию, но если они в одной лиректории пимать только имя
# r - read, encoding='utf-8' - читает кириллицу
# content = file.read() # read - читает всё содержимое файла
# content_2 = file.readlines() # считает все элементы по отдельности и выводит как 1 список
# content = file.readline() # считает первую строку, если писать число то считает по пробелам
# print(content.strip()) # strip - убирает лишние пробелы 
# print(content)
# for line in file:
#     print(line.strip()) 
# file.close() # закрывает файл 

# \t - табуляция, делает 4 пробела в коде 

# w - если сделать ошибку в названии файла то создает новый с этим же названием
# file = open('test2.txt', 'w', encoding='utf-8') # w - write, перезаписывает в файл
# file.write('John Smith')
# file.writelines(['\nHello', ' World']) # writelines - добавляет в файл
# file.close() 


# a
# file = open('test.txt', 'a', encoding='utf-8')
# file.write('\nHello World') # добавляет в файл
# file.writelines(['\nhello'])
# file.close()

# with - автоматическое закрытие файла, не надо писать close()
# with open('test.txt', 'r', encoding='utf-8') as dicl:
#     content = dicl.read()
#     print(content) 
    

# # Позиции , указатель
# with open('test.txt', 'r', encoding='utf-8') as file:
#     print(file.tell()) # tell - показывает текущее нахождение указателя
#     file.seek(8) # перемещает указатель на 8 положение
#     print(file.read()) # читает с 8 позиции 
#     file.seek(0)
#     print(file.read()) # чтобы выводить файл 2 раза


# r+ , a+ , w+
# words = 'Hello'
# with open('test.txt', 'a+', encoding='utf-8') as file:
#     # file.read()
#     file.write(words)
#     # file.seek(0) 
#     print(file.read()) 




# with open('test.txt', 'r' , encoding='utf-8') as file:
#     content1 = file.readline()
#     content2 = file.readline()
#     content3 = file.readline()
#     long_word = len(content1), len(content2), len(content3)
#     print(max(long_word))      


# with open('test.txt', 'r' , encoding='utf-8') as file:
#     content = file.read()  
#     user_input = input("check the word: ")
#     if user_input in content:   
#         print("It's in the file!") 
#     else:
#         print("Not in the file!") 


# user_input = input("choose a country 'm' for Moscow, 'p' for Paris, 'b' for Budapest: ")
# if user_input.upper() == 'M':
#     with open ('moscow.txt', 'w', encoding='utf-8') as file1:
#         user_input1 = input("leave a comment: ")
#         content1 = file1.write(user_input1) 
# elif user_input.upper() == 'P':
#     with open('paris.txt', 'w', encoding='utf-8') as file2:
#         user_input2 = input("leave a comment: ") 
#         content2 = file2.write(user_input2)
# elif user_input.upper() == 'B':
#     with open('budapest.txt', 'w', encoding='utf-8') as file3:
#         user_input3 = input("leave a comment: ")
#         content3 = file3.write(user_input3) 
# else:
#     print("not in the list!") 


# with open('test.txt', 'r+', encoding='utf-8') as file:
#     content = file
#     for i in content:
#         i.split()
#         len(i)
#         print(max(content, key=len)) 
