import tkinter
import random

# list of possible colours.
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']

score = 0
timeleft = 120   # đổi từ 30s → 120s

# function that will start the game.
def startGame(event):
    global timeleft
    if timeleft == 120:
        countdown()
        nextColour()

# Function to choose and display the next colour.
def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()

        # kiểm tra, nếu người dùng nhập đúng màu
        if e.get().lower() == colours[1].lower():
            score += 2         # đúng được +2
        elif e.get() != "":
            score -= 1         # sai bị -1

        e.delete(0, tkinter.END)

        random.shuffle(colours)

        label.config(fg=str(colours[1]), text=str(colours[0]))

        scoreLabel.config(text="Score: " + str(score))

# Countdown timer function
def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)

# Driver Code
root = tkinter.Tk()

root.title("COLORGAME")
root.geometry("420x230")

instructions = tkinter.Label(root,
    text="Type the **COLOR** of the word, not the text!",
    font=('Helvetica', 12)
)
instructions.pack()

scoreLabel = tkinter.Label(root, text="Press Enter to start",
                           font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft),
                          font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

root.mainloop()
