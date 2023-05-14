def play_quiz(questions):
    score = 0
    for question, options, answer in questions:
        print(question)
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        user_answer = input("Enter the number of your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            if options[int(user_answer) - 1] == answer:
                print("Correct!")
                score += 1
            else:
                print("Wrong!")
        else:
            print("Invalid input!")
    print(f"\nQuiz completed! You scored {score} out of {len(questions)}.")


# Quiz questions
quiz_questions = [
    ("What is the capital of France?", ["London", "Paris", "Berlin", "Rome"], "Paris"),
    ("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars"),
    ("Who painted the Mona Lisa?", ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Michelangelo"],
     "Leonardo da Vinci"),
    ("What is the largest ocean in the world?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
     "Pacific Ocean"),
    ("Which country is home to the kangaroo?", ["Australia", "Brazil", "Canada", "India"], "Australia"),
    ("Who wrote the play Romeo and Juliet?",
     ["William Shakespeare", "George Bernard Shaw", "Oscar Wilde", "Jane Austen"], "William Shakespeare"),
    ("What is the chemical symbol for gold?", ["Go", "Ag", "Au", "Gd"], "Au"),
    ("In which year did World War II end?", ["1939", "1942", "1945", "1950"], "1945"),
    ("What is the tallest mountain in the world?", ["Mount Everest", "K2", "Kangchenjunga", "Makalu"], "Mount Everest"),
    ("Who is the author of the Harry Potter book series?",
     ["J.R.R. Tolkien", "J.K. Rowling", "C.S. Lewis", "Stephenie Meyer"], "J.K. Rowling")
]

# Start the quiz
print("Welcome to the Quiz Game!")
play_quiz(quiz_questions)
