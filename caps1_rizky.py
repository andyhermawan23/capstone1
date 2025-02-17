from tabulate import tabulate

keranjangBelanja = []  # Menyimpan barang yang dibeli

# Daftar produk pada toko vape store
daftarProduk = [
#                 ['Liquid Strawberry', 'Iceland', 10, 110000],
#                 ['Liquid Matcha', 'Besti', 20, 110000],
#                 ['Pod Foom X', 'Foom', 25, 250000],
#                 ['Pod Oxva Slim', 'Oxva', 15, 260000],
#                 ['Mod Thelema', 'Lost Vape', 15, 550000],
#                 ['Mod R234', 'Hotcig', 10, 560000]
                ]

# Menu utama program
def menuUtama():
    print('Selamat Datang di JCDS Vape Store')
        
    print('List Menu: ')
    print('1. Menampilkan Daftar Produk')
    print('2. Menambah Produk')
    print('3. Mengubah Produk')
    print('4. Menghapus Produk')
    print('5. Membeli Produk')
    print('6. Exit Program')
    

# Menampilkan pilihan kategori produk
def tampilkanPilihanKategori():
    print('Menu Kategori:')
    print('1. Tampilkan Semua Produk')
    print('2. Tampilkan Produk Tertentu (Liquid, Pod, Mod)')
    print('3. Cari Produk')
    print('4. Kembali ke Menu Utama')
    
# Menampilkan semua produk
def tampilkanSemuaProduk():
    data = [] # untuk menyimpan data produk yang akan ditampilkan
    for i in range(len(daftarProduk)): # mengiterasi semua index
        sublist = [i, daftarProduk[i][0], daftarProduk[i][1], daftarProduk[i][2], daftarProduk[i][3]] #i index produk, 0 nama produk
        # .append() digunakan untuk menambahkan semua data produk ke dalam list data
        data.append(sublist)
    print('\nSemua Produk:\n')
    print(tabulate(data, headers=['Index', 'Nama', 'Merk', 'Stok', 'Harga (Rp)'], tablefmt='simple'))
    
# Menampilkan daftar produk berdasarkan kategori
def tampilkanProdukKategori(kategori): # parameter spesifik
    data = []
    for i in range(len(daftarProduk)):
        if kategori.lower() in daftarProduk[i][0].lower(): # Menggunakan indeks 0 (nama produk) untuk memeriksa kategori
            # .append() digunakan untuk menambahkan data produk yang sesuai dengan kategori ke dalam list data.
            data.append([i, daftarProduk[i][0], daftarProduk[i][1], daftarProduk[i][2], 'Rp. {:,.0f}'.format(daftarProduk[i][3])])
    if data: # jika datanya ada, maka print
        print(f'Daftar Produk Kategori {kategori}\n')
        print(tabulate(data, headers=['Index', 'Nama', 'Merk', 'Stok', 'Harga (Rp)'], tablefmt='simple'))
    else:
        print(f'Tidak ada produk dalam kategori {kategori}.')
    
# Mencari produk berdasarkan nama
def cariProduk(nama):
    data = []
    for i in range(len(daftarProduk)):
        if nama.lower() in daftarProduk[i][0].lower():
            data.append([i, daftarProduk[i][0], daftarProduk[i][1], daftarProduk[i][2], 'Rp. {:,.0f}'.format(daftarProduk[i][3])])
    if not data:
        print("Produk yang Anda cari tidak ada.")
    else:
        print('\nHasil Pencarian Produk\n')
        print(tabulate(data, headers=['Index', 'Nama', 'Merk', 'Stok', 'Harga (Rp)'], tablefmt='simple'))


