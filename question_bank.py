#---------------------------------------
#  Question Bank
#   Talha khan
#   271045552
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("Which is the largest planet in solar system?" , "Jubiper"),
        ("What is the percentage of nitrogen in air?", "78")
        ("What is the speed of light in m/s" , "3x10^8")
        ("Chemical formula of ozone" , "O3")
    ],
        
    "Maths":[
        ("What is the value of π (pi) to two decimal places?" , "3.14"),
        ("What is square root of 144?" "12")
        ("What is the sum of number divide by total of numbers?" , "Average"),
        ("Total internal angles of Triangle" , "180")
        (" What is the sum of the interior angles of an octagon ?(In degrees)" , "1080")
        
    ],
}

hints = {
    "Science": [
        ("hydrogen and oxygen")
        ("5th planet")
        ("Most abndant gas in air")
        ("8th the power of 10")
        ("Consists on oxygen")
    ],
    "Maths":[
        ("near to three")
        ("Greater than 10")
        ("Middle value")
        ("Multiple of 60")
        ("Above 1000")
        
    ]
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    if category.lower() == "maths":
        selected_question = random.choice(Maths)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------




