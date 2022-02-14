def parimpar(inicio, fin):
     i = inicio
     for i in range(inicio, fin):
         residuo = i%2
         if residuo == 0:
             print("El numero es par"), i

         if residuo != 0:
            print("El numero es impar"), i

inicio = int(input("Ingrese numero"))
fin = int(input("Ingrese numero final"))
parimpar(inicio, fin)
