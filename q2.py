import tkinter

math_points = 0
history_points = 0
chem_points = 0
english_points = 0


def display_subject():
    
    if subject_pick.get()=="math":
       math_instructions.pack()
       math_q1.pack(pady=20)
       ma1.pack()
       ma2.pack()
       ma3.pack()
       ma4.pack()
       mq1_button.pack(pady=20)
       math_q2.pack(pady=20)
       ma5.pack()
       ma6.pack()
       ma7.pack()
       ma8.pack()
       mq2_button.pack(pady=20)
       math_q3.pack(pady=20)
       ma9.pack()
       ma10.pack()
       ma11.pack()
       ma12.pack()
       mq3_button.pack(pady=20)
       finalsubmit.pack()
       points.pack()

    if subject_pick.get()=="chem":
       chem_instructions.pack()
       chem_q1.pack(pady=20)
       ca1.pack()
       ca2.pack()
       cq1_button.pack(pady=20)
       chem_q2.pack(pady=20)
       ca3.pack()
       ca4.pack()
       cq2_button.pack(pady=20)
       chem_q3.pack(pady=20)
       ca5.pack()
       ca6.pack()
       cq3_button.pack(pady=20)
       finalsubmit.pack()
       points2.pack()
    
    elif subject_pick.get()=="history":
       history_instructions.pack()
       history_q1.pack(pady=20)
       ha1.pack()
       ha2.pack()
       hq1_button.pack(pady=20)
       history_q2.pack(pady=20)
       ha3.pack()
       ha4.pack()
       hq2_button.pack(pady=20)
       history_q3.pack(pady=20)
       ha5.pack()
       ha6.pack()
       hq3_button.pack(pady=20)
       finalsubmit.pack()
       points3.pack()
    
    elif subject_pick.get()=="english":
       english_instructions.pack()
       english_q1.pack(pady=20)
       ea1.pack()
       ea2.pack()
       eq1_button.pack(pady=20)
       english_q2.pack(pady=20)
       ea3.pack()
       ea4.pack()
       eq2_button.pack(pady=20)
       english_q3.pack(pady=20)
       ea5.pack()
       ea6.pack()
       eq3_button.pack(pady=20)
       finalsubmit.pack()
       points4.pack()
    subject_pick.set(" ")


def display_points():
        global math_points
        global chem_points
        global history_points
        global english_points

        if math_questions1.get() == "correct":
            math_points += 10
        elif math_questions2.get() == "yes":
            math_points += 10
        elif math_questions3.get() == "right":
            math_points += 10
        if chem_questions1.get() == "yes":
            chem_points += 10
        elif chem_questions2.get() == "yes":
            chem_points += 10
        elif chem_questions3.get() == "yes":
            chem_points += 10
        if history_questions1.get() == "yes":
            history_points += 10
        elif history_questions2.get() == "yes":
            history_points += 10
        elif history_questions3.get() == "yes":
            history_points += 10
        if english_questions1.get() == "yes":
            english_points += 10
        elif english_questions2.get() == "yes":
            english_points += 10
        elif english_questions3.get() == "yes":
            english_points += 10
    
def final_submit():
     points.config(text="Your final math points are "+ str(math_points))  

#create window
window = tkinter.Tk()
window.title("Quiz app")
window.geometry("400x600")


welcome_label = tkinter.Label(window, text="Welcome!")
welcome_label.pack()



subject_pick = tkinter.StringVar(value=" ")
question = tkinter.Label(window, text="What subject ould you like to test")
learn_math=tkinter.Radiobutton(window, text="Math",value="math", variable=subject_pick)
learn_chem=tkinter.Radiobutton(window, text="Chem", value="chem", variable=subject_pick)
learn_history=tkinter.Radiobutton(window, text="History", value="history", variable=subject_pick)
learn_english=tkinter.Radiobutton(window, text="English", value="english",variable=subject_pick)
learn_math.pack()
learn_chem.pack()
learn_history.pack()
learn_english.pack()

learn_button = tkinter.Button(window, text="Submit Subject", command=display_subject)
learn_button.pack(pady=20)



math_questions1 = tkinter.StringVar(value=" ")
math_questions2 = tkinter.StringVar(value=" ")
math_questions3 = tkinter.StringVar(value=" ")

math_instructions=tkinter.Label(window, text="Anwser each question you get 10 points for each question you get correct")
math_q1=tkinter.Label(window, text="Simplify completely i(7−i)")
ma1=tkinter.Radiobutton(window, text="7i−i2", value="wrong", variable=math_questions1)
ma2=tkinter.Radiobutton(window, text="1+7i", value="correct", variable=math_questions1)
ma3=tkinter.Radiobutton(window, text="6i", value="bad", variable=math_questions1)
ma4=tkinter.Radiobutton(window, text="−1+7i", value="no", variable=math_questions1)

mq1_button = tkinter.Button(window, text="Submit Anwser", command=display_points)

math_q2=tkinter.Label(window, text="Solve the quadratic x2+10x=−25")
ma5=tkinter.Radiobutton(window, text="-10", value="no", variable=math_questions2)
ma6=tkinter.Radiobutton(window, text="10", value="wrong", variable=math_questions2)
ma7=tkinter.Radiobutton(window, text="5", value="bad", variable=math_questions2)
ma8=tkinter.Radiobutton(window, text="-5", value="yes", variable=math_questions2)

