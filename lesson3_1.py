# #Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
# #способами

sentence = input("Input sentence: ")
r_sentence = sentence.replace(" ","-")
print(r_sentence)
s_sentence = sentence.split(" ")
j_sentence = "-".join(s_sentence)
print(j_sentence)

