ages = [49, 31, 19, 66, 94, 27, 15]

top1_age = 0
top2_age = 0

# Найдем первый максимум в массиве
for i in range(len(ages)):
    top1_age = max(top1_age, ages[i])

# Добавим второй проход по массиву
# И рассмотрим только элементы, которые меньше первого максимума
for i in range(len(ages)):
    if ages[i] < top1_age:
        top2_age = max(top2_age, ages[i])

print("First Max: %d\nSecond Max: %d" % (top1_age, top2_age))
