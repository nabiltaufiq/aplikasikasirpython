# kasir_barcode.py

# --- 1. Data Aplikasi dengan Barcode ---
# Key: Kode Barcode/SKU (String)
# Value: Dictionary detail item
MENU_BARCODE = {
    "03307377485022": {"nama": "Windows Ori", "harga": 1500000},
    "9786024865382": {"nama": "Buku Pemrograman Berorientasi Objek", "harga": 125000},
    "9786027680463": {"nama": "Buku Pemrograman Database dengan Java", "harga": 125000},
    "9786024346782": {"nama": "Buku Pemrograman Dasar", "harga": 100000},
    "9786024348168": {"nama": "Buku Simulasi dan Komunikasi Digital", "harga": 145000},
    "613500161770": {"nama": "Battery HP Xiaomi", "harga": 200000},
    "8910201379633": {"nama": "White Board Maker", "harga": 18000},
    "4710562752625": {"nama": "United Power 500W", "harga": 500000},
    "6935364052461": {"nama": "tp-link Access Point", "harga": 425000},
    "6935364050566": {"nama": "tp-link PCI Adapter", "harga": 255000},
    "22540FQ004320": {"nama": "HUB tp-link", "harga": 623000},
    "8806098269112": {"nama": "LG Monitor", "harga": 800000},
    "X4GG8500804": {"nama": "EPSON Proyektor", "harga": 5250000},
    "4549292111910": {"nama": "Canon EOS 1500D", "harga": 2500000},
    "502DA20AD96F": {"nama": "Laptop SONY", "harga": 4000000},
    "K5412330MX03776": {"nama": "Keyboard AXIOO", "harga": 250000},
    "51600074206": {"nama": "Acer Monitor", "harga": 650000}
    
}

# List global untuk menyimpan pesanan
pesanan = []

# --- 2. Fungsi Tampilan Menu ---
def tampilkan_menu():
    """Menampilkan daftar menu yang tersedia dengan kodenya."""
    print("\n================= DAFTAR MENU & KODE BARCODE =================")
    print("KODE \tITEM \t\tHARGA")
    print("----------------------------------------------------------")
    
    for kode, detail in MENU_BARCODE.items():
        nama = detail["nama"]
        harga = detail["harga"]
        # Menyesuaikan spasi
        spasi = "\t\t" if len(nama) < 10 else "\t"
        print(f"{kode} \t{nama}{spasi}Rp {harga:,.0f}")
        
    print("----------------------------------------------------------")

# --- 3. Fungsi Pemrosesan Kasir (Input Barcode) ---
def proses_kasir():
    """Loop utama untuk menerima input Barcode."""
    print("--- SELAMAT DATANG DI APLIKASI KASIR BARCODE CLI ---")
    
    while True:
        tampilkan_menu()
        
        # Menerima input: Barcode Scanner otomatis akan memasukkan kode
        barcode = input("SCAN BARCODE (atau ketik 'BAYAR' untuk selesai): ").strip()
        
        if barcode.upper() == "BAYAR":
            break # Keluar dari loop pemesanan

        if barcode in MENU_BARCODE:
            detail_item = MENU_BARCODE[barcode]
            menu_ditemukan = detail_item["nama"]
            harga_satuan = detail_item["harga"]
            
            # Asumsi default: Barcode Scanner membaca satu item (jumlah = 1)
            jumlah = 1 
            
            # *Opsional*: Tanyakan jumlah jika lebih dari 1
            tanya_jumlah = input(f"Menu: {menu_ditemukan}. Tambahkan {jumlah} item? (Tekan ENTER untuk YA, atau masukkan jumlah > 1): ").strip()
            
            if tanya_jumlah.isdigit() and int(tanya_jumlah) > 0:
                jumlah = int(tanya_jumlah)

            # Tambahkan pesanan ke list
            pesanan.append({
                "menu": menu_ditemukan,
                "jumlah": jumlah,
                "harga_satuan": harga_satuan,
                "subtotal": jumlah * harga_satuan
            })
            print(f"✅ Berhasil: {jumlah} '{menu_ditemukan}' ditambahkan. Total pesanan saat ini: {len(pesanan)} item.")

        else:
            print(f"❌ Gagal: Kode Barcode '{barcode}' tidak ditemukan. Mohon cek kode atau menu.")

    # Pindah ke tahap perhitungan dan pembayaran
    hitung_total()

# --- 4. Fungsi Perhitungan dan Struk ---
def hitung_total():
    """Menghitung total harga dan memproses pembayaran (Fungsi ini tidak berubah)."""
    if not pesanan:
        print("\nTidak ada pesanan yang dibuat. Aplikasi selesai.")
        return

    # Hitung total semua pesanan
    total_semua = sum(item["subtotal"] for item in pesanan)
    
    # Cetak Header Struk
    print("\n\n===================== STRUK PEMBAYARAN =====================")
    print("ITEM \t\tQTY \tHARGA SATUAN \tSUBTOTAL")
    print("------------------------------------------------------------")
    
    # Cetak Detail Pesanan
    for item in pesanan:
        menu = item["menu"]
        # Menyesuaikan spasi untuk tampilan yang rapi
        spasi = "\t\t" if len(menu) < 8 else "\t"
        print(f"{menu}{spasi}{item['jumlah']} \tRp {item['harga_satuan']:,.0f} \tRp {item['subtotal']:,.0f}")
        
    print("------------------------------------------------------------")
    print(f"TOTAL \t\t\t\t\t\t\tRp {total_semua:,.0f}")
    
    # Proses Pembayaran
    while True:
        try:
            bayar = int(input("💰 Masukkan jumlah pembayaran (Rp): "))
            
            if bayar < total_semua:
                print(f"❌ Pembayaran Gagal: Uang yang dibayarkan kurang. Kurang Rp {(total_semua - bayar):,.0f}")
            else:
                kembalian = bayar - total_semua
                print(f"UANG DIBAYAR \t\t\t\t\t\tRp {bayar:,.0f}")
                print(f"KEMBALIAN \t\t\t\t\t\tRp {kembalian:,.0f}")
                print("============================================================")
                print("🎉 TERIMA KASIH TELAH BERBELANJA! 🎉")
                break
        except ValueError:
            print("❌ Input pembayaran tidak valid. Harap masukkan angka.")

# --- 5. Titik Masuk Program ---
if __name__ == "__main__":
    proses_kasir()