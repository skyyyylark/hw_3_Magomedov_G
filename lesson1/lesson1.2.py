

def func(name, *args, **kwargs):
    print(name)
    print(f"Оставшиеся: {args}") #Аргс - чтобы передать лишние параметры и не выдать ошибку при их добавлении
    print("Kwargs: ", kwargs)  #Кваргс - чтобы создать несозданные заранее аргументы функции как словарь

func("Aman", "Masha", "Petya", age=30, work=True)

def make_sum(*args):
    res = 0
    for i in args:
        res += i
    print("Sum: " , res)

make_sum(2,3,4,5,1,2,4,5,6,54,23) #можно добавить неограниченное кол-во чисел для суммы, так как *аргс засчитывает всё





