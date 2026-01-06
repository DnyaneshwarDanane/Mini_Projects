print("welcome to the python quiz !")

questions = [ "1. which keyword is used to create loop in python? \n " 
              "A) loop\n B) for\n c) repeat ",

              "2) which data type is immutable?\n"
              " A) list\n B) dictionary\n C) tuple ",

              "3) what is output of 5%2?\n "
              "A) 1\n B) 0\n C) 2"

]

Answers = ('b' , 'c' , 'a')

score = 0
i = 0

while i < len(questions):
    print("\n " + questions[i])
    user_ans = input(" Enter your answer A/B/C or or type 'exit' to quit : ").lower()
    if user_ans == Answers[i]:
        print("correct!")
        score+=1
    elif user_ans == 'exit':
        print("Quiz exited")
        break
    else:
        print("wrong answer!")

    i+=1


print(f"\n your final score is : {score} / {len(questions)}")

if score == len(questions):
    print("perfect score! well done ")
elif score >= 2:
    print("good job , keep practicing")
else:
    print("your fail")
