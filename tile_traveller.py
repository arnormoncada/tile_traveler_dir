N = "(N)orth"
S = "(S)outh"
E = "(E)ast"
W = "(W)est"
x=1
y=1


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
        print("You can travel: (N)orth.")
        directions = input("Direction: ")
        directions = directions.upper()
        if directions == "N":
            x,y = stadsetning(directions,x,y)
        else:
            print("Not a valid direction!")    
    elif x==1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        directions = input("Direction: ")
        directions = directions.upper()
        if directions == "N" or directions == "S" or directions == "E":
            x,y = stadsetning(directions,x,y)
        else:
            print("Not a valid direction!")
    elif x==1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
        directions = input("Direction: ")
        directions = directions.upper()
        if directions == "S" or directions == "E":
            x,y = stadsetning(directions,x,y)
        else:
            print("Not a valid direction!")
    elif x==2 and y == 1:
        print("You can travel: (N)orth.")
        directions = input("Direction: ")
        directions = directions.upper()
        if directions == "N":
            x,y = stadsetning(directions,x,y)
        else:
            print("Not a valid direction!")
    elif x==2 and y==2:
        print("You can travel: (S)outh or (W)est.")
        directions = input("Direction: ")
        directions = directions.upper()
        if directions == "S" or directions == "W":
            x,y = stadsetning(directions,x,y)
        else:
            print("Not a valid direction!")
    elif x==2 and y==3:
        print("You can travel: (E)ast or (W)est.")
        directions = input("Direction: ")
        directions = directions.upper()
        if directions == "W" or directions == "E":
            x,y = stadsetning(directions,x,y)
        else:
            print("Not a valid direction!")
    elif x==3 and y==3:
        print("You can travel: (S)outh or (W)est.")
        directions = input("Direction: ")
        directions = directions.upper()
        if directions == "S" or directions == "W":
            x,y = stadsetning(directions,x,y)
        else:
            print("Not a valid direction!")
    elif x==3 and y==2:
        print("You can travel: (N)orth or (S)outh.")
        directions = input("Direction: ")
        directions = directions.upper()
        if directions == "S" or directions == "N":
            x,y = stadsetning(directions,x,y)
        else:
            print("Not a valid direction!")
    elif x==3 and y==1:
        break

print("Victory!")
        
        
        

