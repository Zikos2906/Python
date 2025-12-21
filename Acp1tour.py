import tkinter as tk

def get_weather():
    city = entry.get()
    label_res.config(text=f"The weather in {city} is Sunny!")

root = tk.Tk()
root.title("World Weather Teller")

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Get Weather", command=get_weather)
btn.pack()

label_res = tk.Label(root, text="")
label_res.pack()

root.mainloop()