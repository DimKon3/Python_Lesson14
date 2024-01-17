my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def displey(n):
    if (n == len(my_list)):
        print()
        print("Конец списка!")
        return
    print(my_list[n], end=" ")
    return displey(n+1)

a = 0
displey(a)
