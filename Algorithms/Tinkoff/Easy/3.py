# Done
n, t = list(map(int, input().split()))
floors = list(map(int, input().split()))
floor_id = int(input()) - 1

if floors[floor_id] - floors[0] <= t:
    ans = floors[-1] - floors[0]
elif floors[-1] - floors[floor_id] <= t:
    ans = floors[-1] - floors[0]
else:
    ans = floors[-1] - floors[0] + min(floors[floor_id] - floors[0], floors[-1] - floors[floor_id])
print(ans)
