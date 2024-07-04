import random
import sys
import time
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Set to female voice (assuming the second voice is female, may vary)
engine.setProperty('voice', voices[1].id)

# Function to speak text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to simulate typing
def type_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # Adjust typing speed here
    print()

# Questions, options, and answers
questions = [
    {"question": "What is the capital of France?", 
    "options": ["Paris", "London", "Berlin", "Madrid"], 
    "answer": 0},
    {"question": "What is 2+2?", 
    "options": ["3", "4", "5", "6"], 
    "answer": 1},
    {"question": "What is the largest planet?", 
    "options": ["Earth", "Mars", "Jupiter", "Saturn"], 
    "answer": 2},
    {"question": "Who wrote 'Hamlet'?", 
    "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"], 
    "answer": 1},
    {"question": "Which element has the chemical symbol 'O'?", 
    "options": ["Oxygen", "Gold", "Silver", "Iron"], 
    "answer": 0},
    {"question": "What is the capital of Japan?", 
    "options": ["Tokyo", "Kyoto", "Osaka", "Hiroshima"], 
    "answer": 0},
    {"question": "What is the square root of 64?", 
    "options": ["6", "7", "8", "9"], 
    "answer": 2},
    {"question": "In which year did World War II end?", 
    "options": ["1942", "1945", "1948", "1950"], 
    "answer": 1},
    {"question": "Which planet is known as the Red Planet?", 
    "options": ["Earth", "Mars", "Jupiter", "Venus"], 
    "answer": 1},
    {"question": "What is the largest mammal?", 
    "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 
    "answer": 1},
    {"question": "Who painted the Mona Lisa?", 
    "options": ["Vincent Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], 
    "answer": 2},
    {"question": "What is the capital of Australia?", 
    "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"], 
    "answer": 2},
    {"question": "What is the smallest prime number?", 
    "options": ["0", "1", "2", "3"], 
    "answer": 2},
    {"question": "Which ocean is the largest?", 
    "options": ["Atlantic", "Indian", "Arctic", "Pacific"], 
    "answer": 3},
    {"question": "Who discovered penicillin?", 
    "options": ["Marie Curie", "Albert Einstein", "Alexander Fleming", "Isaac Newton"], 
    "answer": 2}
]

# Prize amounts
prizes = [
    1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,
    640000, 1250000, 2500000, 5000000, 10000000
]

# Lifeline flags
lifelines = {"50-50": True, "ask the audience": True, "phone a friend": True}

# Function to use 50-50 lifeline
def use_50_50(correct_answer, options):
    incorrect_options = [i for i in range(len(options)) if i != correct_answer]
    removed_options = random.sample(incorrect_options, 2)
    for i in removed_options:
        options[i] = None
    return options

# Function to simulate audience help
def ask_audience(correct_answer, options):
    type_text("\nAudience Poll Results:")
    speak_text("Audience Poll Results.")
    for i, option in enumerate(options):
        if i == correct_answer:
            result = f"Option {i + 1}: {random.randint(50, 80)}%"
        else:
            result = f"Option {i + 1}: {random.randint(1, 20)}%"
        type_text(result)
        speak_text(result)

# Function to simulate phone a friend help
def phone_a_friend(correct_answer, options):
    type_text("\nYou have chosen to phone a friend.")
    speak_text("You have chosen to phone a friend.")
    # Simulate friend's suggestion (70% chance of correct answer)
    if random.random() < 0.7:
        result = f"Your friend thinks the correct answer is: Option {correct_answer + 1}"
    else:
        other_options = [i for i in range(len(options)) if i != correct_answer]
        result = f"Your friend thinks the correct answer is: Option {random.choice(other_options) + 1}"
    type_text(result)
    speak_text(result)

# Function to display the prize table
def display_prize_table():
    type_text("\nPrize Table:")
    for i, prize in enumerate(prizes):
        if i < 5:
            role = "Fastest Finger"
        elif i < 10:
            role = "Entry Level"
        else:
            role = "Main Game"
        prize_text = f"{role}: Rs.{prize}"
        type_text(prize_text)
        speak_text(prize_text)

def play_game():
    contestant_name = input("Please enter the contestant's name: ")
    type_text(f"Welcome to the KBC, {contestant_name}!")
    speak_text(f"Welcome to the KBC, {contestant_name}!")
    
    current_prize = 0

    for i, q in enumerate(questions):
        type_text(f"\nCurrent Prize: Rs.{current_prize}")
        type_text(f"Playing for: Rs.{prizes[i]}")
        question_text = f"\nQuestion {i + 1}: {q['question']}"
        type_text(question_text)
        speak_text(question_text)
        
        for j, option in enumerate(q['options']):
            if option is not None:
                option_text = f"{j + 1}. {option}"
                type_text(option_text)
                speak_text(option_text)

        while True:
            choice = input("\nEnter your choice (1-4), 'lifeline' to use a lifeline, 'prize' to see prize table, or 'quit' to take the money: ").strip().lower()

            if choice == "quit":
                quit_text = f"{contestant_name}, you have decided to quit. You won Rs.{current_prize}."
                type_text(quit_text)
                speak_text(quit_text)
                return
            elif choice == "prize":
                display_prize_table()
                continue
            elif choice == "lifeline":
                if not any(lifelines.values()):
                    no_lifeline_text = "No lifelines available."
                    type_text(no_lifeline_text)
                    speak_text(no_lifeline_text)
                    continue

                lifeline_choice = input("Choose a lifeline ('50-50', 'ask the audience', or 'phone a friend'): ").strip().lower()
                if lifeline_choice == "50-50" and lifelines["50-50"]:
                    q['options'] = use_50_50(q['answer'], q['options'])
                    lifelines["50-50"] = False
                elif lifeline_choice == "ask the audience" and lifelines["ask the audience"]:
                    ask_audience(q['answer'], q['options'])
                    lifelines["ask the audience"] = False
                elif lifeline_choice == "phone a friend" and lifelines["phone a friend"]:
                    phone_a_friend(q['answer'], q['options'])
                    lifelines["phone a friend"] = False
                else:
                    invalid_lifeline_text = "Invalid or already used lifeline."
                    type_text(invalid_lifeline_text)
                    speak_text(invalid_lifeline_text)
                
                # Redisplay options after lifeline use without repeating the question
                for j, option in enumerate(q['options']):
                    if option is not None:
                        option_text = f"{j + 1}. {option}"
                        type_text(option_text)
                        speak_text(option_text)
            else:
                try:
                    choice = int(choice) - 1
                    if choice == q['answer']:
                        current_prize = prizes[i]
                        correct_text = f"Correct, {contestant_name}! You have won Rs.{current_prize}."
                        type_text(correct_text)
                        speak_text(correct_text)
                        break
                    else:
                        if i < 5:
                            penalty = 0
                        elif i < 10:
                            penalty = 1000
                        else:
                            penalty = 320000
                        wrong_text = f"Wrong answer, {contestant_name}. You receive a penalty of Rs.{penalty}."
                        type_text(wrong_text)
                        speak_text(wrong_text)
                        current_prize -= penalty
                        return
                except ValueError:
                    invalid_input_text = "Invalid input. Please try again."
                    type_text(invalid_input_text)
                    speak_text(invalid_input_text)

    congrats_text = f"Congratulations, {contestant_name}! You have won the grand prize of Rs.{current_prize} and a brand new car!"
    type_text(congrats_text)
    speak_text(congrats_text)

# Start the game
play_game()
