from collections import deque

def simulasi_antrian():
    queue = deque()  # Membuat antrean kosong
    while True:
        print("\n1. Tambah pelanggan ke antrian")
        print("2. Layani pelanggan")
        print("3. Tampilkan antrian")
        print("4. Keluar")
        
        pilihan = input("Pilih opsi: ")
        
        if pilihan == "1":
            nama = input("Masukkan nama pelanggan: ")
            queue.append(nama)
            print(f"Pelanggan {nama} ditambahkan ke antrian.")
        elif pilihan == "2":
            if queue:
                dilayani = queue.popleft()
                print(f"Pelanggan {dilayani} sedang dilayani.")
            else:
                print("Antrian kosong!")
        elif pilihan == "3":
            print("Antrian saat ini:", list(queue))
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid!")

# Menjalankan simulasi
simulasi_antrian()
