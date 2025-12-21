import tkinter as tk

def start_record():
    status.config(text="Recording...", fg="red")

def stop_record():
    status.config(text="Video Saved!", fg="green")

root = tk.Tk()
root.title("Reel-O-Gram")

status = tk.Label(root, text="Ready to Record")
status.pack(pady=10)

btn_start = tk.Button(root, text="Record", command=start_record)
btn_start.pack()

btn_stop = tk.Button(root, text="Stop", command=stop_record)
btn_stop.pack()

root.mainloop()