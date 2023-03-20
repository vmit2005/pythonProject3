class Ramка:
    """
    Модуль отрисовки рамки
    Ramка(N,'string_1'...'string_n')

    """

    def __init__(self, b : int, *strings):
        print(chr(9556) + chr(9552) * (b - 2) + chr(9559))
        for i in strings:
            if len(i) > b - 2:
                raise TypeError(f"Ширину рамки {b} нужно сделать {len(i)+2} или больше ")
                # b=len(i)+2

            print(chr(9553)  + str(i).center(b-2," ") + chr(9553))
        print(chr(9562) + chr(9552) * (b - 2) + chr(9565))

def add_ramka(b,*title):
    def wrapper(func):
        def wrap(*args,**kwargs):
            Ramка(b,*title)
            output=func(*args,**kwargs)
            print(chr(9552) * b)
            return output

        return wrap
    return wrapper


if __name__ == '__main__':
    Ramка(55, "Модуль", "отрисовки", "рамки", chr(9552)*53,
          'Функция Ramка(b:int,"string_1"..."string_n")','Декоратор @add_ramka(b:int,"string_1"..."string_n")')


    input("Enter")
