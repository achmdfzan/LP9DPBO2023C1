from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from ruko import Ruko
from tkinter import *
from PIL import ImageTk, Image

hunians = []
hunians.append(Apartemen("Fauzan", "AparTeman", "apartemen1.jpeg", "Jl. Yang Lurus", 2, 3))
hunians.append(Rumah("Anandita", 2, "rumah1.jpg", "Jl. Jalan", 2, 2))
hunians.append(Indekos("Bu Onah", "Bintang", "Indekos Putra", "indekos1.jpg", "Jl. Gegerkalong"))
hunians.append(Ruko("Alifia", 2, "ruko1.jpg", "Jl. Inaja Dulu", 5, 4, "Misue"))
hunians.append(Apartemen("Yasin", "AparTeman", "apartemen2.jpg", "Jl. Yang Lurus", 1, 4))

root = Tk()
root.title("Praktikum DPBO Python")

label = Label(root, text="Landing Page", font=('Arial', 20))
label.pack()

m_frame = Frame(root, padx=10, pady=10)
m_frame.pack(padx=10, pady=10)

photos = []

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    image = Image.open("images/" + hunians[index].get_foto())
    image = image.resize((256, 256))
    photo = ImageTk.PhotoImage(image)
    photos.append(photo)
    image_label = Label(d_frame, image=photo)
    image_label.grid(row=0, column=0)

    space = Label(d_frame, text="", width=1, borderwidth=0, relief="solid")
    space.grid(row=0, column=1)

    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=2, sticky="w")

def main_page():
    label.destroy()
    m_frame.destroy()
    image_label.destroy()
    button.destroy()

    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, height=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, height=5, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, height=5, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, height=5, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        image = Image.open("images/" + h.get_foto())
        image = image.resize((64, 64))

        photo = ImageTk.PhotoImage(image)
        photos.append(photo)

        image_labels = Label(frame, image=photo, width=77, height=77, borderwidth=1, relief="solid")
        image_labels.grid(row=index, column=3)

        space = Label(frame, text="", width=1, borderwidth=0, relief="solid")
        space.grid(row=index, column=4)

        b_detail = Button(frame, text="Details ", height=5, width=10, command=lambda index=index: details(index))
        b_detail.grid(row=index, column=5)

image = Image.open("images/icon.jpeg")
image = image.resize((512, 512))
photo = ImageTk.PhotoImage(image)
photos.append(photo)
image_label = Label(m_frame, image=photo)
image_label.pack()

button = Button(root, text='Data Seluruh Residen', font=('Arial', 15), width=25, height=1, command=main_page)
button.pack(side=BOTTOM)

root.mainloop()
