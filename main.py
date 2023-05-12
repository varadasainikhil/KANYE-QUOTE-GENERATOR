from tkinter import *
import requests
def generate_quote():
    quote = requests.get("https://api.kanye.rest")
    canvas.itemconfig(text, text=quote.json()["quote"])


window = Tk()
window.title("KANYE QUOTES")
window.minsize(width=400, height=500)
window.config(pady=50,padx=50)
canvas = Canvas(width=300, height=414, highlightthickness=0)
bg = PhotoImage(file ="background.png")
background = canvas.create_image(150,212, image=bg)
text = canvas.create_text(150,212,font=("Courier", 15, "bold"), width=290)

kanye_image = PhotoImage(file="kanye.png")
button = Button(highlightthickness=0, image=kanye_image, command=generate_quote)
button.grid(row=1, column=0)
canvas.grid(row=0,column=0)
generate_quote()
window.mainloop()