def check_password_with_repeats(password):
    # Menghitung panjang kata sandi
    password_length = len(password)
    
    # Inisialisasi variabel untuk menghitung karakter yang diulang
    repeated_chars = 0
    
    # Loop melalui karakter-karakter dalam kata sandi
    for i in range(1, password_length):
        if password[i] == password[i - 1]:
            repeated_chars += 1
    
    # Menilai kekuatan kata sandi
    if repeated_chars > 0:
        return "Kata sandi lemah: Terdapat karakter yang diulang."
    else:
        return "Kata sandi kuat."

# Mengambil input kata sandi dari pengguna
password = input("Masukkan kata sandi: ")

# Memeriksa kata sandi dengan fungsi
result = check_password_with_repeats(password)

# Menampilkan hasil
print(result)