# Menambahkan produk baru ke dalam daftar produk
def tambahProduk():
    while True: # iterasi berjalan terus menerus
        namaProduk = input('Masukkan Nama Produk: ').title()
        if len(namaProduk) == 0:
            print("Nama produk tidak boleh kosong.")
            continue
        elif len(namaProduk) > 20:
            print("Nama produk terlalu panjang. Harap masukkan maksimal 20 karakter.")
            continue
        for char in namaProduk: # Memeriksa setiap karakter dalam namaProduk
            if not (char.isalnum() or char.isspace()): # Jika karakter bukan huruf, angka, atau spasi
                print('Input tidak valid. Harap masukkan hanya huruf dan angka.') 
                break # Keluar dari loop
        else:
            for produk in daftarProduk: # Jika semua karakter valid, lanjutkan dengan memeriksa apakah produk sudah ada dalam daftar
                if namaProduk.lower() == produk[0].lower(): # Membandingkan nama produk dengan nama produk dalam daftar
                    print('Produk sudah ada dalam daftar. Masukkan nama produk lain.') 
                    # Jika nama produk sudah ada dalam daftarProduk, cetak pesan dan keluar dari loop
                    break
            else:
                break # Jika nama produk tidak ada dalam daftarProduk, keluar dari loop

    while True:
        merkProduk = input('Masukkan Merk Produk: ').title()
        if len(merkProduk) == 0:
            print("Merk produk tidak boleh kosong.")
            continue
        elif len(merkProduk) > 20:
            print("Merk produk terlalu panjang. Harap masukkan maksimal 20 karakter.")
            continue
        for char in merkProduk:
            if char.isalnum() or char.isspace(): # Memeriksa apakah karakter adalah huruf, angka, atau spasi
                continue
            else:
                print('Input tidak valid. Harap masukkan hanya huruf dan angka.')
                break
    
        while True: # Loop untuk memasukkan stok produk, harga produk dan menampilkan daftar produk baru
            while True:
                stokProduk = input('Masukkan Stok Produk: ')
                if stokProduk.isdigit():  
                    stokProduk = int(stokProduk) # konversi menggunakan int pada index
                    if stokProduk > 0:
                        break
                    else:
                        print('Stok harus lebih dari 0.')
                else:
                    print('Input tidak valid. Harap masukkan hanya angka.')

            while True:
                hargaProduk = input('Masukkan Harga Produk: ')
                if hargaProduk.isdigit():  
                    hargaProduk = int(hargaProduk)
                    if hargaProduk > 0:
                        break
                    else:
                        print('Harga harus lebih dari 0.')
                else:
                    print('Input tidak valid. Harap masukkan hanya angka.')
        
            # Menampilkan data produk baru
            print('\nData Produk Baru:')
            print('Nama Produk:', namaProduk)
            print('Merk Produk:', merkProduk)
            print('Stok Produk:', stokProduk)
            print('Harga Produk:', hargaProduk)
                
            # loop konfirmasi penyimpanan
            while True:
                checker = input('Apakah ingin menyimpan produk yang baru ditambahkan? (y/t): ').lower()
                if checker == 'y':
                    daftarProduk.append([namaProduk, merkProduk, stokProduk, hargaProduk])
                    print('Data produk disimpan.')
                    break
                elif checker == 't':
                    print('Data produk tidak disimpan.')
                    break
                else:
                    print("Input tidak valid. Silahkan masukkan 'y' untuk ya atau 't' untuk tidak.")
            tampilkanSemuaProduk()
            break  # Keluar dari iterasi setelah produk ditambahkan
        break
    
