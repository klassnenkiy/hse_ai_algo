arr = []
while True:
    n = int(input())
    if n != 0:
        arr.append(n)
    else:
        break

c = 0
for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        c += 1

print(c)


# создаем список, потом принимаем вводные целые числа в цикле.
# если число не равно нулю - добавляем, если это ноль прерываем цикл,
# далее создаем счетчик, циклом проходим по индексам ,
# если число больше предыдущего то увеличиваем счетчик на 1.
# печатаем счетчик.
