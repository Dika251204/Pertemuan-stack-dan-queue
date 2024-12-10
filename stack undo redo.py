class UndoRedoApp:
    def __init__(self):
        self.history = []  # Menyimpan semua aksi yang dilakukan
        self.undo_stack = []  # Menyimpan aksi yang bisa di-undo
        self.redo_stack = []  # Menyimpan aksi yang bisa di-redo

    def lakukan_aksi(self, aksi):
        """Melakukan aksi baru dan menyimpannya ke dalam undo stack"""
        self.history.append(aksi)
        self.undo_stack.append(aksi)
        self.redo_stack.clear()  # Setiap kali aksi baru dilakukan, redo stack dibersihkan
        print(f"Aksi '{aksi}' telah dilakukan.")

    def undo(self):
        """Melakukan undo (menghapus aksi terakhir dari undo stack)"""
        if self.undo_stack:
            aksi_terakhir = self.undo_stack.pop()  # Mengambil aksi terakhir untuk di-undo
            self.redo_stack.append(aksi_terakhir)  # Menyimpan aksi yang di-undo ke redo stack
            print(f"Aksi '{aksi_terakhir}' di-undo.")
        else:
            print("Tidak ada aksi yang bisa di-undo.")

    def redo(self):
        """Melakukan redo (mengembalikan aksi yang di-undo)"""
        if self.redo_stack:
            aksi_redo = self.redo_stack.pop()  # Mengambil aksi yang ada di redo stack
            self.undo_stack.append(aksi_redo)  # Menyimpan aksi yang di-redo ke undo stack
            print(f"Aksi '{aksi_redo}' di-redo.")
        else:
            print("Tidak ada aksi yang bisa di-redo.")

    def lihat_stack(self):
        """Menampilkan stack undo dan redo"""
        print("\nStack Undo:")
        print(self.undo_stack)
        print("\nStack Redo:")
        print(self.redo_stack)

    def keluar(self):
        """Keluar dari program"""
        print("Terima kasih telah menggunakan program ini!")
        exit()

# Fungsi utama untuk menjalankan program
def main():
    app = UndoRedoApp()

    while True:
        print("\nPilihan Menu:")
        print("1. Lakukan aksi baru")
        print("2. Undo")
        print("3. Redo")
        print("4. Lihat stack Undo dan Redo")
        print("5. Keluar")

        try:
            pilihan = int(input("Masukkan pilihan (1-5): "))
            if pilihan == 1:
                aksi = input("Masukkan aksi yang ingin dilakukan: ")
                app.lakukan_aksi(aksi)
            elif pilihan == 2:
                app.undo()
            elif pilihan == 3:
                app.redo()
            elif pilihan == 4:
                app.lihat_stack()
            elif pilihan == 5:
                app.keluar()
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Input tidak valid. Masukkan angka antara 1 hingga 5.")

if __name__ == "__main__":
    main()
