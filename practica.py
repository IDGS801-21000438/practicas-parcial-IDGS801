class practica:
    
        def __init__(self):   
            self.numero = input("Dame un numero entero porfavor: ") 

        def imprime(self):
         for punto in range(1, int(self.numero) +1):
                print("*" * punto)


        def listaParcial(self):
              lista = list(range(int(self.numero)))
              lista.sort()
              listaPares = [num for num in lista 
                            if num % 2 == 0]
              
              listaPrimos = [num for num in lista 
                             if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
              
              print("Lista original: ", lista)
              print("Lista de números pares: ", listaPares)
              print("Lista de números primos: ", listaPrimos)

             



def main():
        obj = practica()
        obj.listaParcial()
        obj2 = practica()
        obj2.imprime()

if __name__=="__main__":
        main()
