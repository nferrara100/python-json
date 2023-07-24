# Account Balancing

-   The primary objective of the task is to write a working and correct solution.
-   Any optimisations are nice to have and if you feel that doing them upfront is
    detrimental to the primary objective they can be added later.

We have a number of different bank accounts that we use to fund transfers.

From time-to-time, we need to "rebalance" these accounts. Rebalancing involves
transferring funds from one or more accounts to another account.

Please write a function that takes an input (current_state, target_state) and returns
[money_movements].

The algorithm must:

-   Not send money to and from the same account.
-   Not output more than 1 money movement from and to the same pair of accounts.

```json
current_state = [
    {
        "account_id": 1,
        "balance": 1000000
    },
    {
        "account_id": 2,
        "balance": 2000000
    },
    {
        "account_id": 3,
        "balance": 1000000
    },
    {
        "account_id": 4,
        "balance": 2000000
    },
]

target_state = [
    {
        "account_id": 1,
        "balance": 800000
    },
    {
        "account_id": 2,
        "balance": 2500000
    },
    {
        "account_id": 3,
        "balance": 1200000
    },
    {
        "account_id": 4,
        "balance": 1500000
    },
]

money_movements = [
    {
        "from_account": 1,
        "to_account": 2,
        "amount": 200000
    },
    ...
]
```
