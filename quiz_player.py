# import tkinter
import tkinter as tk

import random

# define get_boolean function
def get_boolean(line, prefix):
    bool_value = line.removeprefix(prefix).strip().lower() == "true"
    return bool_value

# define get_specific_input function
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

# define get_integer_input function with prompt as parameter
def get_integer_input(prompt):
    # loop inifinitely
    while True:
        # try
        try:
            # get user_input and convert to int
            user_input = int(input(prompt))
            # check if user_input < 1
            if user_input < 1:
                # raise Exception
                raise Exception
            # else if user_input > 4
            elif user_input > 4:
                # raise Exception
                raise Exception
            # return user_input
            return user_input
        # except
        except:
            # print "Invalid value entered. Enter only positive integer greater than 0 "
            print("\nInvalid value entered. Enter only positive integer greater than 0 to 4")

# define change_settings function with settings as parameter
def change_settings(settings):
    # loop infinitely
    while True:
        # create a prompt variable to which setting to change
        change_setting_prompt = """
Enter...
Q/q: Quit Adjusting the settings and finalize the current settings.
1: Enter how many tries the quiztaker has to get a correct answer per question.
2: Adjust show_correct_answer_each_question which adjusts whether the correct answer is shown after every question.
3: Adjust show_correct_answer_at_end which adjusts whether all correct answers are shown at the end of quiz.
4: Adjust show_score_every_question which adjusts whether the score is shown while taking the quiz.
5: Adjust "show_score_end" which adjusts whether the score is shown at the end.
Input: """
        # set setting_to_change by calling get_specific_input with possible_values as ["q", "1", "2", "3", "4", "5"]
        setting_to_change = get_specific_input(change_setting_prompt, ["q", "1", "2", "3", "4", "5"])

        # check if setting_to_change == "q"
        if setting_to_change == "q":
            # print "the current settings will now apply and you will now proceed to the quiz."
            print("\nThe current settings will now apply and you will now proceed to the quiz")
            # break loop
            break

        # elif setting_to_change == "1"
        elif setting_to_change == "1":
            # create tries_prompt
            tries_prompt = """
You are now adjusting the tries setting. Enter...
Positive integer from 1 to 4: Allow quiztaker to have entered amount of times of tries while answer is wrong.
Input: """
            # set setting_input by calling get_integer_input
            setting_input = get_integer_input(tries_prompt)
            # assign settings[tries] = setting_input
            settings["tries"] = setting_input

        # elif setting_to_change == "2"
        elif setting_to_change == "2":
            # create show_correct_answer_each_question_prompt
            show_correct_answer_each_question_prompt = """
You are now adjusting show_correct_answer_each_question_prompt. Enter...
Y/y: Enable this setting so that the correct answer is shown after each questions in the quiz.
N/n: Disable this so that the correct answer is not shown after each questions in the quiz.
Input: """
            # set setting_input by calling get_specific_input
            setting_input = get_specific_input(show_correct_answer_each_question_prompt)
            # assign settings[show_correct_answer_each_question] = setting_input
            settings["show_correct_answer_each_question"] = setting_input

        # elif setting_to_change == "3"
        elif setting_to_change == "3":
            # create show_correct_answer_at_end_prompt
            show_correct_answer_at_end_prompt = """
You are now adjusting show_correct_answer_at end. Enter...
Y/y: Enable this setting so that there is a special screen at the end of the quiz that shows all correct answers.
N/n: Disable this setting so that there is no special screen at the end of the quiz that shows all correct answers.
Input: """
            # set setting_input by calling get_specific_input
            setting_input = get_specific_input(show_correct_answer_at_end_prompt)
            # assign settings[show_correct_answer_at_end] = setting_input
            settings["show_correct_answer_at_end"] = setting_input

        # elif setting_to_change == "4"
        elif setting_to_change == "4":
            # create show_score_every_question_prompt
            show_score_every_question_prompt = """
You are now adjusting show_score_every_question. Enter...
Y/y: Enable this setting so that the score is shown while the quiz is still being taken.
N/n: Disable this setting so that the score is not shown while the quiz is still being taken.
Input: """
            # set setting_input by calling get_specific_input
            setting_input = get_specific_input(show_score_every_question_prompt)
            # assign settings[show_score_every_question] = setting_input
            settings["show_score_every_question"] = setting_input

        # elif setting_to_change == "5"
        elif setting_to_change == "5":
            # create show_score_end_prompt
            show_score_end_prompt = """
You are now adjusting show_score_end. Enter...
Y/y: Enable this setting so that the score is shown at the end of the quiz.
N/n: Enable this setting so that the score is not shown at the end of the quiz.
Input: """
            # set setting_input by calling get_specific_input
            setting_input = get_specific_input(show_score_end_prompt)
            # assign settings[show_score_end_prompt] = setting_input
            settings["show_score_end"] = setting_input

        # print settings
        print("\nThe settings have now been changed to...")
        for setting in settings:
            print(f"{setting}: {settings[setting]}")

    # return settings
    return settings