# Mengubah informasi sebuah produk
def ubahProduk():
    while True:
        tampilkanSemuaProduk()
        indexProduk = input('Masukkan index produk yang ingin diupdate: ')
        if indexProduk.isdigit():
            indexProduk = int(indexProduk)
            if 0 <= indexProduk < len(daftarProduk): # Memeriksa apakah nomor produk valid
                produk = daftarProduk[indexProduk] # Mengambil produk yang akan diubah dari daftar produk
                print("Produk yang akan diubah:")
                print("Nama Produk:", produk[0])
                print("Merk Produk:", produk[1])
                print("Stok Produk:", produk[2])
                print("Harga Produk:", produk[3])
                while True:
                    print('Masukkan keyword yang ingin diubah (nama/merk/stok/harga):')
                    keyword = input('Keyword: ').lower()
                    if keyword == 'nama':
                        while True:
                            value = input('Masukkan nama produk baru: ').title()
                            if value and len(value) <= 20: # memastikan input tidak boleh kosong
                                # Memeriksa apakah ada duplikasi nama produk
                                duplicated = False
                                for cek in daftarProduk:
                                    if cek != produk and cek[0].lower() == value.lower():
                                        duplicated = True
                                        break
                                if duplicated:
                                    print('Nama produk sudah ada. Tidak diperbolehkan adanya duplikasi.')
                                else:
                                    produk[0] = value # Ubah nama produk dengan nama baru
                                    break
                            else:
                                print('Nama produk tidak boleh kosong dan maksimal 20 karakter.')
                                
                    elif keyword == 'merk':
                        while True:
                            value = input('Masukkan merk produk baru: ').title()
                            if value and len(value) <= 20:
                                produk[1] = value
                                break
                            else:
                                print('Merk produk tidak boleh kosong dan maksimal 20 karakter.')
                                
                    elif keyword == 'stok':
                        while True:
                            value = input('Masukkan jumlah stok produk baru: ')
                            if value.isdigit():
                                value = int(value)
                                if value > 0:
                                    produk[2] = value
                                    break
                                else:
                                    print('Stok harus lebih dari 0.')
                            else:
                                print('Stok harus berupa bilangan bulat.')
                                
                    elif keyword == 'harga':
                        while True:
                            value = input('Masukkan harga produk baru (Rp): ')
                            if value.isdigit():
                                value = int(value)
                                if value > 0:
                                    produk[3] = value
                                    break
                                else:
                                    print('Harga harus lebih dari 0.')
                            else:
                                print('Harga harus berupa bilangan bulat.')
                    else:
                        print('Keyword tidak valid. Harap masukkan salah satu dari: nama, merk, stok, atau harga.')
                        break
                    
                    checker = input('Apakah Anda yakin ingin mengubah produk ini? (y/t): ').lower()
                    while checker not in ['y', 't']:  
                        print('Input tidak valid. Silahkan masukkan "y" untuk ya atau "t" untuk tidak.')
                    if checker == 't':
                        print('Perubahan produk tidak disimpan.')
                        tampilkanSemuaProduk()
                        break
                    elif checker == 'y':
                        daftarProduk[indexProduk] = produk
                        print('Perubahan produk berhasil disimpan.')
                        tampilkanSemuaProduk()
                        break
                break  # Kembali ke submenu setelah selesai mengubah produk
            else:
                print("index produk tidak valid.")
        else:
            print("index produk harus berupa bilangan bulat.")

# Menghapus sebuah produk dari daftar produk
def hapusProduk():
    while True:
        tampilkanSemuaProduk()
        indexProduk = input("Masukkan Index Produk yang ingin dihapus: ")
        if indexProduk.isdigit():
            indexProduk = int(indexProduk)
            if 0 <= indexProduk < len(daftarProduk):
                print("Produk yang akan dihapus:")
                print("Nama Produk:", daftarProduk[indexProduk][0])
                print("Merk Produk:", daftarProduk[indexProduk][1])
                print("Stok Produk:", daftarProduk[indexProduk][2])
                print("Harga Produk:", daftarProduk[indexProduk][3])
                checker = input('Apakah Anda yakin ingin menghapus produk ini? (y/t): ').lower()
                while checker not in ['y', 't']:  
                    print('Input tidak valid. Silahkan masukkan "y" untuk ya atau "t" untuk tidak.')
                    checker = input('Apakah ingin menghapus yang lain? (y/t): ').lower()
                if checker == 't':
                    print('Penghapusan produk dibatalkan.')
                    tampilkanSemuaProduk()
                    break 
                elif checker == 'y':
                    del daftarProduk[indexProduk]
                    print('Produk berhasil dihapus.')
                    tampilkanSemuaProduk()
                    break 
            else:
                print('index produk tidak valid.')
        else:
            print("Input tidak valid. Harap masukkan index produk yang sesuai.")

