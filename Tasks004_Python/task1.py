# С клавиатуры вводится целое положительное число n < 10000. Напишите скрипт, 
# который будет находить и выводить на экран минимальное положительное целое число q такое, 
# что произведение цифр этого числа будет в точности равняться числу n. В случае отсутствия 
# такого числа q скрипт должен выводить на экран сообщение «Искомого числа q не существует!». 
# Например, для числа 70 искомым числом будет 257.

# number = int(input("Введите число от 0 до 10000: "))

number = int(input('Введите число: '))
list = []

for i in range(1, 1000000):
    while i > 0:
        a = i % 10
        list.append(a)
        i //= 10

    mult = 1
    for i in range(len(list)):
        mult *= list[i]
    
    if number == mult:
        new_list = []
        for i in list:
            new_list.insert(i)
        print(f'Это число равно {new_list}')
        break
    list = []
else: print('Такого искомого числа не существует')
    


    

