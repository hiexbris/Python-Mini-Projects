root = [1,10,4,3,null,7,9,12,8,6,null,null,2]

a = 1
sum = 1
odd = True
while sum <= len(root):
    if odd:
        for _ in range(0, a):
            if root[a] % 2 != 0 or root[a] == null:
                game_on = True
            else: game_on = False
        odd = False
    else:
        for _ in range(0, a):
            if root[a] % 2 == 0 or root[a] == null:
                game_on = True
            else: game_on = False
        odd = True
    a *= 2
    sum += a