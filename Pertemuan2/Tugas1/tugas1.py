def init_data():
    return {"accounts": {}, "book_collections": {}}

def register(nim, password, accounts):
    if nim in accounts:
        return "NIM sudah terdaftar.", accounts
    # Mengembalikan data baru tanpa mengubah state yang ada
    new_accounts = {**accounts, nim: password}
    return "Registrasi berhasil!", new_accounts

def login(nim, password, accounts):
    if nim in accounts and accounts[nim] == password:
        return "Login berhasil!", True
    return "NIM atau password salah.", False

def add_book(nim, title, author, year, book_collections):
    new_book_info = (title, author, year)
    current_books = book_collections.get(nim, [])
    new_books = current_books + [new_book_info]
    new_book_collections = {**book_collections, nim: new_books}
    return f"Buku '{title}' berhasil ditambahkan ke koleksi.", new_book_collections

def view_books(nim, book_collections):
    if nim in book_collections and book_collections[nim]:
        result = "Koleksi Buku Anda:\n"
        for index, book in enumerate(book_collections[nim], start=1):
            result += f"{index}. Judul: {book[0]}, Penulis: {book[1]}, Tahun: {book[2]}\n"
        return result.strip(), book_collections
    else:
        return "Tidak ada buku dalam koleksi.", book_collections

def edit_book(nim, book_collections, book_index, title, author, year):
    if nim in book_collections and book_collections[nim]:
        current_books = book_collections[nim]
        if 0 <= book_index < len(current_books):
            updated_book = (title, author, year)
            new_books = current_books[:book_index] + [updated_book] + current_books[book_index + 1:]
            new_book_collections = {**book_collections, nim: new_books}
            return "Buku berhasil diganti.", new_book_collections
    return "Buku tidak ditemukan.", book_collections

def delete_book(nim, book_collections, book_index):
    if nim in book_collections and book_collections[nim]:
        current_books = book_collections[nim]
        if 0 <= book_index < len(current_books):
            removed_book = current_books[book_index]
            new_books = current_books[:book_index] + current_books[book_index + 1:]
            new_book_collections = {**book_collections, nim: new_books}
            return f"Buku '{removed_book[0]}' telah dikembalikan.", new_book_collections
    return "Buku tidak ditemukan.", book_collections

# Fungsi untuk Menu User (Pure Function)
def user_menu(nim, accounts, book_collections):
    while True:
        print("\nMenu:")
        print("1. Pinjam Buku")
        print("2. Lihat Koleksi Buku")
        print("3. Tukar Buku")
        print("4. Kembalikan Buku")
        print("5. Logout")
        
        choice = input("Pilih menu: ")

        if choice == '1':
            title = input("Masukkan judul buku: ")
            author = input("Masukkan penulis buku: ")
            year = input("Masukkan tahun terbit: ")
            message, book_collections = add_book(nim, title, author, year, book_collections)
            print(message)

        elif choice == '2':
            message, book_collections = view_books(nim, book_collections)
            print(message)

        elif choice == '3':
            book_index = int(input("Pilih nomor buku yang ingin ditukar1: ")) - 1
            title = input("Masukkan judul baru: ")
            author = input("Masukkan penulis baru: ")
            year = input("Masukkan tahun terbit baru: ")
            message, book_collections = edit_book(nim, book_collections, book_index, title, author, year)
            print(message)

        elif choice == '4':
            book_index = int(input("Pilih nomor buku yang ingin dihapus: ")) - 1
            message, book_collections = delete_book(nim, book_collections, book_index)
            print(message)

        elif choice == '5':
            print("Anda telah logout.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# Fungsi Menu Utama (Pure Function)
def main_menu(accounts, book_collections):
    while True:
        print("\nSelamat datang di aplikasi PerpusOnline!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Pilih menu: ")

        if choice == '1':
            nim = input("Masukkan NIM: ")
            password = input("Masukkan password: ")
            message, accounts = register(nim, password, accounts)
            print(message)

        elif choice == '2':
            nim = input("Masukkan NIM: ")
            password = input("Masukkan password: ")
            message, success = login(nim, password, accounts)
            print(message)
            if success:
                user_menu(nim, accounts, book_collections)

        elif choice == '3':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# Main Program Execution
if __name__ == "__main__":
    data = init_data()
    accounts, book_collections = data['accounts'], data['book_collections']
    main_menu(accounts, book_collections)
