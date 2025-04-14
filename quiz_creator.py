# define get_specific_input(prompt, possible_values=["y", "n"])
def get_specific_input(prompt, possible_values=["y", "n"]):
    # loop infinitely
    while True:
        try:
            # get user_input with input(prompt, possible_values).lower()
            user_input = input(prompt).lower()

            # check if user_input not in possible_values
            if user_input not in possible_values:
                # raise Exception
                raise Exception
            # else if possible_values != ["y", "n"]
            elif possible_values != ["y", "n"]:
                # return user_input
                return user_input
            # else if user_input == possible_values[0]
            elif user_input == possible_values[0]:
                # return True
                return True
            # else if user_input == possible_values[1]
            elif user_input == possible_values[1]:
                # return False
                return False
        # except
        except:
            # print "Invalid value entered. Enter only {possible_values}."
            print(f"\nInvalid value entered. Enter only {possible_values}")

# define get_integer_input(prompt, limit=None)
    # loop inifinitely
        # try
            # get user_input with input(prompt).lower()

            # check if limit is None and user_input == "n"
                # return False
            # else if limit is None and user_input != "n" and user_input is not numerical
                # raise Exception

            # convert user_input to integer
            # check if user_input < 1
                # raise Exception
            # else if limit is not None and user_input > limit
                # raise Exception
            # return user_input
        # except
            # print "Invalid value entered. Enter only integer from 1 to {limit}."
            # check if limit is None
                # print in the same line "Or enter N/n to remove timer."
            # continue

# define write_question(file) function
    # write to file "==============================\n"

    # get question
    # write to file "{question}\n"

    # assign letter_choices as A,B,C,D
    # shuffle letter_choices

    # define choices as empty dictionary

    # get correct_answer
    # assign the value correct_answer to key of first shuffled letter_choices

    # iterate three times
        # get a possible_choice
        # assign value possible_choice to key of current letter_choices

    # iterate over sorted choices dictionary
        # check if the current possible_choice is the correct_answer
            # write to file the sign of correct_answer ">>>" + current letter_choice + value of possible_choice + "\n"
        # else
            # write to file the current letter_choice + value of possible_choice + "\n"

    # write to file "==============================\n"

# ask user the topic of quiz
topic = input("Enter the topic of this quizbelow by finishing the sentence.\nThis is a quiz about ")

# set a dictionary named settings as...
settings = {
    # enable_change_settings: True
    "enable_change_settings": True,
    # timer: False
    "timer": False,
    # tries: 1
    "tries": 1,
    # show_correct_answer_each_question: True
    "show_correct_answer_each_question": True,
    # show_correct_answer_at_end: False
    "show_correct_answer_at_end": False,
    # show_score_every_question: False
    "show_score_every_question": False,
    # show_score_end: True
    "show_score_end": True
}

# print "These are the default settings"
print("The quiz will use these default settings:")
# loop infinitely
while True:
    # print settings of the quiz
    for setting in settings:
        print(f"{setting}: {settings[setting]}")

    print("")
    # get_specific_input("if user wants ", ["1", "2", "3", "4", "5", "6", "7", "q"])
    settings_prompt = """\
Enter...
Q/q: Quit Adjusting the settings and finalize the current settings.
1: Adjust enable_change_setting which adjusts whether the quiztaker can change the settings in the quiz program
2: Disable timer or enable and input a timer (in seconds) for every question
3: Enter how many tries the quiztaker has to get a correct answer per question
4: Adjust show_correct_answer_each_question which adjusts whether the correct answer is shown after every question
5: Adjust show_correct_answer_at_end which adjusts whether all correct answers are shown at the end of quiz
6: Adjust show_score_every_question which adjusts whether the score is shown while taking the quiz
7: Adjust "show_score_end" which adjusts whether the score is shown at the end
Input: 
"""
    change_settings = get_specific_input(settings_prompt, ["q", "1", "2", "3", "4", "5", "6", "7"])
    # check if change_settings == "q"
    if change_settings == "q":
        # print "you will now enter the questions.\n"
        print("\nSettings saved. You will now enter the quiz questions.\n")
        # break
        break
    # else if change_setting == "1"
    elif change_settings == "1":
        # get setting_input from get_integer_input("Enter y to enable the settings to be changed in the quiz program")
        print("enable settings change")
        # assign settings[enable_change_settings] == setting_input
    # else if change_setting == "2"
    elif change_settings == "2":
        # get setting_input from get_integer_input("Enter number of seconds for timer or N/n to remove timer")
        print("timer")
        # assign settings[timer] = settings_input
    # else if change_setting == "3"
    elif change_settings == "3":
        # get setting_input from get_integer_input("Enter value for amount of tries", limit=4)
        print("tries")
        # assign settings[tries] = settings_input
    # else if change_setting == "4"
    elif change_settings == "4":
        # get setting_input from get_specific_input("Enter y if user wants to show correct answer each question")
        print("show correct answer each question")
        # assign settings[show_correct_answer_each_question] = settings_input
    # else if change_setting == "5"
    elif change_settings == "5":
        # get setting_input from get_specific_input("Enter y if user wants to show all correct answer at the end of quiz")
        print("show all correct answer at end")
        # assign settings[show_correct_answer_at_end] = setting_input
    # else if change_setting == "6"
    elif change_settings == "6":
        # get setting_input from get_specific_input("Enter y if user wants to show score after every question")
        print("show score every question")
        # assign settings[show_score_every_question] = setting_input
    # else
    else:
        # get setting_input from get_specific_input("Enter y if user wants to show score at the end of quiz")
        print("show score at end")
        # assign settings[show_score_end] = setting_input

    # print "The settings are now changed into the following:"
    print("The settings are now changed into the following:")
    
# open file "quiz_questions_configuration.txt" as file
    # write to file "A quiz on {topic}\n"

    # iterate over keys of settings
        # write to file "{key} = {settings[key]}\n"

    # write to file "START#########################\n"

    # loop infinitely
        # write to file "{question}"
        
        # get should_continue from get_specific_input("Enter c if program should continue. Enter q if not", ["c", "q"])
        # check if should_continue
            # write to file "CONTINUE======================\N"
            # print "You will now enter a new question and its choices.\n"
            # continue
        # else
            # write to file "END***************************\n"
            # print "Quiz creator is now being terminated."
            # break