import random

WORDS = [
    "python", "node", "html", "css", "java",  
    "react", "angular", "django", "flask", "next",
    "fastapi", "pandas", "php", "javascript", "typescript"
]

random_word = random.choice(WORDS).upper()


def main():
    
    print("\n<---Guess a word--->")
    char = ["_" for _ in random_word]
    incorrect_guesses = 6
    
    while True:
        user_input = input("\nEnter a character: ").upper()
        correct_guess = False
        
        for i, letter in enumerate(random_word):
            if letter == user_input:
                char[i] = letter
                correct_guess = True
                
        if not correct_guess:
            incorrect_guesses -= 1
            print(f"\n{incorrect_guesses} Guesses left out of 6.\n")
                
        print(" ".join(char))
        
        if incorrect_guesses == 0:
            print("\nIt's Over. You ran out of guesses.")
            print(f"The correct word was {random_word}")
            break

        if "_" not in char:
            print("\nYou guessed it! The word was", random_word)
            break
       


if __name__ == "__main__":
    main()