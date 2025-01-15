import random 

def validation_input(input_number):
    
    if not input_number.isdigit():
        print("Invalid Input. Please enter a number. ")
        return False
    
    input_number = int(input_number)

    if input_number < 1 or input_number > 100:
        print("Invalid Number. Please enter a valid number. ")
        return False
    
    return True

def start_game():
    random_number = random.randint(1, 100)
    score = 100

    while True:
        input_number = input("Enter your guess between 1 and 100 or 'q' to exit. ")

        if input_number.lower() == 'q':
            print("GoodBye...!!!")
            break

        if not validation_input(input_number):
            continue

        input_number = int(input_number)

        if input_number == random_number:
            print(f'You guessed curreclty. your score is {score}')

            wanna_play = input("Do you want to play again(y/n)? : ")

            if wanna_play.lower() == 'y':
                random_number = random.randint(1, 100)
                score = 100
                continue
            else:
                print("Goodbye...!!!")
                break

        elif input_number > random_number:
            print("You guessed too high")
        else:
            print("you guess too low")

        score -= 10
    
    else:
        print(f"Unfortunately you loss. The number was {random_number}")

if __name__ == '__main__':
    start_game()

