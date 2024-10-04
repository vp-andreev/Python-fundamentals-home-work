digits_to_executed = list(map(int, input().split()))
executor = int(input())

order_of_executions = []

index = (executor - 1) % len(digits_to_executed)

while digits_to_executed:
    order_of_executions.append(digits_to_executed[index])
    digits_to_executed.pop(index)
    if digits_to_executed:
        index = (index + executor - 1) % len(digits_to_executed)


# print(f"[{','.join(map(str, order_of_executions))}]")

new_orde_of_execute = str(order_of_executions).replace(' ', '')

print(new_orde_of_execute)
