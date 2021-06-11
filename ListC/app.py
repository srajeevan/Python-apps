a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# one line
print([i for i in a if i % 2 == 0])
# multiple line solution
b = []
for i in a:
    if i%2 == 0:
      b.append(i)
print(b)