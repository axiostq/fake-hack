import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def show_notification():
    for _ in range(20):  
        root = tk.Tk()
        root.title("Warning!")

        root.geometry("800x800")  

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (400 // 2)
        y = (screen_height // 2) - (400 // 2)
        root.geometry(f"400x400+{x}+{y}")

        root.configure(bg='black')

        url = "https://cdn.readawrite.com/articles/4781/4780078/thumbnail/large.gif?1"
        response = requests.get(url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((200, 200), Image.LANCZOS)  
        img_tk = ImageTk.PhotoImage(img)

        label_img = tk.Label(root, image=img_tk, bg='black')
        label_img.image = img_tk  
        label_img.pack(pady=10)  

        label = tk.Label(root, text="⚠️I'm Hacker⚠️", font=("Helvetica", 30, "bold"), fg='red', bg='black')  
        label.pack(expand=True)  

        root.after(800, root.destroy)
        root.mainloop()

show_notification()
