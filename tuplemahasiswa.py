# Mendefinisikan tuple dengan data mahasiswa
mahasiswa = ("andi", "galang", "ucup", "udin", "salsa")

# Meminta input dari pengguna untuk mencari nama
nama_dicari = input("Masukkan nama yang dicari: ").strip().lower()

# Mencari nama dalam tuple dan menampilkan pesan yang sesuai
if nama_dicari in mahasiswa:
    print(f"Data ditemukan, {nama_dicari}.")
else:
    print("Data tidak ditemukan.")
