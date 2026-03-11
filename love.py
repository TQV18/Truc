import tkinter as tk
from PIL import Image, ImageTk
import winsound
import os
import sys

# Hàm lấy đường dẫn tài nguyên khi chạy .exe
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

app = tk.Tk()

frames_top = []
frames_bottom=[]
frames_left=[]
frames_right=[]

top_gif = Image.open(resource_path("top.gif"))
bottom_gif= Image.open(resource_path("bottom.gif"))
left_gif = Image.open(resource_path("left.gif"))
right_gif = Image.open(resource_path("right.gif"))
while True:
    try:
        frames_top.append(ImageTk.PhotoImage(top_gif.copy()))
        top_gif.seek(len(frames_top))

        frames_bottom.append(ImageTk.PhotoImage(bottom_gif.copy()))
        bottom_gif.seek(len(frames_top))

        frames_left.append(ImageTk.PhotoImage(left_gif.copy()))
        left_gif.seek(len(frames_left))

        frames_right.append(ImageTk.PhotoImage(right_gif.copy()))
        right_gif.seek(len(frames_right))
    except EOFError:
        break

label_top = tk.Label(app)
label_top.place(x=480, y=5)

label_bottom = tk.Label(app)
label_bottom.place(x=440,y=400)

label_left = tk.Label(app)
label_left.place(x=50,y=300)

label_right = tk.Label(app)
label_right.place(x=900,y=200)

frame_top_index = 0
frame_bottom_index = 0
frame_left_index = 0 
frame_right_index = 0
def update_gif():
    global frame_bottom_index, frame_top_index, frame_left_index, frame_right_index
    frame_top_index = (frame_top_index + 1) % len(frames_top)
    label_top.config(image=frames_top[frame_top_index])

    frame_bottom_index = (frame_bottom_index+1 )%len(frames_bottom)
    label_bottom.config(image = frames_bottom[frame_bottom_index])

    frame_left_index = (frame_left_index+1)%len(frames_left)
    label_left.config(image=frames_left[frame_bottom_index])

    frame_right_index = (frame_right_index+1)%len(frames_right)
    label_right.config(image= frames_right[frame_right_index])

    app.after(150, update_gif)

update_gif()

def play_sound_main():
    winsound.PlaySound(resource_path("love_u.wav"), winsound.SND_FILENAME | winsound.SND_ASYNC)

play_sound_main()

def show_text():
    if show_text.index<len(full_text):
        text_label.config(text=full_text[:show_text.index+1])
        show_text.index+=1
        app.after(50,show_text)

app.after(100,show_text)
show_text.index = 0
full_text="I love uuuu so muchh >.<"

text_label = tk.Label(app,text="", font=('Super Story',20))
text_label.place(x=440,y=330,width=400,height=50)

app.after(3000,app.destroy)

app.resizable(False, False)
app.title("love uuu^^")
app.iconbitmap(resource_path("heart.ico"))
app.geometry("1200x700")
app.mainloop()
