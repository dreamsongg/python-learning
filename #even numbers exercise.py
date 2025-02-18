#even numbers exercise


totalsum = 0

for even in range(0, 101, 2):
    if even % 2 == 0:
        totalsum += even

print(totalsum)