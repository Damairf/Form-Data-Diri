from tkinter import *
from tkinter import messagebox

def submit():
    if messagebox.askyesno(title="KONFIRMASI", message="Apakah data diri anda sudah benar?"):
        window.destroy()
        window_new = Tk()
        window_new.title("Data Diri")
        window_width_new = 520
        window_height_new = 470
        screen_width_new = window_new.winfo_screenwidth()
        screen_height_new = window_new.winfo_screenheight()
        x = int((screen_width_new / 2) - (window_width_new / 2))
        y = int((screen_height_new / 2) - (window_height_new / 2))
        window_new.geometry("{}x{}+{}+{}".format(window_width_new, window_height_new, x, y))
        window_new.config(background="#22415c")
        
        title = Label(window_new, font=("Arial", 20), text="DATA DIRI", fg="White", bg="#22415c", anchor=CENTER)
        title.grid(row=0, column=0, columnspan=4, pady=10, sticky=N+S+E+W)

        nama = Label(window_new, font=("Arial", 15), text="Nama ", fg="White", bg="#22415c").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        nama_input = Label(window_new, font=("Arial", 15), text=(": "+str(input_nama_var.get())).upper(), fg="White", bg="#22415c").grid(row=1, column=3, sticky=W)

        window_new.grid_columnconfigure(0, weight=1)
        window_new.grid_columnconfigure(1, weight=1)
        window_new.grid_columnconfigure(2, weight=1)
        window_new.grid_columnconfigure(3, weight=1)

        ttl = Label(window_new, font=("Arial", 15), text="Tempat Tgl Lahir ", fg="White", bg="#22415c").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        ttl_input = Label(window_new, font=("Arial", 15), text=(": "+str(input_ttl_var.get())).upper(), fg="White", bg="#22415c").grid(row=2, column=3, sticky=W)

        alamat = Label(window_new, font=("Arial", 15), text="Alamat ", fg="White", bg="#22415c").grid(row=3, column=0, padx=10, pady=10, sticky=W)
        alamat_input = Label(window_new, font=("Arial", 15), text=(": "+str(input_alamat_var.get())).upper(), fg="White", bg="#22415c").grid(row=3, column=3, sticky=W)

        pekerjaan = Label(window_new, font=("Arial", 15), text="Pekerjaan ", fg="White", bg="#22415c").grid(row=4, column=0, padx=10, pady=10, sticky=W)
        pekerjaan_input = Label(window_new, font=("Arial", 15), text=(": "+str(input_pekerjaan_var.get())).upper(), fg="White", bg="#22415c").grid(row=4, column=3, sticky=W)
        
        perkawinan = Label(window_new, font=("Arial", 15), text="Status Perkawinan ", fg="White", bg="#22415c").grid(row=5, column=0, padx=10, pady=10, sticky=W)
        perkawinan_input = Label(window_new, font=("Arial", 15), text=(": "+str(input_perkawinan_var.get())).upper(), fg="White", bg="#22415c").grid(row=5, column=3, sticky=W)

        kelamin = Label(window_new, font=("Arial", 15), text="Jenis Kelamin ", fg="White", bg="#22415c").grid(row=6, column=0, padx=10, pady=10, sticky=W)
        kelamin_input = Label(window_new, font=("Arial", 15), text=(": "+str(input_kelamin_var.get())).upper(), fg="White", bg="#22415c").grid(row=6, column=3, sticky=W)

        telp = Label(window_new, font=("Arial", 15), text="Telepon ", fg="White", bg="#22415c").grid(row=7, column=0, padx=10, pady=10, sticky=W)
        telp_input = Label(window_new, font=("Arial", 15), text=(": "+str(input_telp_var.get())).upper(), fg="White", bg="#22415c").grid(row=7, column=3, sticky=W)

        email = Label(window_new, font=("Arial", 15), text="Email ", fg="White", bg="#22415c").grid(row=8, column=0, padx=10, pady=10, sticky=W)
        email_input = Label(window_new, font=("Arial", 15), text=(": "+str(input_email_var.get())).upper(), fg="White", bg="#22415c").grid(row=8, column=3, sticky=W)

window = Tk()
window.title("Form Data Diri")

icon = PhotoImage(file='Gambar\\orang.png')
window.iconphoto(True, icon)

