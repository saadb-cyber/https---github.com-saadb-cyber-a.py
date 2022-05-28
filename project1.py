import random
import time

def burgers(i):
    bgname = ""
    if i == 1:
        bgname = "veg.BG"
    elif i == 2:
        bgname = "chicken BG"
    elif i == 3:
        bgname = "American Cheese BG "
    elif i == 4: 
        bgname = "chocolat BG"
    elif i == 5:
        bgname = "minion BG"
    elif i == 6:
        bgname = "maxican BG"
    elif i == 7:
        bgname = "Special INDIAN BG"
    elif i == 8:
        bgname = "green BG"
    else:
        bgname = "you havent selected any item"
    return bgname

def burgeramount(f, b):
    amount = 0
    if f == 1 :
        amount = 6 * b
    elif f == 2:
        amount = 7 * b
    elif f == 3:
        amount = 8 * b
    elif f == 4:
        amount = 7 * b
    elif f == 5:
        amount = 4 * b
    elif f == 6:
        amount = 6 * b
    elif f == 7:
        amount = 8 * b
    elif f == 8:
        amount = 5 * b
    else:
        amount = 0
    return amount

def Juices (a):
    juiceN = ""
    if a == 1:
        juiceN = "orange"
    elif a == 2:
        juiceN = "Coconut"
    elif a == 3:
        juiceN = "Mango"
    elif a == 4:
        juiceN = "Pomagranet"
    elif a == 5:
        juiceN = "Pepsi"
    elif a == 6:
        juiceN = "Cocakola"
    elif a == 7:
        juiceN = "Sprite"
    else:
        juiceN = "You havent selected any item"
    return juiceN

def JuiceAmount (s, b):
    Amaount = 0
    if s == 1:
        Amaount = 3 * b
    elif s == 2:
        Amaount = 5 * b
    elif s == 3:
        Amaount = 10 * b
    elif s == 4:
        Amaount = 3 * b
    elif s == 5:
        Amaount = 2 * b
    elif s == 6:
        Amaount = 2 * b
    elif s == 7:
        Amaount = 2 * b
    else:
        Amaount = 0
    return Amaount

def Extra (h):
    ExtraName = ""
    if h == 1:
        ExtraName = "seezling cheese Potatos"
    elif h == 2:
        ExtraName = "french fries"
    elif h == 3:
        ExtraName = "mashed potato"
    elif h == 4:
        ExtraName = "chilli fries"
    elif h == 5:
        ExtraName = "potato nugets"
    elif h == 6:
        ExtraName = "chili fills"
    elif h == 7:
        ExtraName = "chicken wings"
    elif h == 8:
        ExtraName = "Fride Chicken"
    elif h == 9:
        ExtraName = "Chicken nugets"
    else:
        ExtraName = "You havent selected any item"
    return ExtraName

def ExtraAmount (a, b):
    Amaount = 0
    if a == 1:
        Amaount = 5 * b
    elif a == 2:
        Amaount = 5 * b
    elif a == 3:
        Amaount = 5 * b
    elif a == 4:
        Amaount = 5 * b
    elif a == 5:
        Amaount = 5 * b
    elif a == 6:
        Amaount = 5 * b
    elif a == 7:
        Amaount = 6 * b
    elif a == 8:
        Amaount = 6 * b
    elif a == 9:
        Amaount = 7 * b
    else:
        Amaount = 0
    return Amaount

def Sandwiches (h):
    Sandwichname = ""
    if h == 1:
        Sandwichname = "veg.Sandwich"
    elif h == 2:
        Sandwichname = "Chicken Sandwich"
    elif h == 3:
        Sandwichname = "Paneer Sandwich"
    elif h == 4:
        Sandwichname = "egg.Sandwich"
    elif h == 5:
        Sandwichname = "Grilled Extra Cheese Sandwich"
    elif h == 6:
        Sandwichname = "Maxican Sandwich"
    elif h == 7:
        Sandwichname = "Chocolat Sandwich"
    elif h == 8:
        Sandwichname = "French Toste Cheese Sandwich"
    elif h == 9:
        Sandwichname = "Famli size Sandwich"
    elif h == 10:
        Sandwichname = "Club Sandwich"
    elif h == 11:
        Sandwichname = "Jumbo size three layered Sandwich"
    elif h == 12:
        Sandwichname = "Barbeque Sandwich"
    elif h == 13:
        Sandwichname = "Kids Sandwich"
    elif h == 14:
        Sandwichname = "diet Sandwich"
    else:
        Sandwichname = "You havent selected any item"
    return Sandwichname

