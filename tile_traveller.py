print("You can travel: (N)orth")
directions = input("Direction: ")

N = "(N)orth"
S = "(S)outh"
E = "(E)ast"
W = "(W)est"

x_pos , y_pos = 1,1
start_point = x_pos ,y_pos

def update(x):
    return x+1
def fun(direct, x, y):
    if direct == N:
        return x, y +1
    if direct == S:
        return x, y-1
    if direct == E:
        return x+1,y
    if direct == W:
        return x-1, y




"""while True:
    if (x_pos == 1) and (y_pos == 1):
        print(f"You can travel: {N}.")
        direction = str(input("Direction: "))
        while True:
            if direction.lower() == 'n':
                y_pos +=1
                break
            else: 
                print("Not a valid direction")
                direction = str(input("Direction: "))
    if (x_pos == 1) and (y_pos == 2):
        print(f"You can travel: {N} or {E} or {S}.")
        direction = str(input("Direction: "))
        while True:
            if direction.lower() in ('n', 's', 'e'):
                if direction.lower() == 'n':
                    y_pos += 1
                    break
                elif direction.lower() == 's':
                    y_pos -= 1
                    break
                elif direction.lower() == 'e':
                    x_pos += 1
                    break
            else: 
                print("Not a valid direction!")
                direction = str(input("Direction: "))
    if (x_pos == 1) and (y_pos == 3):
        print(f"You can travel: {E} or {S}.")
        direction = str(input("Direction: "))
        while True:
            if direction.lower() in ('s', 'e'):
                if direction.lower() == 's':
                    y_pos -= 1
                    break
                elif direction.lower() == 'e':
                    x_pos += 1
                    break
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))"""

        