# Melakukan pembelian produk
def beliProduk():
     # Pengecekan jika semua stok produk telah habis
    if all(produk[2] == 0 for produk in daftarProduk):
        print("Maaf, semua produk sudah habis.")
        return
    # for produk in daftarProduk:
    #     # Memeriksa apakah stok produk saat ini adalah 0
    #     if all(produk[2] == 0):
    #         # Jika stok produk habis, cetak pesan dan keluar dari blok kode atau fungsi
    #         print("Maaf, semua produk sudah habis.")
    #         return
    
    tampilkanSemuaProduk()
    while True:
        indexProdukInput = input('Masukkan Index Produk yang ingin dibeli : ')
        if indexProdukInput.isdigit():  
            indexProduk = int(indexProdukInput)
            if 0 <= indexProduk < len(daftarProduk):
                if daftarProduk[indexProduk][2] == 0: # ngecek apakah stok = 0
                    print(f'Stok {daftarProduk[indexProduk][0]} sudah habis.')
                    continue  
                while True:
                    qtyProdukInput = input('Masukkan jumlah yang ingin dibeli : ')
                    if qtyProdukInput.isdigit():
                        qtyProduk = int(qtyProdukInput)
                        if qtyProduk > daftarProduk[indexProduk][2]: # ngecek jika stok tidak cukup
                            print(f'Stok tidak cukup, stok {daftarProduk[indexProduk][0]} tinggal {daftarProduk[indexProduk][2]}')
                            return
                        else:
                            # Menambahkan produk ke keranjang belanja
                            keranjangBelanja.append([daftarProduk[indexProduk][0], daftarProduk[indexProduk][1], qtyProduk, daftarProduk[indexProduk][3], indexProduk])
                            # Mengurangi stok produk di daftarProduk
                            daftarProduk[indexProduk][2] -= qtyProduk
                        break
                    else:
                        print('Inputan harus berupa angka. Silahkan coba lagi.')
                        
                print('Isi Keranjang Belanja :')
                dataKeranjang = []
                for item in keranjangBelanja:
                    # Membuat entri data untuk setiap item dalam keranjang belanja dengan format yang diinginkan
                    entry = [item[0], item[1], item[2], 'Rp. {:,.0f}'.format(item[3])]
                    # Menambahkan entri data ke dalam list dataKeranjang
                    dataKeranjang.append(entry)
                # Menampilkan data keranjang belanja menggunakan tabulate
                print(tabulate(dataKeranjang, headers=['Nama', 'Merk', 'Qty', 'Harga (Rp)'], tablefmt='simple'))

                checker = input('Apakah ingin membeli yang lain? (y/t): ').lower()
                while checker not in ['y', 't']:  
                    print('Input tidak valid. Silahkan masukkan "y" untuk ya atau "t" untuk tidak.')
                if checker == 't':
                    break
                elif checker == 'y':
                    # Memeriksa apakah masih ada stok yang tersedia
                    if all(produk[2] == 0 for produk in daftarProduk):
                        print("Maaf, semua produk sudah habis.")
                        break
                    else:
                        tampilkanSemuaProduk()
            else:
                print('Input tidak valid. Masukkan index produk yang sesuai.')
        else:
            print('Inputan harus berupa angka. Silahkan coba lagi.')
            
    total_pembelian = 0
    for item in keranjangBelanja:
        # Menghitung total pembelian dengan menjumlahkan harga total setiap item dalam keranjang belanja
        total_pembelian += item[2] * item[3]
    print(f'Total Pembelian: Rp {total_pembelian:,}')

    while True:
        pembayaran = input('Masukkan jumlah pembayaran: Rp ')
        if pembayaran.isdigit():
            pembayaran = int(pembayaran)
            break
        else:
            print('Inputan harus berupa angka. Silahkan coba lagi.')
            
    kembalian = pembayaran - total_pembelian
    if kembalian >= 0:
        print(f'Pembayaran berhasil. Kembalian Anda: Rp. {kembalian:,}')
    else:
        print('Pembayaran tidak mencukupi.')
        while True:
            pembayaran = input('Uang Anda kurang. Masukkan jumlah pembayaran yang mencukupi: Rp ')
            if pembayaran.isdigit():
                pembayaran = int(pembayaran)
                if pembayaran >= total_pembelian:
                    kembalian = pembayaran - total_pembelian
                    print(f'Pembayaran berhasil. Kembalian Anda: Rp. {kembalian:,}')
                    break
                else:
                    print('Pembayaran tidak mencukupi. Masukkan jumlah yang mencukupi.')
            else:
                print('Inputan harus berupa angka. Silahkan coba lagi.')
    # Mengosongkan keranjang belanja setelah transaksi selesai
    keranjangBelanja.clear()

