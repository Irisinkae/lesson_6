#1. Функция склейка-перевертыш

def concat(*args:str, reversed:bool=False)->str:

    s=''
    if reversed == False:
        for i in args:
            s+=i
    else:
        for i in args[::-1]:
            s+=i
    return s
print(concat(' мир',' труд',' май',' дружба'))
print(concat(' мир',' труд',' май',' дружба', reversed=True))
print()

# 2. Нахождение факториала


def factorial(n: int) ->int:
    if n==1:
        return n
 
    return n*factorial(n-1)

print(f'Факториал  равен {factorial(7)}')
print()



# 3.декоратор + функция склейки
def inspect(func):
    def wrapper_func(*args, **kwargs):
        print(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        retvalue=func(*args, **kwargs)
        print(f'Retvalue: {retvalue}')
        print(retvalue)
    return wrapper_func

@inspect
def concat(*args: str, reversed:bool = False) -> str:
    s=''
    if reversed == False:
        for i in args:
            s+=i
    else:
        for i in args[::-1]:
            s+=i
    return s

concat('мир','дружба','жвачка', reversed=True)
print()
concat('мир','дружба','жвачка')