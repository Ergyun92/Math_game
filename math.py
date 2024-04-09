import random, time
operators = ["+", "-", "/", "*"]


def generate_problem():
    left = random.randint(10, 25)
    right = random.randint(2, 5)
    operator = random.choice(operators)
    task = str(left) + " " + operator + " " + str(right)
    result = eval(task)
    return task, result


print("Let's begin!")
print()
wrong = 0
start = time.time()
for i in range(10):
    task, result = generate_problem()
    while True:
        solution = input("Task number" + str(i + 1) + ": " + task + " = ")
        if solution == str(result):
            break
        wrong += 1

end = time.time()
duration = round(end - start, 2)

print(f"You have completed the tasks in {duration} seconds with {wrong} mistakes.")
