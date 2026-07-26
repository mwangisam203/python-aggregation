scores = [85, 92, 78, 90]
total = sum(scores)  # 345

#generator expression
orders = [{"amount": 50}, {"amount": 30}, {"amount": 20}]
total = sum(o["amount"] for o in orders)  # 100


# len() + conditional generator — filtered count
users = [{"active": True}, {"active": False}, {"active": True}]
active_count = sum(1 for u in users if u["active"])  # 2

## frequency count

from collections import Counter

words = ["apple", "banana", "apple", "orange", "apple"]
counts = Counter(words)  # Counter({'apple': 3, 'banana': 1, 'orange': 1})
counts.most_common(2)    # [('apple', 3), ('banana', 1)]