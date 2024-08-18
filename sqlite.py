import tkinter as tk #Arya Bagas
from tkinter import * #Arya Bagas
import sqlite3

# Membuat atau menghubungkan ke database SQLite
conn = sqlite3.connect('prodi.db')
c = conn.cursor()

# Membuat tabel nilai_siswa jika belum ada
c.execute('''CREATE TABLE IF NOT EXISTS prodi (
            id INTEGER PRIMARY KEY,
            geografi INTEGER,
            matematika INTEGER,
            bahasa_inggris INTEGER,
            prediksi_prodi TEXT
            )''')

#untuk menyimpan perubahan yang terjadi pada tabel
conn.commit()

# Fungsi untuk menyimpan data ke database
def simpan_ke_database(geografi, matematika, inggris, prediksi):
    #untuk execute isinya supaya INSERT ke database nilai_siswa
    c.execute("INSERT INTO prodi (geografi, matematika, bahasa_inggris, prediksi_prodi) VALUES (?, ?, ?, ?)", (geografi, matematika, inggris, prediksi))
    #1. Setiap ? adalah tempat untuk memasukkan nilai tertentu.
    #2. Dalam SQL, ini dikenal sebagai parameterized query atau prepared statement.
    #3. Tujuan dari penggunaan placeholder adalah untuk mencegah serangan SQL Injection dan untuk mempermudah penyisipan data yang bervariasi.
    
    #untuk meyimpan
    conn.commit()

jendela = tk.Tk() #Husna Kamila    
jendela.title("Aplikasi Prodi Pilihan") #Husna Kamila
jendela.configure(bg='#729c9b') #Gibran Fathoni
jendela.geometry("400x400")

matematika = tk.DoubleVar() #Gibran Fathoni
inggris = tk.DoubleVar() #Gibran Fathoni
geografi = tk.DoubleVar() #Gibran Fathoni

# (FIX) : convert string to integer before comparing ##habib
def prediksi() :
    
    if int(geografi.get()) < 75 or int(inggris.get()) < 75 or int(matematika.get()) < 75 :
        prediksi_prodi = "Tidak Lulus"
    elif int(matematika.get()) > int(geografi.get()) and int(matematika.get()) > int(inggris.get()) :
        prediksi_prodi = "Kedokteran"
    elif int(geografi.get()) > int(matematika.get()) and int(geografi.get()) > int(inggris.get()) :
        prediksi_prodi = "Teknik"
    elif int(inggris.get()) > int(geografi.get()) and int(inggris.get()) > int(matematika.get()) :
        prediksi_prodi = "Bahasa"
    
    hasil_label.config(text=f"Prediksi Prodi: {prediksi_prodi}")
    
    simpan_ke_database(int(geografi.get()), int(matematika.get()), int(inggris.get()), prediksi_prodi)

geografi_label = tk.Label(master=jendela, text=f'Nilai Geografi', font=('Inter', 12), fg='#FFFFFF', bg='#729c9b')   #alfan
geografi_label.place (relx=0.5, rely=0.18, anchor='center') #alfan

geografi = tk.Entry(master=jendela, font=('Inter', 12), width=30, fg='#FFFFFF', bg='#729c9b', highlightcolor='#FFF0CE', highlightthickness=2,textvariable=geografi) #alfan
geografi.place (relx=0.5, rely=0.25, anchor='center')  #alfan

matematika_label = tk.Label(master=jendela, text=f'Nilai Matematika', font=('Inter', 12), fg='#FFFFFF', bg='#729c9b') #Arya Bagas
matematika_label.place (relx=0.5, rely=0.32, anchor='center') #Arya Bagas

matematika = tk.Entry(master=jendela, font=('Inter', 12), width=30, fg='#FFFFFF', bg='#729c9b', highlightcolor="#FFF0CE", highlightthickness=2,textvariable=matematika) #Arya Bagas
matematika.place (relx=0.5, rely=0.39, anchor='center')  #Arya Bagas

bahasa_inggris_label = tk.Label(master=jendela, text=f'Nilai bahasa inggris', font=('Inter', 12), fg='#FFFFFF', bg='#729c9b') #Zaky
bahasa_inggris_label.place (relx=0.5, rely=0.46, anchor='center')  #Zaky

bahasa_inggris = tk.Entry(master=jendela, font=('Inter', 12), width=30, fg='#FFFFFF', bg='#729c9b', highlightcolor="#FFF0CE", highlightthickness=2, textvariable=inggris) #Zaky
bahasa_inggris.place (relx=0.5, rely=0.53, anchor='center') #Zaky

prediksi_button = tk.Button(jendela, text='prediksi', command=prediksi) #elga
prediksi_button.pack() #elga

hasil_label = tk.Label(jendela, text="")  #diva
hasil_label.pack(pady=10)  #diva

jendela.mainloop() #diva

conn.close()