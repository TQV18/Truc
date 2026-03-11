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

root = tk.Tk()
root.title("Animated GIF in Tkinter")

frames = []
frames_panda2 = []
frames_cat2 = []
frames_wishing=[]
frames_cute =[]

gif_panda = Image.open(resource_path("panda.gif"))
gif_panda2 = Image.open(resource_path("panda2.gif"))
gif_cat2 = Image.open(resource_path("cat2.gif"))
gif_wishing  = Image.open(resource_path("happy.gif"))
gif_cute = Image.open(resource_path("cute.gif"))

while True:
    try:
        frames.append(ImageTk.PhotoImage(gif_panda.copy()))
        gif_panda.seek(len(frames))

        frames_panda2.append(ImageTk.PhotoImage(gif_panda2.copy()))
        gif_panda2.seek(len(frames_panda2))

        frames_cat2.append(ImageTk.PhotoImage(gif_cat2.copy()))
        gif_cat2.seek(len(frames_cat2))

        frames_wishing.append(ImageTk.PhotoImage(gif_wishing.copy()))
        gif_wishing.seek(len(frames_wishing))

        frames_cute.append(ImageTk.PhotoImage(gif_cute.copy()))
        gif_cute.seek(len(frames_cute))
        
    except EOFError:
        break

label_panda = tk.Label(root)
label_panda.place(x=1005, y=400)

label_panda2 = tk.Label(root)
label_panda2.place(x=1005,y=100)

label_cat2= tk.Label(root)
label_cat2.place(x=100,y=400)


label_wishing = tk.Label(root)
label_wishing.place(x=410,y=200)

label_cute = tk.Label(root)
label_cute.place(x=100,y=70)

frame_index = 0
frame_index_panda2 = 0
frame_index_cat2 = 0
frame_index_wishing=0
frame_index_cute = 0

def update_gif():
    global frame_index,frame_index_panda2,frame_index_cat2,frame_index_wishing,frame_index_cute
    
    frame_index = (frame_index + 1) % len(frames)
    label_panda.config(image=frames[frame_index])

    frame_index_panda2 = (frame_index_panda2 +1)%len(frames_panda2)
    label_panda2.config(image = frames_panda2[frame_index_panda2])

    frame_index_cat2 = (frame_index_cat2+1) %len(frames_cat2)
    label_cat2.config(image=frames_cat2[frame_index_cat2] )

    frame_index_wishing = (frame_index_wishing+1)%len(frames_wishing)
    label_wishing.config(image=frames_wishing[frame_index_wishing])

    frame_index_cute = (frame_index_cute+1)%len(frames_cute)
    label_cute.config(image=frames_cute[frame_index_cute])

    root.after(150, update_gif)

update_gif()

def show_text():
    if show_text.index < len(full_text):
        text_label.config(text=full_text[:show_text.index+1])
        show_text.index += 1
        root.after(50, show_text)

root.after(50, show_text)
show_text.index = 0
full_text = "Happy birthday Truc Phan^^"

text_label = tk.Label(root, text="", font=('Super Story', 20))
text_label.place(x=475, y=100, width=400, height=50)

def play_sound_main():
    winsound.PlaySound(resource_path("main.wav"), winsound.SND_FILENAME | winsound.SND_ASYNC)

def out():
    root.destroy()
    os.system(resource_path("love.exe"))

play_sound_main()
root.after(28500, out)

root.title("Truc Phan's birthday")
root.resizable(False, False)
root.geometry("1300x680")
root.iconbitmap(resource_path("cake.ico"))
root.mainloop()
