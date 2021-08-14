from tkinter import *
import time
import pyautogui
import pyperclip

root = Tk()

root.geometry("600x750")

root.resizable(0, 0)

root.title("Spammer")

root.configure(bg='#2e2e2e',cursor="dot")

def starting():
    num = x.get()
    try:
        int(num)
    except ValueError:
        Label(root, text="Enter a valid number!", bg='#2e2e2e', fg="white").pack()
        return

    timer_font = ("Consolas", 26, "normal")
    start_font = ("Consolas", 16, "normal")
    timer = Label(root, text="Start", font=timer_font, bg='#2e2e2e', fg="white")
    timer.pack(pady = 30)

    Label(root, text="If you need to stop, close this window!", font=start_font, bg='#2e2e2e', fg="white").pack()

    time.sleep(3)
    spam()
    
def spam():
    count = 0
    text = txt.get("1.0", END)
    num = int(x.get())
    pyperclip.copy(text)
    for count in range(0, num):
        pyautogui.hotkey("ctrl", "v")



if __name__ == "__main__":

    font_title = ("Calibri", 40, "normal")
    font = ("Consolas", 12, "normal")

    Label(root, text="Spam Bot", font=font_title, bg='#2e2e2e', fg="white").pack()

    Label(root, text="Type the text do you want to spam", fg="white",bg='#2e2e2e').pack(pady = 20)

    global txt
    txt = Text(root, bg='#0f0f0f', fg="white", font=font, width=100, height=10,insertbackground="white")
    txt.pack(padx = 10)

    Label(root, text="number of times :", fg="white",bg='#2e2e2e').pack()
    global x
    x = Entry(root, fg="white", font=font,bg='#0f0f0f',insertbackground="white")
    x.pack()

    Label(root, fg="white",bg='#2e2e2e').pack()

    aviso = "When you click on the button you have 3s to place the cursor where you want to spam..."

    Label(root, text=aviso, fg="white",bg='#2e2e2e').pack(pady=5)

    Button(root, text="Start",width=50, bg='#2e2e2e', fg="white",command=starting).pack()

    root.mainloop()