mq2_button = tkinter.Button(window, text="Submit Anwser", command=display_points)

math_q3=tkinter.Label(window, text="Evaluate f(x)=−a3+6a−7 at a = – 1 and state the remainder")
ma9=tkinter.Radiobutton(window, text="-14", value="no", variable=math_questions3)
ma10=tkinter.Radiobutton(window, text="-12", value="right", variable=math_questions3)
ma11=tkinter.Radiobutton(window, text="14", value="wrong it", variable=math_questions3)
ma12=tkinter.Radiobutton(window, text="12", value="bad", variable=math_questions3)

mq3_button = tkinter.Button(window, text="Submit Anwser", command=display_points)

finalsubmit=tkinter.Button(window, text="Final Submit", command=final_submit)
points = tkinter.Label(window)








chem_questions1 = tkinter.StringVar(value=" ")
chem_questions2 = tkinter.StringVar(value=" ")
chem_questions3 = tkinter.StringVar(value=" ")

chem_instructions=tkinter.Label(window, text="Anwser each question you get 10 points for each question you get correct")
chem_q1=tkinter.Label(window, text="Ionic bonds are formed when oppositely charged molecules are attracted to one another.")
ca1=tkinter.Radiobutton(window, text="True", value="yes", variable=chem_questions1)
ca2=tkinter.Radiobutton(window, text="False", value="no", variable=math_questions1)

cq1_button = tkinter.Button(window, text="Submit Anwser", command=display_points)

chem_q2=tkinter.Label(window, text="Solve the quadratic x2+10x=−25")
ca3=tkinter.Radiobutton(window, text="True", value="no", variable=chem_questions2)
ca4=tkinter.Radiobutton(window, text="False", value="yes", variable=chem_questions2)

cq2_button = tkinter.Button(window, text="Submit Anwser", command=display_points)

chem_q3=tkinter.Label(window, text="Evaluate f(x)=−a3+6a−7 at a = – 1 and state the remainder")
ca5=tkinter.Radiobutton(window, text="True", value="yes", variable=chem_questions3)
ca6=tkinter.Radiobutton(window, text="False", value="no", variable=chem_questions3)

cq3_button = tkinter.Button(window, text="Submit Anwser", command=display_points)

finalsubmit=tkinter.Button(window, text="Final Submit", command=final_submit)
points2 = tkinter.Label(window)









history_questions1 = tkinter.StringVar(value=" ")
history_questions2 = tkinter.StringVar(value=" ")
history_questions3 = tkinter.StringVar(value=" ")

history_instructions=tkinter.Label(window, text="Anwser each question you get 10 points for each question you get correct")
history_q1=tkinter.Label(window, text="How many colonies were there in the United States?")
ha1=tkinter.Radiobutton(window, text="12", value="no", variable=history_questions1)
ha2=tkinter.Radiobutton(window, text="13", value="yes", variable=history_questions1)

hq1_button = tkinter.Button(window, text="Submit Anwser", command=display_points)

history_q2=tkinter.Label(window, text="During what period did the title of Dictator originate.")
ha3=tkinter.Radiobutton(window, text="Napoleonic Europe", value="no", variable=history_questions2)
ha4=tkinter.Radiobutton(window, text="Roman Republic", value="yes", variable=history_questions2)

hq2_button = tkinter.Button(window, text="Submit Anwser", command=display_points)

history_q3=tkinter.Label(window, text="The Louisiana Purchase took place in what year?")
ha5=tkinter.Radiobutton(window, text="1803", value="yes", variable=history_questions3)
ha6=tkinter.Radiobutton(window, text="1801", value="no", variable=history_questions3)

hq3_button = tkinter.Button(window, text="Submit Anwser", command=display_points)

finalsubmit=tkinter.Button(window, text="Final Submit", command=final_submit)
points3 = tkinter.Label(window)









english_questions1 = tkinter.StringVar(value=" ")
english_questions2 = tkinter.StringVar(value=" ")
english_questions3 = tkinter.StringVar(value=" ")

english_instructions=tkinter.Label(window, text="Anwser each question you get 10 points for each question you get correct")
english_q1=tkinter.Label(window, text="They didn't reach an agreement ______ their differences.")
ea1=tkinter.Radiobutton(window, text="On account of", value="yes", variable=english_questions1)
ea2=tkinter.Radiobutton(window, text="due", value="no", variable=english_questions1)

eq1_button = tkinter.Button(window, text="Submit Anwser", command=display_points)

english_q2=tkinter.Label(window, text="I wish I _____ those words. But now it's too late.")
ea3=tkinter.Radiobutton(window, text="had never said", value="yes", variable=english_questions2)
ea4=tkinter.Radiobutton(window, text="never said", value="no", variable=english_questions2)

eq2_button = tkinter.Button(window, text="Submit Anwser", command=display_points)

english_q3=tkinter.Label(window, text="The woman, who has been missing for 10 days, is believed _____.")
ea5=tkinter.Radiobutton(window, text="to have been abducted", value="yes", variable=english_questions3)
ea6=tkinter.Radiobutton(window, text="to be abducted", value="no", variable=english_questions3)

eq3_button = tkinter.Button(window, text="Submit Anwser", command=display_points)

finalsubmit=tkinter.Button(window, text="Final Submit", command=final_submit)
points4 = tkinter.Label(window)




tkinter.mainloop()