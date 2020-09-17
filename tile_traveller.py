valid=""
N = "(N)orth"
S = "(S)outh"
E = "(E)ast"
W = "(W)est"
x=1
y=1
def update(x):
    return x+1
def stadsetning(direct, x, y): # Benedikt hjálpaði okkur með þetta
    if direct == "N":
        return x, y +1
    if direct == "S":
        return x, y-1
    if direct == "E":
        return x+1,y
    if direct == "W":
        return x-1, y
while True:
    if x == 1 and y == 1:
        print("You can travel: (N)orth")
        directions = input("Direction: ")
        if directions != "N":
            print("Not a valid direction!")
        else:
            x,y = stadsetning(directions,x,y)
    elif x==1 and y == 2:
        print("You can travel: (N)orth")
        print("You can travel: (S)outh")
        print("You can travel: (E)ast)")
        directions = input("Direction: ")
        if directions != "N" or directions != "S" or directions != "E":
            print("Not a valid direction!")
        else:
            x,y = stadsetning(directions,x,y)
    elif x==1 and y == 3:
        print("You can travel: (S)outh")
        print("You can travel: (E)ast)")
        directions = input("Direction: ")
        if directions != "S" or "E":
            print("Not a valid direction!")
        else:
            x,y = stadsetning(directions,x,y)
    elif x==2 and y == 1:
        print("You can travel: (N)orth")
        directions = input("Direction: ")
    elif x==2 and y==2:
        print("You can travel: (S)outh")
        print("You can travel: (W)est)")
        directions = input("Direction: ")
    elif x==2 and y==3:
        print("You can travel: (E)ast")
        print("You can travel: (W)est)")
        directions = input("Direction: ")
    elif x==3 and y==3:
        print("You can travel: (S)outh")
        print("You can travel: (W)est)")
        directions = input("Direction: ")
    elif x==3 and y==2:
        print("You can travel: (S)outh")
        print("You can travel: (N)orth)")
        directions = input("Direction: ")
else: 
    print("Victory!")
