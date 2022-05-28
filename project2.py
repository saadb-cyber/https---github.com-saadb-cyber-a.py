from Menu import Menu1

#providing burgers names to numbers
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

#Burger rate and quantity file
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

#providing juice names to 
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

#Juice rate and quantity file
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

#providing Extras names to inputs
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

#Extras rate and quantity file
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

#Providing names to inputs
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

# rate and quantity file
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

#providing names to inputs
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

#rate and quantity file
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

#providing names to inputs
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

#rate and quantity file
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

print (Menu1)


