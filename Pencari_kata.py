import tkinter as tk
from tkinter import messagebox

# Fungsi untuk mencari kata dalam kalimat
def cari_kata():
    kalimat = entry_kalimat.get()
    kata = entry_kata.get()
    if kata in kalimat:
        hasil = f'Kata "{kata}" ditemukan dalam kalimat.'
    else:
        hasil = f'Kata "{kata}" tidak ditemukan dalam kalimat.'
    messagebox.showinfo("Hasil Pencarian", hasil)

# Membuat jendela utama
root = tk.Tk()
root.title("Pencari Kata")

# Membuat label dan entry untuk kalimat
label_kalimat = tk.Label(root, text="Masukkan kalimat:")
label_kalimat.pack(pady=5)
entry_kalimat = tk.Entry(root, width=50)
entry_kalimat.pack(pady=5)

# Membuat label dan entry untuk kata
label_kata = tk.Label(root, text="Masukkan kata yang ingin dicari:")
label_kata.pack(pady=5)
entry_kata = tk.Entry(root, width=50)
entry_kata.pack(pady=5)

# Membuat tombol untuk mencari kata
button_cari = tk.Button(root, text="Cari Kata", command=cari_kata)
button_cari.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
