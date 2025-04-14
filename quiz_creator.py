# define get_specific_input(prompt, possible_values=["y", "n"])
    # loop infinitely
        #try
            # get user_input with input(prompt, possible_values).lower()

            # check if user_input not in possible_values
                # raise Exception
            # else if possible_values != ["y", "n"]
                # return user_input
            # else if user_input == possible_values[0]
                # return True
            # else if user_input == possible_values[1]
                # return False
        # except
            # print "Invalid value entered. Enter only {choice[0]} or {choice[1]}."
            # continue

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
    # enable_change_settings: True
    # timer: False
    # tries: 1
    # show_correct_answer_each_question: True
    # show_correct_answer_at_end: False
    # show_score_every_question: False
    # show_score_end: True

# loop infinitely
    # print settings of the quiz

    # get_specific_input("if user wants ", ["1", "2", "3", "4", "5", "6", "7", "q"])
        # check if setting_input == "q"
            # print "you will now enter the questions.\n"
            # break
        # else if change_setting == "1"
            # get setting_input from get_integer_input("Enter y to enable the settings to be changed in the quiz program")
            # assign settings[enable_change_settings] == setting_input
        # else if change_setting == "2"
            # get setting_input from get_integer_input("Enter number of seconds for timer or N/n to remove timer")
            # assign settings[timer] = settings_input
        # else if change_setting == "3"
            # get setting_input from get_integer_input("Enter value for amount of tries", limit=4)
            # assign settings[tries] = settings_input
        # else if change_setting == "4"
            # get setting_input from get_specific_input("Enter y if user wants to show correct answer each question")
            # assign settings[show_correct_answer_each_question] = settings_input
        # else if change_setting == "5"
            # get setting_input from get_specific_input("Enter y if user wants to show all correct answer at the end of quiz")
            # assign settings[show_correct_answer_at_end] = setting_input
        # else if change_setting == "6"
            # get setting_input from get_specific_input("Enter y if user wants to show score after every question")
            # assign settings[show_score_every_question] = setting_input
        # else
            # get setting_input from get_specific_input("Enter y if user wants to show score at the end of quiz")
            # assign settings[show_score_end] = setting_input
    
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