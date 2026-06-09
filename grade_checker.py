grade = int(input("Enter your grade (0-100): "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

print("Your grade is:", letter)

# Message
if grade >= 70:
    print("Congratulations! You passed!")
else:
    print("Keep trying! You can do it!")