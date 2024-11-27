# for loops

for item in ("Python"):
    print(item)

for item in ['ash', 'bash', 'cash']:
    print(item)

for item in range(10):
    print(item)

for item in range(5,10):
    print(item)

for item in range(5,10, 2):
    print(item)

prices = [10, 20, 30]
for price in prices:
    total = sum(prices)
print(f'Total: {total}')

for x in range(4):
    for y in range(3):
        print(f'{x}, {y}')
