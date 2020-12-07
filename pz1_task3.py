# Ввести строку произвольной длины большей 15. У этой строки вывести:
# 9. Символы строки за исключением некоторых (вводится пользователем)

# Получить строку с исклюенными символами
def exclude_characters_from_line(currentLine, exCharacters):
    resultStr = []
    for ch in currentLine:
        if ch not in exCharacters:
            resultStr.append(ch)
    return "".join(resultStr)


excludeCharacters = input("Введите символы котрые будут исключены: ")
line = input("Введите строку: ")

print("Результат: ", exclude_characters_from_line(line, excludeCharacters))
