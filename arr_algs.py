def min(arr1):
    mn = arr1[0]
    for i in range(len(arr1)):
        print(i, arr1[i])
    for i in range(len(arr1)):
        if mn > arr1[i]:
            mn = arr1[i]
    return mn

def sr(arr1):
    s=0
    for i in range(len(arr1)):
        s = s + arr1[i]
    print("Сумма всех элементов массива = ", s)
    avr = s/len(arr1)
    return avr

arr1 = [500, 6990, 2450, 10, 50]
m=min(arr1)
print("Минимальный элемент массива = ", m)
print("Задание б: ")
s1=sr(arr1)
print("Среднее арифметическое массива = ", s1)






