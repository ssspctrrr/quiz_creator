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
def get_integer_input(prompt, limit=None):
    # loop inifinitely
    while True:
        # try
        try:
            # get user_input with input(prompt).lower()
            user_input = input(prompt)

            # check if limit is None and user_input == "n"
            if limit is None and user_input == "n":
                # return False
                return False
            # else if limit is None and user_input != "n" and user_input is not numerical
            elif limit is None and not user_input.isnumeric():
                # raise Exception
                raise Exception

            # convert user_input to integer
            user_input = int(user_input)
            # check if user_input < 1
            if user_input < 1:
                # raise Exception
                raise Exception
            # else if limit is not None and user_input > limit
            elif limit is not None and user_input > limit:
                # raise Exception
                raise Exception
            # return user_input
            return user_input
        # except
        except:
            # print "Invalid value entered. Enter only positive integer greater than 0 "
            print("\nInvalid value entered. Enter only positive integer greater than 0 ", end="")
            # check if limit is None
            if limit is None:
                # print in the same line "Or enter N/n to remove timer."
                print("Or enter N/n to remove timer.")
            # else
            else:
                # print in the same line "to {limit}"
                print(f"to {limit}.")

# define write_question(file) function
def write_question(file):
    # write to file "==============================\n"
    file.write("==============================\n")

    # get question
    question = input("Enter question: ")
    # write to file "{question}\n"
    file.write(f"{question}\n")

    # get correct_answer
    correct_answer = input("Enter the correct answer: ")
    # write to file ">>>" + correct_answer
    file.write(f">>>{correct_answer}\n")

    # iterate three times
    for i in range(0, 3):
        # input choice
        choice = input(f"Enter choice #{i + 1}: ")
        # write choice to file
        file.write(f"{choice}\n")

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
print("\nThe quiz will currently use these default settings:")
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
1: Adjust enable_change_setting which adjusts whether the quiztaker can change the settings in the quiz program.
2: Disable timer or enable and input a timer (in seconds) for every question.
3: Enter how many tries the quiztaker has to get a correct answer per question.
4: Adjust show_correct_answer_each_question which adjusts whether the correct answer is shown after every question.
5: Adjust show_correct_answer_at_end which adjusts whether all correct answers are shown at the end of quiz.
6: Adjust show_score_every_question which adjusts whether the score is shown while taking the quiz.
7: Adjust "show_score_end" which adjusts whether the score is shown at the end.
Input: """
    change_settings = get_specific_input(settings_prompt, ["q", "1", "2", "3", "4", "5", "6", "7"])
    # check if change_settings == "q"
    if change_settings == "q":
        # print "you will now enter the questions.\n"
        print("\nSettings saved. You will now enter the quiz questions.\n")
        # break
        break
    # else if change_setting == "1"
    elif change_settings == "1":
        # get setting_input from get_specific_input("Enter y to enable the settings to be changed in the quiz program")
        enable_change_settings_prompt = """
You are now adjusting enable_change_settings. Enter...
Y/y: Allow the quiztaker to change the settings of this quiz in the quiz program.
N/n: Disallow the quiztaker to change the settings of this quiz in the quiz program.
Input: """
        setting_input = get_specific_input(enable_change_settings_prompt)
        # assign settings[enable_change_settings] = setting_input
        settings["enable_change_settings"] = setting_input
    # else if change_setting == "2"
    elif change_settings == "2":
        # get setting_input from get_integer_input("Enter number of seconds for timer or N/n to remove timer")
        timer_prompt = """
You are now adjusting timer settings. Enter...
N/n: To remove timer for every question.
Any positive integer: To create a timer for every question with that entered amount of seconds.
Input: """
        setting_input = get_integer_input(timer_prompt)
        # assign settings[timer] = settings_input
        settings["timer"] = setting_input
        print(settings["timer"])
    # else if change_setting == "3"
    elif change_settings == "3":
        # get setting_input from get_integer_input("Enter value for amount of tries", limit=4)
        tries_prompt = """
