import time

z = open('test2.html', 'x')

def burgers(i):
    bgname = ""
    if i == 1:
        bgname = "<p>veg.BG</p>"
    elif i == 2:
        bgname = "<p>chicken BG</p>"
    elif i == 3:
        bgname = "<p>American Cheese BG </p>"
    elif i == 4: 
        bgname = "<p>chocolat BG</p>"
    elif i == 5:
        bgname = "<p>minion BG</p>"
    elif i == 6:
        bgname = "<p>maxican BG</p>"
    elif i == 7:
        bgname = "<p>Special INDIAN BG</p>"
    elif i == 8:
        bgname = "<p>green BG</p>"
    else:
        bgname = "<p>you havent selected any item</p>"
    return bgname

def burgeramount(f):
    amount = 0
    if f == 1:
        amount = 6
    elif f == 2:
        amount = 7
    elif f == 3:
        amount = 8
    elif f == 4:
        amount = 7
    elif f == 5:
        amount = 4
    elif f == 6:
        amount = 6
    elif f == 7:
        amount = 8
    elif f == 8:
        amount = 5
    else:
        amount = 0
    return amount

def Juices (a):
    juiceN = ""
    if a == 1:
        juiceN = "<p>orange</p>"
    elif a == 2:
        juiceN = "<p>Coconut</p>"
    elif a == 3:
        juiceN = "<p>Mango</p>"
    elif a == 4:
        juiceN = "<p>Pomagranet</p>"
    elif a == 5:
        juiceN = "<p>Pepsi</p>"
    elif a == 6:
        juiceN = "<p>Cocakola</p>"
    elif a == 7:
        juiceN = "<p>Sprite</p>"
    else:
        juiceN = "<p>You havent selected any item</p>"
    return juiceN

def JuiceAmount (s):
    Amaount = 0
    if s == 1:
        Amaount = 3
    elif s == 2:
        Amaount = 5
    elif s == 3:
        Amaount = 10
    elif s == 4:
        Amaount = 3
    elif s == 5:
        Amaount = 2
    elif s == 6:
        Amaount = 2
    elif s == 7:
        Amaount = 2
    else:
        Amaount = 0
    return Amaount

def Extra (h):
    ExtraName = ""
    if h == 1:
        ExtraName = "<p>seezling cheese Potatos</p>"
    elif h == 2:
        ExtraName = "<p>french fries<p>"
    elif h == 3:
        ExtraName = "<p>mashed potato</p>"
    elif h == 4:
        ExtraName = "<p>chilli fries</p>"
    elif h == 5:
        ExtraName = "<p>potato nugets</p>"
    elif h == 6:
        ExtraName = "<p>chili fills</p>"
    elif h == 7:
        ExtraName = "<p>chicken wings</p>"
    elif h == 8:
        ExtraName = "<p>Fride Chicken</p>"
    elif h == 9:
        ExtraName = "<p>Chicken nugets</p>"
    else:
        ExtraName = "<p>You havent selected any item</p>"
    return ExtraName

def ExtraAmount (a):
    Amaount = 0
    if a == 1:
        Amaount = 5
    elif a == 2:
        Amaount = 5
    elif a == 3:
        Amaount =5
    elif a == 4:
        Amaount = 5
    elif a == 5:
        Amaount = 5
    elif a == 6:
        Amaount = 5
    elif a == 7:
        Amaount = 6
    elif a == 8:
        Amaount = 6
    elif a == 9:
        Amaount = 7
    else:
        Amaount = 0
    return Amaount

def Sandwiches (h):
    Sandwichname = ""
    if h == 1:
        Sandwichname = "<p>veg.Sandwich</p>"
    elif h == 2:
        Sandwichname = "<p>Chicken Sandwich</p>"
    elif h == 3:
        Sandwichname = "<p>Paneer Sandwich</p>"
    elif h == 4:
        Sandwichname = "<p>egg.Sandwich</p>"
    elif h == 5:
        Sandwichname = "<p>Grilled Extra Cheese Sandwich</p>"
    elif h == 6:
        Sandwichname = "<p>Maxican Sandwich</p>"
    elif h == 7:
        Sandwichname = "<p>Chocolat Sandwich</p>"
    elif h == 8:
        Sandwichname = "<p>French Toste Cheese Sandwich</p>"
    elif h == 9:
        Sandwichname = "<p>Famli size Sandwich</p>"
    elif h == 10:
        Sandwichname = "<p>Club Sandwich</p>"
    elif h == 11:
        Sandwichname = "<p>Jumbo size three layered Sandwich</p>"
    elif h == 12:
        Sandwichname = "<p>Barbeque Sandwich</p>"
    elif h == 13:
        Sandwichname = "<p>Kids Sandwich</p>"
    elif h == 14:
        Sandwichname = "<p>diet Sandwich</p>"
    else:
        Sandwichname = "<p>You havent selected any item</p>"
    return Sandwichname

