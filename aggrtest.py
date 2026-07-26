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


# collections.defaultdict — grouping into buckets

from collections import defaultdict

orders = [("alice", 50), ("bob", 30), ("alice", 20)]
totals = defaultdict(int)
for name, amount in orders:
    totals[name] += amount
# {'alice': 70, 'bob': 30}



## defaultdict(list) — grouping into lists
from collections import defaultdict

people = [("eng", "sam"), ("sales", "amy"), ("eng", "joe")]
by_dept = defaultdict(list)
for dept, name in people:
    by_dept[dept].append(name)
# {'eng': ['sam', 'joe'], 'sales': ['amy']}


#dict comprehension aggregation
prices = {"apple": 1.0, "banana": 0.5, "cherry": 3.0}
expensive = {k: v for k, v in prices.items() if v > 0.5}
# {'apple': 1.0, 'cherry': 3.0}



from itertools import groupby

orders = [("alice", 50), ("alice", 20), ("bob", 30)]
for key, group in groupby(orders, key=lambda x: x[0]):
    print(key, sum(amount for _, amount in group))
# alice 70
# bob 30