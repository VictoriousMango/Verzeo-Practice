# Prepare the Question list for the game
Questions = [
    'Who is the current Prime Minister of India ?',
    'Who is the current President of India ?',
    'Which of the following is not one of the 7 seas of the world.',
    'Which of the following is not one of the 8 wonders of the world',
    'What is the full form of acronym KBC'
]

# Correct answers of the given questions are:
Answers = [
    'Mr. Narendra Modi',
    'Ram Nath Kovind',
    'Arabian Sea',
    'J.E.B. Stuart Monument',
    'Kon Banega Corerpati'
]

# Options available for the quizer
Options = [
    ['Mr. Narendra Modi', 'Mr. Manmohan Singh', 'Sri Atal Bihari Vajpayee', 'Mr. Inder Kumar Gujral'],
    ['Mr. Ram Nath Kovind', 'Mr. Pranab Mukherjee', 'Mrs. Pratibha Patil', 'Dr. A.P.J. Abdul Kalam'],
    ['Pacific Ocean', 'Atlantic Ocean', 'Arabian Sea', 'Souther Ocean'],
    ['Colosseum', 'J.E.B. Stuart Monument', 'Machu Picchu', 'Christ the Redeemer'],
    ['Knowledge Based Configuration', 'Knox Beauty College', 'Keyboard Controller', 'Kon Banega Corerpati']
]

# To play the game
def Play():
    print("You Choose to play the game")

# To view your scores
def Scores():
    print("You choose to view the game")

# Main KBC Game function
def KBC():
    while True:
        print("Welcome to KBC Game")
        '''
        We need to proved three choices, 
        1. To Play the Game
        2. To View your scores
        3. To Exit the Application
        ''' 
        choice = input("Choose one of the below to proceed further: \n1. Play \n2. View Scores \n3. Exit:\n")
        
        if choice == '1':
            Play()
        elif choice == '2':
            Scores()
        elif choice == '3':
            break
        else :
            print("You have entered a wrong choice, please enter again")

KBC()