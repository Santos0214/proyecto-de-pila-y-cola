
import os

class ficha :
    def _init_(self):
        pass
        
    

    def menu(self,opciones):
        

        print("===================> MENU DE FICHA PERSONAL <========================")
        for opcion in opciones:
            print(opcion)

        opc=input("digite la ficha personal [1...{}]: ".format(len(opciones)))
        return opc

help=ficha()
Lista=["1) PILA","2) COLA","3) LISTA","4) SALIR"]

opcion =" "

while opcion != "4":
    
    os.system("cls")
    
    if opcion=="1":
        class Menu :
            def _init_(self):
                pass
        
    

            def menu(self,opciones):
                

                print("================> Haz ingresado al menú PILA <================ ")
                for opcion in opciones:
                    print(opcion)

                opc=input("digite la ficha personal [1...{}]: ".format(len(opciones)))
                return opc

        help=Menu()
        Lista1=["=> Elemento a la pila","=> Ingrese datos","=> Elemento  Salir","=> Sacar Elemento","=> Posicion","=> SALIR"]
        
        opcion=" "

        while opcion != "6":
            
            os.system("cls")
            
            if opcion=="1":
                    milis=[]
                    
                    print("================> Haz ingresado al menú PILA <================ ")
                    while True:
                        try:
                        
                            entrada=int(input("cuantos elementos desea agregar a la Pila: "))
                            break
                        except ValueError:
                            print("error")
                    os.system("cls")
                    
                    cant=entrada
                
                
                    os.system("cls")
                    i=0
                    if cant <8:
                        
                        print("lista esta vacia")
                    input("Presione ¨ENTER¨ para volver al menú Pilas ")
                    os.system ("cls")
                
            
            elif opcion=="2":
                 while i<cant:
                        
                        nom=input("ingrese su elemento a la Pila : ")
                        
                        milis.append(nom)
                        i+=1
                        
                        
                        
                        os.system("cls")
                        print(milis)
                    
                 else:
                
                    print("PILA esta llena")

                 input("Presione ¨ENTER¨ para volver al menú Pilas ")
                 os.system ("cls")
            elif opcion=="3":
                
                print("La lista es ",milis)
                
                na=milis.pop(-1)
                print("el elemento que se va a salir es : ",na)


                print(milis)
                input("Presione ¨ENTER¨ para volver al menú Pilas ")
                os.system ("cls")
            elif opcion=="4":
                
                print(milis)
                sacar=input("que elemento desea sacar : ")
                
                print("el elmento que se saco es : ",sacar)
                
                os.system("cls")
                for x in range(len(milis)-1,-1,-1):
                        if milis[x]== sacar:
                            print(milis.pop(x))
                print(milis)
                input("Presione ¨ENTER¨ para volver al menú Pilas")
                os.system ("cls")
            elif opcion=="5":
                
                print(milis)
                sa=input("desea saber en que posicion esta su elemento : ")
            
                print("posicion : ",milis.index(sa))
                input("Presione ¨ENTER¨ para volver al menú Pilas")
                os.system ("cls")
            elif opcion=="6":print(Lista)
                
            opcion=help.menu(Lista1)
            os.system("cls")
        
        
    
            



    elif opcion=="2":
        class ficha :
            def _init_(self):
                pass
        
    

            def menu(self,opciones):
                

                print("================> Haz ingresado al menú COLA <================ ")
                for opcion in opciones:
                    print(opcion)

                opc=input("digite la ficha personal [1...{}]: ".format(len(opciones)))
                return opc

        help=ficha()
        Lista2=["=> Elemento a la Cola","=> Ingrese datos","=> Elemento  Salir","=> Sacar Elemento","=> Posicion","=> SALIR"]
        
        opcion=" "

        while opcion != "6":
            
            os.system("cls")
            
            if opcion=="1":
                
                    milis=[]
                    
                    print("================> Haz ingresado al menú COLA <================ ")
                    while True:
                        try:
                        
                            entrada=int(input("cuantos elementos desea agregar a la Cola: "))
                            break
                        except ValueError:
                            print("error")
                    os.system("cls")
                    
                    cant=entrada
                
                
                    os.system("cls")
                    i=0
                    if cant <8:
                        
                        print("lista esta vacia")
                    input("Presione ¨ENTER¨ para volver al menú Colas ")
                    os.system ("cls")
                    



            elif opcion=="2":
                
                while i<cant:
                        
                        nom=input("ingrese su elemento a la Cola : ")
                        
                        milis.append(nom)
                        i+=1
                        
                        
                        
                        
                        os.system("cls")
                        print(milis)
                    
                else:
                
                    print("COLA esta llena")

                

                input("Presione ¨ENTER¨ para volver al menú Colas ")
                os.system ("cls")
            elif opcion=="3":
                
                print("La lista es ",milis)
                
                na=milis.pop(0)
                print("el elemento que se va a salir es : ",na)


                print(milis)
                input("Presione ¨ENTER¨ para volver al menú Colas ")
                os.system ("cls")
            elif opcion=="4":
               
                print(milis)
                sacar=input("que elemento desea sacar : ")
               
                os.system("cls")
                for x in range(len(milis)-1,-1,-1):
                        if milis[x]== sacar:
                            print(milis.pop(x))
                print(milis)
               
    
                input("Presione ¨ENTER¨ para volver al menú Colas ")
                os.system ("cls")
            elif opcion=="5":
                
                print(milis)
                sa1=input("desea saber en que posicion esta su elemento : ")
            
                print("posicion : ",milis.index(sa1))

                input("Presione ¨ENTER¨ para volver al menú Colas ")
                os.system ("cls")
            elif opcion=="6":print(Lista)
            opcion=help.menu(Lista2)
        
            os.system("cls")
       


    elif opcion=="3":
        class ficha :
            def _init_(self):
                pass
        
    

            def menu(self,opciones):
                

                print("================> Haz ingresado al menú LISTA <================ ")
                for opcion in opciones:
                    print(opcion)

                opc=input("digite la ficha personal [1...{}]: ".format(len(opciones)))
                return opc

        help=ficha()
        Lista2=["=> Elemento a la Lista","=> Ingrese datos","=> Elemento  Quitar","=> Posicion","=> SALIR"]
        
        opcion=" "

        while opcion != "5":
            
            os.system("cls")
            
            if opcion=="1":
                
                    milis=[]
                    
                    print("================> Haz ingresado al menú LISTA <================ ")
                    while True:
                        try:
                        
                            entrada=int(input("cuantos elementos desea agregar a la Lista: "))
                            break
                        except ValueError:
                            print("error")
                    os.system("cls")
                    
                    cant=entrada
                
                
                    os.system("cls")
                    i=0
                    if cant <8:
                        
                        print("lista esta vacia")
                    input("Presione ¨ENTER¨ para volver al menú Listas ")
                    os.system ("cls")
                    



            elif opcion=="2":
                
                while i<cant:
                        
                        nom=input("ingrese su elemento a la Lista : ")
                        
                        milis.append(nom)
                        i+=1
                        
                        
                        
                        
                        os.system("cls")
                        print(milis)
                    
                else:
                
                    print("LISta esta llena")
                lista2=["si","no"]
                lista2=input("desea agg otro nombre si o no : ")

                os.system("cls")
                if lista2 == "si":
                        print(milis)
                        nom2=input("Puedes agregar otro elemento : ")
                        
                        

                        print(f"el otro elemento que se agrego fue = {nom2}")
                        
                        milis.append(nom2)
                        
                        
                        while True:
                                try:
                                    pos=int(input("en que posicion deseas agregarlo : "))
                                    break
                                
                                except ValueError:
                                    print("error")
                        
                        
                        milis.insert(pos,nom2)
                        milis.pop(-1)
                                    
                                        
                                
                        
                        print(milis)
                

                input("Presione ¨ENTER¨ para volver al menú Listas ")
                os.system ("cls")
            elif opcion=="3":
                print(milis)
                sacar=input("que elemento desea sacar : ")
                    
                os.system("cls")
                for x in range(len(milis)-1,-1,-1):
                                        if milis[x]== sacar:
                                            print(milis.pop(x))
                print(milis)
                input("Presione ¨ENTER¨ para volver al menú Listas ")
                os.system ("cls")
            elif opcion=="4":
                print(milis)
                sa=input("desea saber en que posicion esta su elemento : ")
            
                print("posicion : ",milis.index(sa))
    
                input("Presione ¨ENTER¨ para volver al menú Listas ")
                os.system ("cls")
            
            elif opcion=="5":print(Lista)
            opcion=help.menu(Lista2)
        
            os.system("cls")


    else:
        print()
    opcion=help.menu(Lista)
print("GRACIAS POR VISITARNOS")