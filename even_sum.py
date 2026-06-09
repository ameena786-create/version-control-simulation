sum_even = 0
for i in range(1, 51):
    if i % 2 == 0:
        sum_even += i

print("Sum using for loop:", sum_even)

sum_even2 = 0
i = 1

while i <= 50:
    if i % 2 == 0:
        sum_even2 += i
    i += 1

print("Sum using while loop:", sum_even2)