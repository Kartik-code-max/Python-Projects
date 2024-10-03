def quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "Who wrote 'Harry Potter'?": "J.K. Rowling",
        "What is the square root of 16?": "4"
    }
    score = 0
    for question, correct_answer in questions.items():
        answer = input(f"{question} ")
        if answer.lower() == correct_answer.lower():
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")

    print(f"\nYour final score is {score}/{len(questions)}")


quiz()