# Daftar semua menu
while True:
    menuUtama()
    pilihanMenu = input('Masukkan pilihan menu: ')
    if pilihanMenu == '1': # Menampilkan daftar produk
        while True:
            tampilkanPilihanKategori()
            pilihanKategori = input('Masukkan angka kategori (1 - 4): ')
            if pilihanKategori.isdigit() and 1 <= int(pilihanKategori) <= 4:  # Menambahkan validasi input
                if pilihanKategori == '1': # tampilkan semua produk
                    if not daftarProduk:
                        print('Maaf, tidak ada produk yang tersedia saat ini')
                    else:
                        tampilkanSemuaProduk()
                elif pilihanKategori == '2': # Tampilkan produk tertentu
                    if not daftarProduk:
                        print('Maaf, tidak ada produk yang tersedia saat ini')
                    else:
                        while True:
                            print('Pilih jenis produk:')
                            print('1. Liquid')
                            print('2. Pod')
                            print('3. Mod')
                            print('4. Kembali ke Menu Kategori')
                            jenisProduk = input('Masukkan angka jenis produk (1 - 4): ')
                            if jenisProduk == '1':
                                tampilkanProdukKategori('Liquid')
                            elif jenisProduk == '2':
                                tampilkanProdukKategori('Pod')
                            elif jenisProduk == '3':
                                tampilkanProdukKategori('Mod')
                            elif jenisProduk == '4':
                                break
                            else:
                                print('Inputan tidak valid. Harap masukkan angka antara 1 dan 4.')
                elif pilihanKategori == '3': # Cari produk berdasarkan nama
                    if not daftarProduk:
                        print('Maaf, tidak ada produk yang tersedia saat ini')
                    else:
                        keyword = input('Masukkan nama produk yang ingin dicari: ').lower()
                        cariProduk(keyword)
                    
                elif pilihanKategori == '4': # kembali ke main menu
                    break
                else:
                    print('Inputan tidak valid. Harap masukkan angka antara 1 dan 4.')

    elif pilihanMenu == '2': # Menambah produk
        while True:
            print("1. Tambah Produk")
            print("2. Kembali ke Menu Utama")
            subMenu = input("Pilih menu: ")
            if subMenu == '1':
                tambahProduk()
            elif subMenu == '2':
                tampilkanPilihanKategori()
                break
            else:
                print("Pilihan tidak valid. Silahkan pilih antara 1 atau 2.")

    elif pilihanMenu == '3': # Mengubah produk
        while True:
            print("1. Ubah Produk")
            print("2. Kembali ke Menu Utama")
            subMenu = input("Pilih menu: ")
            if subMenu == '1':
                if not daftarProduk:
                    print('Maaf, tidak ada produk yang tersedia saat ini')
                    continue
                ubahProduk()
            elif subMenu == '2':
                tampilkanPilihanKategori()
                break
            else:
                print("Pilihan tidak valid. Silakan pilih antara 1 atau 2.")
                
    elif pilihanMenu == '4': # Menghapus produk
        while True:
            print("1. Hapus Produk")
            print("2. Kembali ke Menu Utama")
            subMenu = input("Pilih menu: ")
            if subMenu == '1':
                if not daftarProduk:
                    print('Maaf, tidak ada produk yang tersedia saat ini')
                    continue
                hapusProduk()
            elif subMenu == '2':
                tampilkanPilihanKategori()
                break
            else:
                print("Pilihan tidak valid. Silakan pilih antara 1 atau 2.")
                
    elif pilihanMenu == '5': # Membeli produk
        while True:
            print("1. Beli Produk")
            print("2. Kembali ke Menu Utama")
            subMenu = input("Pilih menu: ")
            if subMenu == '1':
                if not daftarProduk:
                    print('Maaf, tidak ada produk yang tersedia saat ini')
                    continue
                beliProduk()
            elif subMenu == '2':
                tampilkanPilihanKategori()
                break
            else:
                print("Pilihan tidak valid. Silahkan pilih antara 1 atau 2.")
        
    elif pilihanMenu == '6': # Exit
        print('Terima Kasih telah mengunjungi JCDS Vape Store. Sampai Jumpa Kembali!!')
        break
    else:
        print('Pilihan menu tidak valid. Masukkan angka menu antara 1 dan 6.')
