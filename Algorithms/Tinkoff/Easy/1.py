# Done
a, b, c, d = list(map(int, input().split()))
cost = 0
if d > b:
    cost = a + c * (d - b)
else:
    cost = a
print(cost)