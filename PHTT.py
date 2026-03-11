import tkinter 
from tkinter import ttk
from PIL import ImageTk, Image
import os
import sys

# Hàm lấy đường dẫn tài nguyên khi chạy .exe
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

app = tkinter.Tk()

bg = Image.open(resource_path("1200x600.png"))
photo_bg = ImageTk.PhotoImage(bg)

log = True

def main():
    # Background
    label_bg = tkinter.Label(app, image=photo_bg)
    label_bg.place(relwidth=1, relheight=1)

    # Title
    label_title = tkinter.Label(app, text='Panda Login', font=('Super Story', 30), bg='white', fg='#CB3467')
    label_title.place(x=475, y=200)

    # Username
    label_username = tkinter.Label(app, text='username', font=('Super Story', 15), bg='white', fg='#CB3467')
    label_username.place(x=400, y=300)
    entry_username = tkinter.Entry(app, width=45)
    entry_username.place(height=20, x=500, y=305)

    # Password
    label_password = tkinter.Label(app, text='password', font=('Super Story', 15), fg='#CB3467', bg='white')
    label_password.place(x=400, y=360)
    entry_password = tkinter.Entry(app, width=45, show='*')
    entry_password.place(height=20, x=500, y=365)

    def reload():
        panda = Image.open(resource_path("re.png")).resize((600, 300))
        photo_panda = ImageTk.PhotoImage(panda)
        
        label = tkinter.Label(app, bg='white')
        label.place(width=1200, height=600, x=0, y=0)


        # Create a background label
        label = tkinter.Label(app, bg='white')
        label.place(width=1200, height=600, x=0, y=0)

        # Create a loading frame
        loading_frame = tkinter.Frame(app, bg='black')
        loading_frame.place(width=1000, height=50, x=100, y=500)

        # Create a loading bar inside the frame
        loading = tkinter.Label(loading_frame, bg='white')
        loading.place(width=980, height=40, x=10,y=5)  # Adjusted position within frame

        # Create an image label and reference the image
        circle = tkinter.Label(app, image=photo_panda, bg="white")
        circle.image = photo_panda  # Keep a reference to prevent garbage collection
        circle.place(height=300, width=600, x=300, y=100)

        # Loading animation
        loading_box = tkinter.Label(app, bg='light green')
        loading_box.place(height=40, width=49, x=110, y=505)

        loading_box_x = 110
        speed = 10

        def out():
            app.destroy()
            os.system(resource_path("test2.exe"))

        def animate():
            nonlocal loading_box_x, speed
            loading_box_x += speed
            if loading_box_x >= 1041:
                speed = 0
                app.after(1000, out)
            loading_box.place(x=loading_box_x, y=505)
            app.after(10, animate)

        app.after(10, animate)

    def done():
        complete_label = tkinter.Label(app, text='Successful', font=('Super Story', 23), fg='white', bg='#CB3467')
        complete_label.place(x=515, y=440, width=170)
        app.after(1000, reload)

    def fail():
        fail_label = tkinter.Label(app, text='Failed', font=('Super Story', 23), fg='white', bg='#CB3467')
        fail_label.place(x=515, y=440, width=170)
        entry_username.delete(0, tkinter.END)
        entry_password.delete(0, tkinter.END)
        app.after(1000, fail_label.destroy)

    def data():
        username_data = entry_username.get()
        password_data = entry_password.get()
        if username_data == 'PHTT' and password_data == '1404':
            done()
        else:
            fail()

    button = tkinter.Button(app, text='Submit', font=('Super Story', 23), fg='white', bg='#CB3467', command=data)
    button.place(x=515, y=440, width=170)

if log:
    main()

app.resizable(False, False)
app.title("Truc Phan's birthday")
app.geometry('1200x600')
app.iconbitmap(resource_path("cake.ico"))
app.mainloop()
