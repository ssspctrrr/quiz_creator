# import tkinter

# define get_boolean function

# define get_specific_input function

# define get_integer_input function

# define change_settings function

# define store_questions function

# define check_correct_answer function

# define show_correct_answer_screen

# define question_screen

# define show_correct_answer_screen function

# define main function
    # open file for reading
        # iterate over lines 0 to 6
            # save topic of quiz
            # save settings from file

        # if enable_change_settings == True
            # input if user wants to change settings for this quiz:
            # if yes
                # call change_settings function

        # call store_questions function

    # set up root window

    # set question_screen as tkframe
    # set show_correct_answer_screen as tkframe
    # set end_screen as tkframe

    # iterate over the keys in questions dictionary (this will be made in store_questions function)
        # iterate over number of tries
            # call main_screen(questions[question], tries, score)
            # check if is_answer_correct (will be made in check_correct_answer function)
                # score += 1
                # break
            # tries += 1
        # check if settings[show_correct_answer_each_question]
            # call show_correct_answer_screen function

    # check if settings[show_score_end]
        # put score as tk.label
    # check if correct_answers (this dictionary will be made in store_questions function)
        # put correct_answers as tk.label

    # run tk.mainloop()

# create main function guard