def SandwichAmount(v, b):
    Amaount = 0
    if v == 1:
        Amaount = 5* b
    elif v == 2:
        Amaount = 6 * b
    elif v == 3:
        Amaount = 6 * b
    elif v == 4:
        Amaount = 3 * b
    elif v == 5:
        Amaount = 8 * b
    elif v == 6:
        Amaount = 5 * b
    elif v == 7:
        Amaount = 4 * b
    elif v == 8:
        Amaount = 5 * b
    elif v == 9:
        Amaount = 6 * b
    elif v == 10:
        Amaount = 5 * b
    elif v == 11:
        Amaount = 8 * b
    elif v == 12: 
        Amaount = 9 * b
    elif v == 13:
        Amaount = 3 * b
    elif v == 14:
        Amaount = 4 * b
    else:
        Amaount = 0
    return Amaount

def Wrap(e):
    Wrapname = ""
    if e == 1:
        Wrapname = "Paneer Wrap"
    elif e == 2:
        Wrapname = "Chicken Wrap"
    elif e == 3:
        Wrapname = "egg.Wrap"
    elif e == 4:
        Wrapname = "Chocole Wrap"
    else:
        Wrapname = "You havent selected any item"
    return Wrapname

def WrapAmount(e, b):
    v = 0
    if e == 1:
        v = 10 * b
    elif e == 2:
        v = 10 * b
    elif e == 3:
        v = 9 * b
    elif e == 4:
        v = 11 * b
    else:
        v = 0
    return v

def Dips (n):
    e = ""
    if n == 1:
        e = "Cream & Onion"
    elif n == 2:
        e = "Cream cheese"
    elif n == 3:
        e = "Chocochip Cream"
    elif n == 4:
        e = "Smoaled cheese"
    elif n == 5:
        e = "Heavy cheese"
    elif n == 6:
        e = "seezling cheese"
    else:
        e = "You havent selected any item"
    return e

def DipsAmount (S, b):
    a = 0
    if S == 1:
        a = 1 * b
    elif S == 2:
        a = 1 * b
    elif S == 3:
        a = 2 * b
    elif S == 4:
        a = 2 * b
    elif S == 5:
        a = 2 * b
    elif S == 6:
        a = 1 * b
    else:
        a = 0
    return a


    cout << "--------------------W E L C O M E-------------------" 

def changeOrder (z, x):
    n = 0
    if z == 1:
        n = burgers(int(x))
    elif z == 2:
        n = Juices(int(x))
    elif z == 3:
        n = Extra(int(x))
    elif z == 4:
        n = Sandwiches(int(x))
    elif z == 5:
        n = Wrap(int(x))
    elif z == 6:
        n = Dips(int(x))
    else:
        print ("I guess I will take that as you dont want any thing to be changed.")
    return n

def changeOrder2 (z, x, y):
    n = 0
    if z == 1:
        n = burgeramount(int(y, x))
    elif z == 2:
        n = JuiceAmount(int(y, x))
    elif z == 3:
        n = ExtraAmount(int(y, x))
    elif z == 4:
        n = SandwichAmount(int(y, x))
    elif z == 5:
        n = WrapAmount(int(y, x))
    elif z == 6:
        n = DipsAmount(int(y, x))

def changeOrderfinal (z, x, y):
    changeOrder2(z, x, y)
    changeOrder(z, x)

