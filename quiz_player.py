# import tkinter
import tkinter as tk

# define get_boolean function
def get_boolean(line, prefix):
    bool_value = line.removeprefix(prefix).strip().lower() == "true"
    return bool_value

# define get_specific_input function

# define get_integer_input function

# define change_settings function

# define store_questions function

# define check_correct_answer function

# define show_correct_answer_screen

# define question_screen

# define show_correct_answer_screen function

# define main function
def main():
    # open file for reading
    with open("quiz_questions_config.txt", "r") as file:
        settings = {}
        # iterate over lines 0 to 6
        for index, line in enumerate(file):
            # save topic of quiz
            if index == 0:
                topic = line.removeprefix("A QUIZ ABOUT: ").strip()
            # save settings from file
            elif index == 2:
                settings["tries"] = int(line.removeprefix("tries = "))
            elif index == 3:
                settings["show_correct_answer_each_question"] = get_boolean(line, "show_correct_answer_each_question = ")
        print(settings["show_correct_answer_each_question"])

        # if enable_change_settings == True
            # input if user wants to change settings for this quiz:
            # if yes
                # call change_settings function

        # call store_questions function

    # set up root window
    root = tk.Tk()

    # set question_screen as tkframe
    question_screen = tk.Frame()
    # set show_correct_answer_screen as tkframe
    show_correct_answer_screen = tk.Frame()
    # set end_screen as tkframe
    end_screen = tk.Frame()

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
        # put score as tk.label on end screen
    # check if correct_answers (this dictionary will be made in store_questions function)
        # put correct_answers as tk.label on end screen

    # run tk.mainloop()
    tk.mainloop()

# create main function guard
if __name__ == "__main__":
    main()