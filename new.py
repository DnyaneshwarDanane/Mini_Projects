import random

history = []

print("🎯 Lucky Number Predictor")
print("Type 'q' to quit.\n")

while True:
    user = input("Enter your lucky number (1-100): ")

    if user.lower() == "q":
        break

    try:
        num = int(user)

        if num < 1 or num > 100:
            print("Enter a number between 1 and 100.\n")
            continue

        history.append(num)

        if len(history) < 3:
            prediction = random.randint(1, 100)
        else:
            avg = sum(history[-3:]) // 3
            prediction = max(1, min(100, avg + random.randint(-5, 5)))

        print(f"🤖 AI Prediction: Your next lucky number could be {prediction}")

        if prediction == num:
            print("🎉 Wow! Exact match!")
        elif abs(prediction - num) <= 5:
            print("✨ Very close!")
        else:
            print("😊 Let's keep learning!")

        print()

    except ValueError:
        print("Please enter a valid number.\n")

print("\nHistory:", history)
print("Thanks for playing!")
#git remote add origin https://github.com/DnyaneshwarDanane/Mini_Projects.git