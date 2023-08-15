# Dynamic Typing: you can dynamically change the data type by assigning new value

from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def runtimer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_logo.config(text = "Break", fg = RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_logo.config(text = "Break", fg = PINK)
    else:
        count_down(work_sec)
        timer_logo.config(text = "Work", fg = GREEN)
    

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_logo.config(text = "Timer", fg = GREEN)
    checkmark.config(text="")
    global reps
    reps = 0

def count_down(count):

    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"
    
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        runtimer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        checkmark.config(text=mark)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_logo = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_logo.grid(column=1, row=0)

# highlightthickness to remove the border
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"28_pomodoro\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=runtimer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)

checkmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
checkmark.grid(column=1, row=3)

window.mainloop()
