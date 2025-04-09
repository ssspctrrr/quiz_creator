# ask user the topic of quiz

# set a dictionary named settings as...
    # ask_settings_in_quiz: True
    # timer: False
    # tries: 1
    # show_correct_answer_each_question: True
    # show_correct_answer_at_end: False
    # show_score_every_question: False
    # show_score_end: True

# loop infinitely
    # print settings of the quiz

    # get_specific_input("if user wants to change and which setting to change", ["1", "2", "3", "4", "5", "6", "7", "q"])
        # check if setting_input == "q"
            # print "you will now enter the questions.\n"
            # break

        # check if change_setting == "1"
            # get setting_input from get_specific_input("Enter y if user wants to ask settings in quiz program. Enter n if not")
            # assign settings[ask_settings_in_quiz] = settings_input
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