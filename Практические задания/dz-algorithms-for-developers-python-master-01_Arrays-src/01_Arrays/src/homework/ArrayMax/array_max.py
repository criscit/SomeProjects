from typing import List

# Task #1
def find_smallest_transaction(transactions: List[int]) -> int:
    max_trx = transactions[0]
    for i in range(len(transactions)):
        if transactions[i] > max_trx:
            max_trx = transactions[i]
    return max_trx


# Task #2
def find_best_student_mistakes(students: List[int]) -> int:
    min_m = students[0]
    for i in range(len(students)):
        if students[i] < min_m:
            min_m = students[i]
    return min_m


# Task #3
def find_average_time(times: List[int]) -> float:
    accumulator = 0
    for el in times:
        accumulator += el

    return accumulator / len(times)


# Task #4
def find_most_profitable_client(income: List[List[int]]) -> int:
    max_total = income[0][0]
    best_i = 0
    for i in range(len(income)):
        total = 0
        for el in income[i]:
            total += el

        if total > max_total:
            max_total = total
            best_i = i

    return best_i