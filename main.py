import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

RED = "#e7305b"
PINK = "#e2979c"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
 
def reset_timer():

    global reps
    reps=0

    label2.config(text="")
    window.after_cancel(timer)
    label1.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
    
def startTimer():

    global reps
    reps+=1

    if reps%8==0:
        countDown(LONG_BREAK_MIN*60)
        label1.config(text="Break",fg=RED)

    elif reps%2==0:
        countDown(SHORT_BREAK_MIN*60)
        label1.config(text="Break",fg=PINK)

    else:
        countDown(WORK_MIN*60)
        label1.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
         
def countDown(count):

    min=math.floor(count/60)
    sec=count%60

    if sec<10:
        sec=f"0{sec}"

    canvas.itemconfig(timer_text,text=f"{min}:{sec}")

    if(count>0):
        global timer
        timer=window.after(1000,countDown,count-1)

    else:

        startTimer()

        mark=""
        work_session=math.floor(reps/2)

        for i in range(work_session):
            mark+="✔"
        label2.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
        
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW,highlightthickness=0)

label1=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
label1.grid(row=0,column=1)

canvas=Canvas(width=200,height=224,bg=YELLOW)
pomodoro_img=PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=pomodoro_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

button1=Button(text="Start",fg="black",highlightthickness=0,command=startTimer)
button1.grid(row=2,column=0)

label2=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
label2.grid(row=3,column=1)

button2=Button(text="Reset",fg="black",highlightthickness=0,command=reset_timer)
button2.grid(row=2,column=2)

window.mainloop()
