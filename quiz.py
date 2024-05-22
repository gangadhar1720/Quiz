# Constants for the quiz
CORRECT = 4
INCORRECT= -1
QUESTIONS= 5
MAX_SCORE =QUESTIONS * CORRECT

# Questions that are going to be asked
questions = [
    "What is the keyword to define a function in Python?",
    "Which of the following is a correct way to declare a variable in Python?",
    "How do you create a dictionary in Python?",
    "What is the correct way to check if a value is not equal to another value in Python?",
    "Which of the following is used to handle exceptions in Python?"
]

# Options for the above questions
options = [
    ["def", "function", "func", "define"],
    ['var x = 5', 'x = 5', 'int x = 5', 'declare x = 5'],
    ["dict = {1: 'one', 2: 'two'}", "dict = (1: 'one', 2: 'two')", "dict = [1: 'one', 2: 'two']", "dict = <1: 'one', 2: 'two'>"],
    ["a <> b", "a != b", "a =! b", "a not= b"],
    ["try...except", "do...except", "try...handle", "do...catch"]
]

# Correct answers for the questions
correct_answers = [1, 2, 1, 2, 1]

# Function to display the welcome message and instructions
def display_welcome_message():
    print("_______Welcome to the Python quiz_________")
    print("-------------Instructions--------------")
    print("This quiz contains 5 basic questions related to Python programming.")
    print("Each question contains 4 options and a single correct answer.")
    print("Please respond with one of the following options: 1, 2, 3, or 4.")
    print("Each correct answer awards 4 points, while each incorrect answer deducts 1 point.")

# Function to get valid input from the user
def get_valid_input(prompt, valid_range):
    while True:
        try:
            guess = int(input(prompt))
            if guess in valid_range:
                return guess
            else:
                print(f"Please enter a number between {valid_range[0]} and {valid_range[-1]}")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to evaluate the user's answer and update the score
def evaluate(guess, correct_answer, score):
    if guess == correct_answer:
        print(f"Correct, you have scored 4 points")
        score += CORRECT
    else:
        print("Oops, you have chosen the incorrect option")
        print(f"The correct answer is option {correct_answer}")
        score += INCORRECT
    return score

# Function to provide a complement based on the user's total score
def provide_complement(score):
    if score == MAX_SCORE:
        return "Excellent! You got all answers right!"
    elif 15 <= score < MAX_SCORE:
        return "Good job! Keep it up!"
    elif 10 <= score < 15:
        return "Nice effort! You're getting there!"
    elif 5 <= score < 10:
        return "Keep trying! Practice makes perfect!"
    else:
        return "Don't give up! Keep learning and you'll improve!"

# Main function to conduct the quiz
def quiz(questions, options):
    ans=input("To start the quiz enter start :  ").lower()
    if ans=="start":
      score=0
      display_welcome_message()

      # Loop through each question
      for i in range(QUESTIONS):
          print(f"{i + 1}. {questions[i]}")
          # Display the options for the current question
          for j in range(len(options[i])):
              print(f"{j + 1}) {options[i][j]}")
          # Get the user's answer and evaluate it
          guess = get_valid_input("Select one of the above options  : ", range(1, 5))
          score = evaluate(guess, correct_answers[i], score)

      # Display the user's total score and complement
      print(f"Your total score is {score}/{MAX_SCORE}")
      print(provide_complement(score))
    else:
      print("OKAY BYE")
      

# Run the quiz
quiz(questions, options)