def SandwichAmount(v):
    Amaount = 0
    if v == 1:
        Amaount = 5
    elif v == 2:
        Amaount = 6
    elif v == 3:
        Amaount = 6
    elif v == 4:
        Amaount = 3
    elif v == 5:
        Amaount = 8
    elif v == 6:
        Amaount = 5
    elif v == 7:
        Amaount = 4
    elif v == 8:
        Amaount = 5
    elif v == 9:
        Amaount = 6
    elif v == 10:
        Amaount = 5
    elif v == 11:
        Amaount = 8
    elif v == 12:
        Amaount = 9
    elif v == 13:
        Amaount = 3
    elif v == 14:
        Amaount = 4
    else:
        Amaount = 0
    return Amaount

def Wrap(e):
    Wrapname = ""
    if e == 1:
        Wrapname = "<p>Paneer Wrap</p>"
    elif e == 2:
        Wrapname = "<p>Chicken Wrap</p>"
    elif e == 3:
        Wrapname = "<p>egg.Wrap</p>"
    elif e == 4:
        Wrapname = "<p>Chocole Wrap</p>"
    else:
        Wrapname = "<p>You havent selected any item</p>"
    return Wrapname

def WrapAmount(e):
    v = 0
    if e == 1:
        v = 10
    elif e == 2:
        v = 10
    elif e == 3:
        v = 9
    elif e == 4:
        v = 11
    else:
        v = 0
    return v

def Dips (n):
    e = ""
    if n == 1:
        e = "<p>Cream & Onion</p>"
    elif n == 2:
        e = "<p>Cream cheese</p>"
    elif n == 3:
        e = "<p>Chocochip Cream</p>"
    elif n == 4:
        e = "<p>Smoaled cheese</p>"
    elif n == 5:
        e = "<p>Heavy cheese</p>"
    elif n == 6:
        e = "<p>seezling cheese</p>"
    else:
        e = "<p>You havent selected any item</p>"
    return e

def DipsAmount (S):
    a = 0
    if S == 1:
        a = 1
    elif S == 2:
        a = 1
    elif S == 3:
        a = 2
    elif S == 4:
        a = 2
    elif S == 5:
        a = 2
    elif S == 6:
        a = 1
    else:
        a = 0
    return a


