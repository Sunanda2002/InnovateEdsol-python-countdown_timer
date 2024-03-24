import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")

        self.duration_label = tk.Label(master, text="Enter duration (in seconds):")
        self.duration_label.pack()

        self.duration_entry = tk.Entry(master)
        self.duration_entry.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.timer_label = tk.Label(master, text="")
        self.timer_label.pack()

    def start_timer(self):
        try:
            duration = int(self.duration_entry.get())
            self.countdown(duration)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the duration.")

    def countdown(self, duration):
        while duration >= 0:
            mins, secs = divmod(duration, 60)
            timer_display = '{:02d}:{:02d}'.format(mins, secs)
            self.timer_label.config(text=timer_display)
            self.master.update()
            if duration == 0:
                messagebox.showinfo("Countdown Timer", "Time's up!")
            duration -= 1
            time.sleep(1)

def main():
    root = tk.Tk()
    app = CountdownTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
