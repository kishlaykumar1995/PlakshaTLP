import random

for i in
X = []
count = 0
for j in range(1_00_000):
    X= []
    for i in range(50):
        X.append(random.randint(1,366))

    if len(X) - len(set(X)) == 0:
        count+=1

print(count*100/1_00_000)

[random.randint(1,366) for x in range(1,50)]