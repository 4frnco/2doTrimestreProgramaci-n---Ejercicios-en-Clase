
class calculadoraBinaria:

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def set_a(self, a):
        if isinstance (a,int) or isinstance(a,float) or isinstance(a, complex):
            self.__a = a
        else:
            self.__a = 0

    def get_a(self, a):
        return self.__a

    def set_b(self, b):
        if isinstance(b,int) or isinstance(b,float) or isinstance(b, complex):
            self.__b = b
        else:
            self.__b = 0

    def get_b(self, b):
        return self.__b


    def operacion (self, op):
        if op == '+':
            return self.__a + self.__b
        if op == '-':
            return self.__a - self.__b
        if op == '*':
            return self.__a * self.__b
        if op == '/':
            return self.__a / self.__b

    a = property (get_a,set_a)
    b = property (get_b,set_b)

if __name__=='__main__':
        c1 = calculadoraBinaria (2, 3)
        c1.a = 1
        c1.__a = 'once'
        print (c1.operacion('+'))
        c2 = calculadoraBinaria (2, 3)
        print(c2.operacion('+'))

        try:
            print(c2.operacion('/'))
        except ZeroDivisionError:
            print("No se puede dividir por cero")

        finally:
            print("Fin del programa")








