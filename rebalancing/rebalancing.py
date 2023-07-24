current_state = [
    {
        "account_id": 1,
        "balance": 1_000_000
    },
    {
        "account_id": 2,
        "balance": 2000_000
    },
    {
        "account_id": 3,
        "balance": 1000_000
    },
    {
        "account_id": 4,
        "balance": 2000_000
    },
]

target_state = [
    {
        "account_id": 1,
        "balance": 800_000
    },
    {
        "account_id": 2,
        "balance": 2500_000
    },
    {
        "account_id": 3,
        "balance": 1200_000
    },
    {
        "account_id": 4,
        "balance": 1500_000
    },
]

def moveMoney(current, target):
    changes = []
    for i in range(len(current)):
        changes.append(target[i]["balance"] - current[i]["balance"])
    money_movements = []
    for i in range(len(current)):
        if changes[i] < 0:
            for x in range(0, len(current)):
                if changes[x] > 0 and x != i:
                    apply = min(changes[x], abs(changes[i]))
                    money_movements.append({"from_account": i + 1, "to_account": x + 1, "amount": apply})
                    changes[i] += apply
                    changes[x] -= apply
                    if changes[i] == 0:
                        break

    return money_movements

final = moveMoney(current_state, target_state)

print(final)
