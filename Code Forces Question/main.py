n = 5
f = 3
k = 1
a = [3, 3, 2, 3, 2]
b = a[:]

b.sort(reverse=True)
print(a)
print(b)

if b[k-1] > a[f-1]:
    print("NO")
elif b[k-1] == a[f-1]:
    if b[k] == b[k-1]:
        print("MAYBE")
    else:
        print("YES")
elif b[k-1] < a[f-1]:
    print("YES")

