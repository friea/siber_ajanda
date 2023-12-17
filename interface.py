from tkinter import *
import btk_mining
import bga_mining
import bilgeis_mining
import ttkbootstrap as ttk
import makale_al

# Fonksiyonlar
def btk_data_al():
    text.config(state="normal")
    j=0
    text.delete(1.0,END)
    btk_ders=btk_mining.btk_siber_dersler()
    for i in btk_ders:
        j=j+1
        text.insert(INSERT, str(j)+"."+i+"\n")
    text.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
    text.config(state="disabled")
def bga_data_al():
    text.config(state="normal")
    j=0
    text.delete(1.0,END)
    bga_ders=bga_mining.bga_makaleler()
    for i in bga_ders:
        j=j+1
        text.insert(INSERT, str(j)+"."+i+"\n")
    text.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
    text.config(state="disabled")
def bilgeis_data_al():
    text.config(state="normal")
    j=0
    text.delete(1.0,END)
    bilgeis_ders=bilgeis_mining.bilgeIs_siber_dersler()
    for i in bilgeis_ders:
        j=j+1
        text.insert(INSERT, str(j)+"."+i+"\n")
    text.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
    text.config(state="disabled")
def forensic_data_al():
    text.config(state="normal")
    j=0
    text.delete(1.0,END)
    forensic_ders=makale_al.makale_al("digital forensic")
    for i in forensic_ders:
        j=j+1
        text.insert(INSERT, str(j)+"."+i+"\n")
    text.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
    text.config(state="disabled")
def web_data_al():
    text.config(state="normal")
    j=0
    text.delete(1.0,END)
    web_ders=makale_al.makale_al("web security")
    for i in web_ders:
        j=j+1
        text.insert(INSERT, str(j)+"."+i+"\n")
    text.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
    text.config(state="disabled")
def network_data_al():
    text.config(state="normal")
    j=0
    text.delete(1.0,END)
    web_ders=makale_al.makale_al("network security")
    for i in web_ders:
        j=j+1
        text.insert(INSERT, str(j)+"."+i+"\n")
    text.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
    text.config(state="disabled")
def malware_data_al():
    text.config(state="normal")
    j=0
    text.delete(1.0,END)
    web_ders=makale_al.makale_al("malware analysis")
    for i in web_ders:
        j=j+1
        text.insert(INSERT, str(j)+"."+i+"\n")
    text.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
    text.config(state="disabled")
def kripto_data_al():
    text.config(state="normal")
    j=0
    text.delete(1.0,END)
    web_ders=makale_al.makale_al("cryptology")
    for i in web_ders:
        j=j+1
        text.insert(INSERT, str(j)+"."+i+"\n")
    text.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
    text.config(state="disabled")
def privesc_data_al():
    text.config(state="normal")
    j=0
    text.delete(1.0,END)
    web_ders=makale_al.makale_al("privilege escalation")
    for i in web_ders:
        j=j+1
        text.insert(INSERT, str(j)+"."+i+"\n")
    text.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
    text.config(state="disabled")
def ml_data_al():
    text.config(state="normal")
    j=0
    text.delete(1.0,END)
    web_ders=makale_al.makale_al("machine learning security")
    for i in web_ders:
        j=j+1
        text.insert(INSERT, str(j)+"."+i+"\n")
    text.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
    text.config(state="disabled")
def cikis():
    master.destroy()

# Fontlar
Font_tuple = ("Bodoni", 16)

# Temel Grafik Birimleri Oluşturma

master = Tk()
master.title("Siber Ajanda")
master.attributes('-fullscreen', True)
master.configure(bg='black')
#master.iconbitmap("hacker.png")
canvas = Canvas(master, height = 450, width = 750)
canvas.configure(bg='black')
canvas.pack(fill=BOTH, expand=True)
frame_sol = Frame(master,bg = "#4A484A" , highlightbackground="#6973ff", highlightthickness=3)
frame_sol.place(relx = 0.05, rely = 0.05, relwidth = 0.2, relheight = 0.75)
frame_orta = Frame(master,bg = "#4A484A" , highlightbackground="#6973ff", highlightthickness=3)
frame_orta.place(relx = 0.27, rely = 0.05, relwidth = 0.7, relheight = 0.9)
frame_cikis = Frame(master,bg = "#4A484A" , highlightbackground="#6973ff", highlightthickness=3)
frame_cikis.place(relx = 0.05, rely = 0.825, relwidth = 0.2, relheight = 0.125)

#Scrollbar Özellikleri
style = ttk.Style('superhero')
scrollbar = ttk.Scrollbar(frame_orta, bootstyle='info-round')
scrollbar.pack(pady=10,side=RIGHT, fill='y')
scrollbar.set(0.1,0.9)



#Text Özellikleri
text = Text(frame_orta)
text.configure(font=Font_tuple, foreground="white",state="normal",yscrollcommand=scrollbar.set)
scrollbar.config( command = text.yview )

# Buton Tanımlamaları
forensic_buton = Button(frame_sol, text = "Forensic", command = forensic_data_al)
forensic_buton.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.08)
web_buton = Button(frame_sol, text = "Web", command = web_data_al)
web_buton.place(relx = 0.05, rely = 0.15, relwidth = 0.9, relheight = 0.08)
network_buton = Button(frame_sol, text = "Network", command = network_data_al)
network_buton.place(relx = 0.05, rely = 0.25, relwidth = 0.9, relheight = 0.08)
malware_buton = Button(frame_sol, text = "Malware Analizi", command = malware_data_al)
malware_buton.place(relx = 0.05, rely = 0.35, relwidth = 0.9, relheight = 0.08)
kripto_buton = Button(frame_sol, text = "Kriptoloji", command = kripto_data_al)
kripto_buton.place(relx = 0.05, rely = 0.45, relwidth = 0.9, relheight = 0.08)
privesc_buton = Button(frame_sol, text = "Yetki Yükseltme", command = privesc_data_al)
privesc_buton.place(relx = 0.05, rely = 0.55, relwidth = 0.9, relheight = 0.08)
ml_buton = Button(frame_sol, text = "Makina Öğrenmesi", command = ml_data_al)
ml_buton.place(relx = 0.05, rely = 0.65, relwidth = 0.9, relheight = 0.08)
btk_buton = Button(frame_sol, text = "BTK", command = btk_data_al)
btk_buton.place(relx = 0.05, rely = 0.75, relwidth = 0.9, relheight = 0.08)
bga_buton = Button(frame_sol, text = "BGA", command = bga_data_al)
bga_buton.place(relx = 0.05, rely = 0.85, relwidth = 0.9, relheight = 0.08)
bi_buton = Button(frame_sol, text = "Bilge İş", command = bilgeis_data_al)
bi_buton.place(relx = 0.05, rely = 0.95, relwidth = 0.9, relheight = 0.08)
cikis_buton = Button(frame_cikis, text = "Çıkış", command = cikis)
cikis_buton.place(relx = 0.05, rely = 0.15, relwidth = 0.9, relheight = 0.7)


master.mainloop()