# define store_questions function with file as parameter
def store_questions(file, should_show_right_answer):
    # create empty questions dictionary
    questions = {}
    # create empty shuffled_questions dictionary
    shuffled_questions = {}

    # check if settings[show_correct_answer_at_end]
    if should_show_right_answer:
        # create empty global correct_answers dictionary
        global correct_answers
        correct_answers = {}

    # define question_counter as 0
    question_counter = 0

    # iterate over lines in file
    for line in file:
        # elif line == "END***************************"
        if line == "END***************************":
            # break loop
            break
        # check if line == "=============================="
        elif line == "==============================\n":
            # set question_counter = 5
            question_counter = 5
        # elif question_counter == 5
        elif question_counter == 5:
            # assign current_question as line
            current_question = line.strip()
            # assign questions[current_question] as empty array
            questions[current_question] = []
            question_counter -= 1
        # elif question_counter in range(2,5)
        elif question_counter in range(2,5):
            # append line to questions[current_question]
            questions[current_question].append(line.strip())
            question_counter -= 1
        # elif question_counter == 1
        elif question_counter == 1:
            # append line to questions[current_question]
            questions[current_question].append(line.strip())
            # shuffle the choices in questions[current_question]
            random.shuffle(questions[current_question])

        # if settings[show_correct_answer_at_end] and line startswith ">>>"
        if should_show_right_answer and line.startswith(">>>"):
            # correct_answers[current_question] = line.removeprefix(">>>").strip()
            correct_answers[current_question] = line.removeprefix(">>>").strip()

    # shuffle questions and store it into shuffled_question
    questions_keys = list(questions.keys())
    random.shuffle(questions_keys)
    for question in questions_keys:
        shuffled_questions[question] = questions[question]

    # returned shuffled_questions
    return shuffled_questions

# define check_correct_answer function
def check_correct_answer(root, settings, selected, correct_answer, check_answer_label, questions, questions_list, topic):
    # declare score, question_index, tries as global
    global score, question_index, tries

    # check if selected == correct_answer:
    if selected == correct_answer:
        # add 1 to score
        score += 1
        #config check_answer_label with text=Correct
        check_answer_label.config(text="Correct!", fg="green")
        # add 1 to question_index
        question_index += 1
        # call main_screen with a delay
        root.after(1000, lambda: main_screen(root, settings, question_index, questions_list, questions, topic, score))
    # else
    else:
        # decrement tries by 1
        tries -= 1
        # check if tries > 0
        if tries > 0:
            # config check_answer_label with text=Wrong + tries
            check_answer_label.config(text=f"Wrong Answer! {tries} left.", fg="red")
        # else:
        else:
            # message = Wrong
            message = "Wrong!"
            # if settings[show_correct_each_question]
            if settings["show_correct_answer_each_question"]:
                # add "Correct answer if {correct_answer}" to message
                message += f" Correct answer is {correct_answer}"
            # config check_answer_label with text=message
            check_answer_label.config(text=message, fg="red")
            # add 1 to question_index
            question_index += 1
            # call question_screen with delay
            root.after(1500, lambda: main_screen(root, settings, question_index, questions_list, questions, topic, score))

