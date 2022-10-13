# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст: ") #абвжз мфдывао йзаоа фваабв жлор выабвфы
del_text = "абв"
result = [i for i in text.split() if del_text not in i]
print("Результат:", " ".join(result))