window_width = 600
window_height = 520
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
window.config(background="#22415c")
window.resizable(False, False)


judul = Label(window, font=("Arial", 20), text="Formulir Data Diri", fg="White", bg="#22415c").grid(row=0, column=0, columnspan=4, pady=10)
nama = Label(window, font=("Arial", 15), text="Masukkan Nama: ", fg="White", bg="#22415c").grid(row=1, column=0, sticky=W, padx=10, pady=10)
input_nama_var = StringVar()
input_nama = Entry(window, width=25, font=("Arial", 15), textvariable=input_nama_var, validate="key", validatecommand=(window.register(lambda P: len(P) <= 25), '%P'))
input_nama.grid(row=1, column=3, sticky=E+W)

ttl = Label(window, font=("Arial", 15), text="Masukkan Tempat Tgl Lahir: ", fg="White", bg="#22415c").grid(row=2, column=0, sticky=W, padx=10, pady=10)
input_ttl_var = StringVar()
input_ttl = Entry(window, width=25, font=("Arial", 15), textvariable=input_ttl_var, validatecommand=(window.register(lambda P: len(P) <= 25), '%P'))
input_ttl.grid(row=2, column=3, sticky=E+W)

alamat = Label(window, font=("Arial", 15), text="Masukkan Alamat: ", fg="White", bg="#22415c").grid(row=3, column=0, sticky=W, padx=10, pady=10)
input_alamat_var = StringVar()
input_alamat = Entry(window, width=25, font=("Arial", 15), textvariable=input_alamat_var, validatecommand=(window.register(lambda P: len(P) <= 25), '%P'))
input_alamat.grid(row=3, column=3, sticky=E+W)

pekerjaan = Label(window, font=("Arial", 15), text="Masukkan Pekerjaan: ", fg="White", bg="#22415c").grid(row=4, column=0, sticky=W, padx=10, pady=10)
input_pekerjaan_var = StringVar()
input_pekerjaan = Entry(window, width=25, font=("Arial", 15), textvariable=input_pekerjaan_var, validatecommand=(window.register(lambda P: len(P) <= 25), '%P'))
input_pekerjaan.grid(row=4, column=3, sticky=E+W)

perkawinan = Label(window, font=("Arial", 15), text="Masukkan Status Perkawinan: ", fg="White", bg="#22415c").grid(row=5, column=0, sticky=W, padx=10, pady=10)
input_perkawinan_var = StringVar()
input_perkawinan = Entry(window, width=25, font=("Arial", 15), textvariable=input_perkawinan_var, validatecommand=(window.register(lambda P: len(P) <= 25), '%P'))
input_perkawinan.grid(row=5, column=3, sticky=E+W)

kelamin = Label(window, font=("Arial", 15), text="Masukkan Jenis Kelamin: ", fg="White", bg="#22415c").grid(row=6, column=0, sticky=W, padx=10, pady=10)
input_kelamin_var = StringVar()
input_kelamin = Entry(window, width=25, font=("Arial", 15), textvariable=input_kelamin_var, validatecommand=(window.register(lambda P: len(P) <= 25), '%P'))
input_kelamin.grid(row=6, column=3, sticky=E+W)

telp = Label(window, font=("Arial", 15), text="Masukkan Telepon: ", fg="White", bg="#22415c").grid(row=7, column=0, sticky=W, padx=10, pady=10)
input_telp_var = StringVar()
input_telp = Entry(window, width=25, font=("Arial", 15), textvariable=input_telp_var, validatecommand=(window.register(lambda P: len(P) <= 25), '%P'))
input_telp.grid(row=7, column=3, sticky=E+W)

email = Label(window, font=("Arial", 15), text="Masukkan Email: ", fg="White", bg="#22415c").grid(row=8, column=0, sticky=W, padx=10, pady=10)
input_email_var = StringVar()
input_email = Entry(window, width=25, font=("Arial", 15), textvariable=input_email_var, validatecommand=(window.register(lambda P: len(P) <= 25), '%P'))
input_email.grid(row=8, column=3, sticky=E+W)

submit_btn = Button(window, font=("Arial", 18), text="SUBMIT", bg="White", command=submit, fg="#22415c", activeforeground="#1b344a").grid(row=9, column=0, columnspan=4, pady=10)

window.mainloop()