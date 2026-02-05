from typing import List
from collections import defaultdict
"""
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.
"""

class Transaction:
    def __init__(self, idx, transaction):
        self.id = idx
        name, time, amount, city = transaction.split(",")
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city

    # def __str__(self):
    #     return f"{self.name},{self.time},{self.amount},{self.city}"

    # def __repr__(self):
    #     return f"{self.name},{self.time},{self.amount},{self.city}"


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        records = defaultdict(list)
        for idx, transaction in enumerate(transactions):
            instance = Transaction(idx, transaction)
            records[instance.name].append(instance)

        invalids = set()
        for instances in records.values():
            n = len(instances)
            for i in range(n):
                t1 = instances[i]
                if t1.amount > 1000:
                    invalids.add(t1.id)
                for j in range(i+1, n):
                    t2 = instances[j]
                    if t1.city != t2.city and abs(t1.time - t2.time) <= 60:
                        invalids.add(t1.id)
                        invalids.add(t2.id)
        ans = []
        for i in range(len(transactions)):
            if i in invalids:
                ans.append(transactions[i])
        return ans


transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
transactions = ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
print(Solution().invalidTransactions(transactions))

