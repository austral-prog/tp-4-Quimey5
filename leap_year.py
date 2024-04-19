def leap_year():
    a=int(input("Ingrese un año: "))
if(a%4==0 and a% 100==0 and a%400!=0) or (a % 4!=0):
    print("el año",a,"no es bisiesto")
else:
    print("elaño",a,"es bisiesto")