You are now adjusting the tries setting. Enter...
Positive integer from 1 to 4: Allow quiztaker to have entered amount of times of tries while answer is wrong.
Input: """
        setting_input = get_integer_input(tries_prompt, 4)
        # assign settings[tries] = settings_input
        settings["tries"] = setting_input
    # else if change_setting == "4"
    elif change_settings == "4":
        # get setting_input from get_specific_input("Enter y if user wants to show correct answer each question")
        show_correct_answer_each_question_prompt = """
You are now adjusting show_correct_answer_each_question_prompt. Enter...
Y/y: Enable this setting so that the correct answer is shown after each questions in the quiz.
N/n: Disable this so that the correct answer is not shown after each questions in the quiz.
Input: """
        setting_input = get_specific_input(show_correct_answer_each_question_prompt)
        # assign settings[show_correct_answer_each_question] = settings_input
        settings["show_correct_answer_each_question"] = setting_input
    # else if change_setting == "5"
    elif change_settings == "5":
        # get setting_input from get_specific_input("Enter y if user wants to show all correct answer at the end of quiz")
        show_correct_answer_at_end_prompt = """
You are now adjusting show_correct_answer_at end. Enter...
Y/y: Enable this setting so that there is a special screen at the end of the quiz that shows all correct answers.
N/n: Disable this setting so that there is no special screen at the end of the quiz that shows all correct answers.
Input: """     
        setting_input = get_specific_input(show_correct_answer_at_end_prompt)
        # assign settings[show_correct_answer_at_end] = setting_input
        settings["show_correct_answer_at_end"] = setting_input
    # else if change_setting == "6"
    elif change_settings == "6":
        # get setting_input from get_specific_input("Enter y if user wants to show score after every question")
        show_score_every_question_prompt = """
You are now adjusting show_score_every_question. Enter...
Y/y: Enable this setting so that the score is shown while the quiz is still being taken.
N/n: Disable this setting so that the score is not shown while the quiz is still being taken.
Input: """
        setting_input = get_specific_input(show_score_every_question_prompt)
        # assign settings[show_score_every_question] = setting_input
        settings["show_score_every_question"] = setting_input
    # else
    else:
        # get setting_input from get_specific_input("Enter y if user wants to show score at the end of quiz")
        show_score_end_prompt = """
You are now adjusting show_score_end. Enter...
Y/y: Enable this setting so that the score is shown at the end of the quiz.
N/n: Enable this setting so that the score is not shown at the end of the quiz.
Input: """
        setting_input = get_specific_input(show_score_end_prompt)
        # assign settings[show_score_end] = setting_input
        settings["show_score_end"] = setting_input

    # print "The settings are now changed into the following:"
    print("\nThe settings are now changed into the following:")
    
# open file "quiz_questions_configuration.txt" as file
with open("quiz_questions_config.txt", "w") as file:
    # write to file "A quiz on {topic}\n"
    file.write(f"A QUIZ ABOUT: {topic}\n")

    # iterate over keys of settings
    for setting in settings:
        # write to file "{key} = {settings[key]}\n"
        file.write(f"{setting} = {settings[setting]}\n")

    # write to file "START#########################\n"
    file.write("START#########################\n")

    # loop infinitely
    while True:
        # use function write_question(file)
        write_question(file)
        
        # get should_continue from get_specific_input("Enter y if program should continue. Enter n if not")
        should_continue_prompt = """
Continue entering questions? Enter...
Y/y: Enter a new question
N/n: End this program and finalize the entered questions & choices.
Input: """
        should_continue = get_specific_input(should_continue_prompt)
        # check if should_continue
        if should_continue:
            # print "You will now enter a new question and its choices.\n"
            print("\nYou will now enter a new question and its choices.\n")
        # else
        else:
            # write to file "=============================="
            # write to file "END***************************"
            # print "Quiz creator is now being terminated."
            # break
            break