z.write("<p>--------------------W E L C O M E-------------------</p>")
z.write("<p>----------------------------------------------------</p>")
z.write("<p> |----------------------|    |--------------------|</p>")
z.write("<p> |     B U R G E R      |    |  JUICE/SOFDRINCK   |</p>")
z.write("<p> |----------------------|    |--------------------|</p>")
z.write("<p> |1.Veg.Burger    $: 6/-|    |1.Orange        $: 3/-|</p>")
z.write("<p> |2.chicken Burger$: 7/-|    |2.Coconut       $: 5/-|</p>")
z.write("<p> |3.American      ______|    |3.Mango         $:10/-|</p>")
z.write("<p> |  cheese Burger $: 8/-|    |4.Pomagranet    $: 2/-|</p>")
z.write("<p> |4.Chocolat      ______|    |5.Pepsi         $: 2/-|</p>")
z.write("<p> |         Burger $: 7/-|    |6.Cocakola      $: 2/-|</p>")
z.write("<p> |5.Minion Burger $: 4/-|    |7.Sprite        $: 2/-|</p>")
z.write("<p> |6.Maxican Burger$: 6/-|    |----------------------|</p>")
z.write("<p> |7.Special INDIAN______|    |        EXTRAS        |</p>")
z.write("<p> |  Burger        $: 8/-|    |----------------------|</p>")
z.write("<p> |8.Green Burger  $: 5/-|    |1.Seezling cheez______|</p>")
z.write("<p> |----------------------|    |  Potatos       $: 5/-|</p>")
z.write("<p>                             |2.French Fries  $: 5/-|</p>")
z.write("<p> |----------------      |    |3.Mashed Potatos$: 5/-|</p>")
z.write("<p> |      SANDWICH        |    |4.Chili Fries   $: 5/-|</p>")
z.write("<p> |----------------------|    |5.Potato nugets $: 5/-|</p>")
z.write("<p> |1.Veg.Sandwich  $: 5/-|    |6.chili fills   $: 5/-|</p>")
z.write("<p> |2.Chicken       ______|    |7.Chicken wings $: 6/-|</p>")
z.write("<p> |  Sandwich      $: 6/-|    |8.Fride Chicken $: 6/-|</p>")
z.write("<p> |3.Paneer        ______|    |9.Chicken nugets$: 7/-|</p>")
z.write("<p> |  Sandwich      $: 6/-|    |----------------------|</p>")
z.write("<p> |4.egg.Sandwich  $: 3/-|</p>")
z.write("<p> |5.Grilled Extra ______|    |----------------------|</p>")
z.write("<p> |  Cheese        ______|    |      WRAPS           |</p>")
z.write("<p> |      Sandwich  $: 8/-|    |----------------------|</p>")
z.write("<p> |6.Maxican       ______|    |1.Paneer Wrap   $:10/-|</p>")
z.write("<p> |  Sandwich      $: 5/-|    |2.Chicken Wrap  $:10/-|</p>")
z.write("<p> |7.Chocolat      ______|    |3.egg.Wrap      $: 5/-|</p>")
z.write("<p> |   Sandwich     $: 4/-|    |4.Chocolat Wrap $:11/-|</p>")
z.write("<p> |8.French Toste  ______|    |----------------------|</p>")
z.write("<p> |Cheese Sandwich $: 5/-|</p>")
z.write("<p> |9.Famli size    ______|    |----------------------|</p>")
z.write("<p> |  Sandwich      $: 6/-|    |      DIPS            |</p>")
z.write("<p> |10.Club Sandwich$: 5/-|    |----------------------|</p>")
z.write("<p> |11.Jumbo size   ______|    |1.Cream&Onion   $: 1/-|</p>")
z.write("<p> |   three layered______|    |2.Cream Cheese  $: 1/-|</p>")
z.write("<p> |   Sandwich     $: 8/-|    |3.Chocochip     ______|</p>")
z.write("<p> |12.Barbeque     ______|    |  Cream         $: 2/-|</p>")
z.write("<p> |   Sandwich     $: 9/-|    |4.Smoked Cheese $: 2/-|</p>")
z.write("<p> |13.Kids Sandwich$: 3/-|    |5.Heavy cheez   $: 2/-|</p>")
z.write("<p> |14.diet Sandwich$: 4/-|    |6.Seezling cheez$: 1/-|</p>")
z.write("<p> |----------------------|    |----------------------|</p>")

b = "yes"
c = False
while not(c):
    a = input("enter the burger number to select :")
    f_a = burgers(int(a))
    i = burgeramount(int(a))
    print(f_a)
    f = input("enter the Juice number to select :")
    A_a = Juices(int(f))
    s = JuiceAmount(int(f))
    print(A_a)
    h = input("enter the EXTRAS number to select :")
    a = Extra(int(h))
    h = ExtraAmount(int(h))
    print(a)
    v = input("enter the Sandwich number to select :")
    e = Sandwiches(int(v))
    En = SandwichAmount(int(v))
    print(e)
    d = input("enter the Wrap number to select :")
    m = Wrap(int(d))
    y = WrapAmount(int(d))
    print(m)
    t = input("enter the DIPS number to select :")
    af_A = Dips(int(t))
    l = DipsAmount(int(t))
    print(af_A)
    print("")
    print(f_a)
    print(A_a)
    print(a)
    print(e)
    print(m)
    print(af_A)
    z = input("would you like to check out :")
    if z == "yes":
        c = True

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
z.close()
