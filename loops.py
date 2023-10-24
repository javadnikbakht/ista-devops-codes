x = range(1, 10, 2)
print(list(x))


for item in range(0, 10, 2):
    print(item)
else:
    print("tamoom shod baba!")

for havij in ["havij1", "havij2", "parazit", "havij3"]:
    print(havij)

i = 0
while i < 100:
    print(i)
    i += 1


for item in range(100):
    if item == 8:
        break
    print(item)


for item in range(100):
    if not(item % 8):
        continue
    print(item)