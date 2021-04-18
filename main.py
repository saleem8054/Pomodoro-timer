from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
i = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global i
    global reps
    i = 1
    reps = 0
    check_symbol_label.config(text="")
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    
    window.after_cancel(timer)
    #canvas.itemconfig(timer_text,text=f"00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN *60
    
    if reps % 8 == 0:
        count_down(long_break)
        title_label.config(text="Long Break",fg=RED)
    elif reps % 2 == 0 :
        count_down(short_break)
        title_label.config(text="Short Break",fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work Time",fg=GREEN)        
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_min == 0:
        count_min = "00"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        global i
        if reps % 8 == 0:
            check_symbol_label.config(text="")
            i = 1
        if reps % 2 !=0:
            check_symbol = i * "✔"
            check_symbol_label.config(text=check_symbol)
            i += 1
        start_timer()
    
        #check_symbol = reps * "✔"
            

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


title_label = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
title_label.grid(row=0,column=1)

canvas = Canvas(width=205,height=230,bg=YELLOW,highlightthickness=0)
tomate_image = PhotoImage(file="tomato.png")
canvas.create_image(102,115,image=tomate_image)
timer_text = canvas.create_text(101,140,text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)



start_button = Button(text="Start", highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)


check_symbol_label = Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,20,"italic"))
check_symbol_label.grid(row=3,column=1)

reset_button = Button(text="Reset",highlightthickness=0,command=reset)
reset_button.grid(row=2,column=2)




window.mainloop()