print("----------------------------------------------------" )
print(" |----------------------|    |--------------------|")
print(" |     B U R G E R      |    |  JUICE/SOFDRINCK   |")
print(" |----------------------|    |--------------------|")
print(" |1.Veg.Burger    $: 6/-|    |1.Orange        $: 3/-|")
print(" |2.chicken Burger$: 7/-|    |2.Coconut       $: 5/-|")
print(" |3.American      ______|    |3.Mango         $:10/-|")
print(" |  cheese Burger $: 8/-|    |4.Pomagranet    $: 2/-|")
print(" |4.Chocolat      ______|    |5.Pepsi         $: 2/-|")
print(" |         Burger $: 7/-|    |6.Cocakola      $: 2/-|")
print(" |5.Minion Burger $: 4/-|    |7.Sprite        $: 2/-|")
print(" |6.Maxican Burger$: 6/-|    |----------------------|")
print(" |7.Special INDIAN______|    |        EXTRAS        |")
print(" |  Burger        $: 8/-|    |----------------------|")
print(" |8.Green Burger  $: 5/-|    |1.Seezling cheez______|")
print(" |----------------------|    |  Potatos       $: 5/-|")
print("                             |2.French Fries  $: 5/-|")
print(" |----------------      |    |3.Mashed Potatos$: 5/-|")
print(" |      SANDWICH        |    |4.Chili Fries   $: 5/-|")
print(" |----------------------|    |5.Potato nugets $: 5/-|")
print(" |1.Veg.Sandwich  $: 5/-|    |6.chili fills   $: 5/-|")
print(" |2.Chicken       ______|    |7.Chicken wings $: 6/-|")
print(" |  Sandwich      $: 6/-|    |8.Fride Chicken $: 6/-|")
print(" |3.Paneer        ______|    |9.Chicken nugets$: 7/-|")
print(" |  Sandwich      $: 6/-|    |----------------------|")
print(" |4.egg.Sandwich  $: 3/-|")
print(" |5.Grilled Extra ______|    |----------------------|")
print(" |  Cheese        ______|    |      WRAPS           |")
print(" |      Sandwich  $: 8/-|    |----------------------|")
print(" |6.Maxican       ______|    |1.Paneer Wrap   $:10/-|")
print(" |  Sandwich      $: 5/-|    |2.Chicken Wrap  $:10/-|")
print(" |7.Chocolat      ______|    |3.egg.Wrap      $: 5/-|")
print(" |   Sandwich     $: 4/-|    |4.Chocolat Wrap $:11/-|")
print(" |8.French Toste  ______|    |----------------------|")
print(" |Cheese Sandwich $: 5/-|")
print(" |9.Famli size    ______|    |----------------------|")
print(" |  Sandwich      $: 6/-|    |      DIPS            |")
print(" |10.Club Sandwich$: 5/-|    |----------------------|")
print(" |11.Jumbo size   ______|    |1.Cream&Onion   $: 1/-|")
print(" |   three layered______|    |2.Cream Cheese  $: 1/-|")
print(" |   Sandwich     $: 8/-|    |3.Chocochip     ______|")
print(" |12.Barbeque     ______|    |  Cream         $: 2/-|")
print(" |   Sandwich     $: 9/-|    |4.Smoked Cheese $: 2/-|")
print(" |13.Kids Sandwich$: 3/-|    |5.Heavy cheez   $: 2/-|")
print(" |14.diet Sandwich$: 4/-|    |6.Seezling cheez$: 1/-|")
print(" |----------------------|    |----------------------|")

b = "yes"
c = False
z = 0
g = 0
while not(c):
    a = input("enter the burger number to select.\n inter zero if you don't want to select:")
    f_a = print(burgers(int(a)))
    g = input("enter the quantity from 1 to 10 to select :")
    z = input ("enter \"yes\" confirme your order:")
    if(z == b):
        c = True
i = burgeramount(int(a, g))

while not(c):
    f = input("enter the Juice number to select\n inter zero if you don't want to select :")
    A_a = print(Juices(int(f)))
    g = input("enter the quantity from 1 to 10 to select :")
    z = input("confirme your order:")
    if(z == b and f == 0):
        c = True
s = JuiceAmount(int(f, g))

while not(c):
    h = input("enter the EXTRAS number to select\n inter zero if you don't want to select :")
    a = print(Extra(int(h)))
    g = input("enter the quantity from 1 to 10 to select :")
    z = input("confirme your order:")
    if(z == b):
        c = True
h = ExtraAmount(int(h, g))

while not(c):
    v = input("enter the Sandwich number to select \n inter zero if you don't want to select:")
    e = print(Sandwiches(int(v)))
    g = input("enter the quantity from 1 to 10 to select :")
    z = input("confirme your order:")
    if(z == b):
        c = True
En = SandwichAmount(int(v, g))

while not(c):
    d = input("enter the Wrap number to select\n inter zero if you don't want to select :")
    m = print(Wrap(int(d)))
    g = input("enter the quantity from 1 to 10 to select :")
    z = input("confirme your order:")
    if(z == b):
        c = True
y = WrapAmount(int(d, g))

while not(c):
    t = input("enter the DIPS number to select\n inter zero if you don't want to select :")
    af_A = print(Dips(int(t)))
    g = input("enter the quantity from 1 to 10 to select :")
    z = input("confirme your order:")
    if(z == b):
        c = True
l = DipsAmount(int(t, g))

print("")
print("")
print("")
print("category Number : 1 ")
print(f_a)
print("category Number :2 ")
print(A_a)
print("category Number :3 ")
print(a)
print("category Number :4 ")
print(e)
print("category Number :5 ")
print(m)
print("category Number :6 ")
print(af_A)

r = input("Do you want to change some thing from your order")
if r == "yes":
    while not(c):
        r = input("Enter the category number to select:")          
        p = input("Now enter the item number to select:")          
        q = input("Now enter the quantity from 1 to 10 to select:")
        u = changeOrderfinal(r, p, q)                              
else: 
    print("Thank you for your effort, hears your bill. \n  HAVE A NICE DAY SIR.")



print("Bill")
print(str(i) + "/-")
print(str(s) + "/-")
print(str(h) + "/-")
print(str(En) + "/-")
print(str(y) + "/-")
print(str(l) + "/-")

total = int(i) + int(s) + int(h) + int(En) + int(y) + int(l)

print("Total:" + str(total))

time.sleep(600)
