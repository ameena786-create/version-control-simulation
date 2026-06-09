grade = int(input("Enter your grade(0-100):"))
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
                    print(f"Your letter grade is: {letter}")
                    if letter in ["A", "B", "C"]:
                        print("Congratulations! You passed!")   
                        else:
                            print("keep trying! You can do it!")