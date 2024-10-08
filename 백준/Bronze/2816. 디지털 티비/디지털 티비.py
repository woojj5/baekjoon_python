cnt = 0
def down(cursor):
    cursor+=1
    print("1", end="")
    return cursor

def switch(cursor):
    if cursor > 0:
        click[cursor], click[cursor-1] = click[cursor-1], click[cursor]
        cursor -=1
        print("4", end="")
    return cursor

num = int(input())
click = []
for i in range(num):
    click.append(input())
cursor = 0

while True:
    if click[cursor] != "KBS1":
        cursor = down(cursor)
    else:
        cursor = switch(cursor)
    if click[0] == "KBS1":
        break

while True:
    if click[cursor] != "KBS2":
        cursor = down(cursor)
    else:
        cursor = switch(cursor)
    if click[1] == "KBS2":
        break