# define main_screen with root, question_index, questions_list, questions, topic, score
def main_screen(root, settings, question_index, questions_list, questions, topic, score):
    # define tries_left as settings[tries]
    global tries
    tries = settings["tries"]

    # check if current_index == len(questions_list)
    if question_index >= len(questions_list):
        # destroy all current widgets in root
        for widget in root.winfo_children():
            widget.destroy()
        # call end_screen()
        root.after(0, lambda: end_screen(topic, root, score, settings, len(questions_list)))
        return
    
    # destroy all current widgets in root
    for widget in root.winfo_children():
        widget.destroy()

    # create topic_label
    topic_label = tk.Label(root, text=topic, font=("Times New Roman", 20))
    # place topic_label to root
    topic_label.place(relx=0.5, rely=0.075, anchor="center")

    # create check_answer_label with no text
    check_answer_label = tk.Label(root, text="", font=("Arial", 12))
    # place check_answer_label to root
    check_answer_label.place(relx=0.5, rely=0.935, anchor="center")

    # create tries_label
    tries_label = tk.Label(root, text=f"Total tries: {tries}", font=("Arial", "12"))
    # place tries_label to root
    tries_label.place(relx=0.035, rely=0.965, anchor="sw")

    # check if settings[show_score_every_question]
    if settings["show_score_every_question"]:
        # create score_label
        score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 12))
        # place score_label to root
        score_label.place(relx=0.965, rely=0.965, anchor="se")

    # create question_screen frame
    question_screen = tk.Frame(root, bg="pink")
    # place question_screen to root
    question_screen.place(relx=0.5, rely=0.5, anchor="center")

    # assign question = questions_list[question_index]
    question = questions_list[question_index]
    # define choice_letter as [A,B,C,D]
    choice_letter = ["A. ", "B. ", "C. ", "D. "]
    # define empty choices array
    choices = []

    # iterate over choice in questions[question]
    for choice in questions[question]:
        # check if choice startswith ">>>"
        if choice.startswith(">>>"):
            # assign choice = choice.removeprefix(>>>)
            choice = choice.removeprefix(">>>")
            # assign choice = choice_letter[0] + choice
            choice = choice_letter[0] + choice
            # assign correct_answer = choice
            correct_answer = choice
        # else
        else:
            # assign choice = choice_letter[0] + choice
            choice = choice_letter[0] + choice
        # append choice to choices
        choices.append(choice)
        # pop choice_letter[0]
        choice_letter.pop(0)

    # create question_label
    question_label = tk.Label(question_screen, text=question, font=("Arial", 11))
    question_label.config(width=40, height=3, wraplength=300)
    # pack question_label to question_screen
    question_label.pack(ipadx=5, ipady=5, padx=5, pady=5)

    # create buttons_frame
    buttons_frame = tk.Frame(question_screen, bg="lightblue")
    # pack buttons_frame to question_screen
    buttons_frame.pack()

    # create button_A with text=choices[0], command=check_correct_answer
    button_A = tk.Button(buttons_frame, text=choices[0], font=("Arial", 11))
    button_A.config(width=20, height=3, wraplength=170)
    button_A.config(command=lambda selected=choices[0]: check_correct_answer(
        root, settings, selected, correct_answer, check_answer_label, questions, questions_list, topic))
    # grid place button_A to buttons_frame
    button_A.grid(row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

    # create button_B with text=choices[1], command=check_correct_answer
    button_B = tk.Button(buttons_frame, text=choices[1], font=("Arial", 11))
    button_B.config(width=20, height=3, wraplength=170)
    button_B.config(command=lambda selected=choices[1]: check_correct_answer(
        root, settings, selected, correct_answer, check_answer_label, questions, questions_list, topic))
    # grid place button_B to buttons_frame
    button_B.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

    # create button_C with text=choices[2], command=check_correct_answer
    button_C = tk.Button(buttons_frame, text=choices[2], font=("Arial", 11))
    button_C.config(width=20, height=3, wraplength=170)
    button_C.config(command=lambda selected=choices[2]: check_correct_answer(
        root, settings, selected, correct_answer, check_answer_label, questions, questions_list, topic))
    # grid place button_C to buttons_frame
    button_C.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

    # create button_D with text=choices[3], command=check_correct_answer
    button_D = tk.Button(buttons_frame, text=choices[3], font=("Arial", 11))
    button_D.config(width=20, height=3, wraplength=170)
    button_D.config(command=lambda selected=choices[3]: check_correct_answer(
        root, settings, selected, correct_answer, check_answer_label, questions, questions_list, topic))
    # grid place button_D to buttons_frame
    button_D.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

# define end_screen function
def end_screen(topic, root, score, settings, num_questions):
    # create end_frame
    end_frame= tk.Label(root)
    # place end_frame to root
    end_frame.place(relx=0.5, rely=0.5, anchor="center")

    # create end_label
    end_label = tk.Label(end_frame, text=f"{topic} Quiz\nFinished!", font=("Times New Roman", 20), wraplength=500)
    # pack end_label to end_frame
    end_label.pack(padx=5, pady=5)

    # check if settings[show_score_end]
    if settings["show_score_end"]:
        # create score_label with text="Score: {score}/{len(correct_answer)}"
        score_label = tk.Label(end_frame, text=f"Score: {score}/{num_questions}", font=("Times New Roman", 15))
        # pack score_label to end_frame
        score_label.pack(padx=5, pady=5)

    # check if settings[show_correct_answer_at_end]
    if settings["show_correct_answer_at_end"]:
        # define correct_answers_text
        correct_answers_text = ""
        # iterate over question in correct_answers
        for question in correct_answers:
            # concatenate "{question} >>> {correct_answers[question]}\n" to correct_answers_text
            correct_answers_text += f"{question} >>> {correct_answers[question]}\n"
        # create correct_answers_label with text=correct_answers_text
        correct_answers_label = tk.Label(end_frame, text=f"Correct Answers:\n{correct_answers_text}".strip())
        correct_answers_label.config(font=("Arial", 13), wraplength=500, justify="left")
        # pack correct_answers_label to end_frame
        correct_answers_label.pack(padx=5, pady=5)

    # create exit_button with command=root.destroy()
    exit_button = tk.Button(root, text="Press to exit\nquiz player", font=("Arial", 10))
    exit_button.config(highlightthickness=5, highlightbackground="black", highlightcolor="black")
    exit_button.config(command=root.destroy)
    # pack exit_button to root in lower left corner
    exit_button.place(relx=0.95, rely=0.95, anchor="se")

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
            elif index == 1:
                settings["enable_change_settings"] = get_boolean(line, "enable_change_settings = ")
            elif index == 2:
                settings["tries"] = int(line.removeprefix("tries = "))
            elif index == 3:
                settings["show_correct_answer_each_question"] = get_boolean(line, "show_correct_answer_each_question = ")
            elif index == 4:
                settings["show_correct_answer_at_end"] = get_boolean(line, "show_correct_answer_at_end = ")
            elif index == 5:
                settings["show_score_every_question"] = get_boolean(line, "show_score_every_question = ")
            elif index == 6:
                settings["show_score_end"] = get_boolean(line, "show_score_end = ")
        
        # reset read cursor to 0
        file.seek(0)

        # if enable_change_settings == True
        if settings["enable_change_settings"]:
            # input if user wants to change settings for this quiz:
            print("CURRENT SETTINGS:\n")
            for key in settings:
                print(f"{key}: {settings[key]}")

            change_settings_prompt = """\nSince changing settings is enabled, do you want to change the current settings? Enter...
Y/y: Change the settings (NOTE: Changing the settings here will not permanently change the settings for this quiz file).
N/n: Keep the current settings and proceed to the quiz.
Input: """
            should_change_settings = get_specific_input(change_settings_prompt)
            # if yes
            if should_change_settings:
                # call change_settings function
                settings = change_settings(settings)

        # call store_questions function
        questions = store_questions(file, settings["show_correct_answer_at_end"])

        # print quiz message
        print("\nYou will now answer the Quiz.")
        print("Note: It is recommended to answer/play the quiz in its default or full-screen size.")
        print("Happy Quiztaking :) !!!")

    # set up root window
    root = tk.Tk()
    root.geometry("667x500")

    # define empty score
    global score
    score = 0
    # define questions_list
    questions_list = list(questions.keys())

    # define question_index
    global question_index
    question_index = 0

    # call main_screen
    main_screen(root, settings, question_index, questions_list, questions, topic, score)

    # run tk.mainloop()
    tk.mainloop()

# create main function guard
if __name__ == "__main__":
    main()