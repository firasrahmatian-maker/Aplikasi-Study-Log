catatan = []

def tambah_catatan():
    """Meminta input dari pengguna dan menyimpan catatan ke dalam list `catatan`.
    Struktur catatan adalah dictionary sederhana:
    {'mapel': str, 'topik': str, 'durasi': int}
    """
    mapel = input("Masukkan mata pelajaran: ").strip()
    topik = input("Masukkan topik: ").strip()

    # Validasi durasi agar berupa angka positif
    while True:
        durasi_input = input("Masukkan durasi belajar (menit): ").strip()
        if durasi_input.isdigit() and int(durasi_input) > 0:
            durasi = int(durasi_input)
            break
        else:
            print("Durasi harus berupa angka positif. Coba lagi.")

    catatan.append({'mapel': mapel, 'topik': topik, 'durasi': durasi})
    print("Catatan berhasil ditambahkan ✅")


def lihat_catatan():
    """Menampilkan semua catatan yang tersimpan dalam format tabel rapi.

    Jika belum ada catatan, tampilkan pesan yang sesuai.
    """
    if not catatan:
        print("Belum ada catatan.")
        return

    # Tentukan lebar kolom berdasarkan isi agar rapi
    no_w = 4
    mapel_w = max(len("Mapel"), max((len(c['mapel']) for c in catatan), default=0))
    topik_w = max(len("Topik"), max((len(c['topik']) for c in catatan), default=0))
    durasi_w = len("Durasi")

    # Header
    print()
    header = f"{'No':<{no_w}}  {'Mapel':<{mapel_w}}  {'Topik':<{topik_w}}  {'Durasi':>{durasi_w}}"
    print(header)
    print('-' * len(header))

    # Baris data
    for i, c in enumerate(catatan, start=1):
        print(f"{i:<{no_w}}  {c['mapel']:<{mapel_w}}  {c['topik']:<{topik_w}}  {c['durasi']:>{durasi_w}} menit")

    # Footer ringkasan
    print(f"\nTotal: {len(catatan)} catatan")


# Fitur target harian
# Nilai None berarti belum diatur
target_harian = None

def set_target_harian():
    """Meminta input target harian dalam menit dan menyimpannya ke `target_harian`."""
    global target_harian
    while True:
        nilai = input("Masukkan target harian (menit): ").strip()
        if nilai.isdigit() and int(nilai) > 0:
            target_harian = int(nilai)
            print(f"Target harian disimpan: {target_harian} menit ✅")
            break
        else:
            print("Masukkan angka positif. Coba lagi.")


def lihat_target_harian():
    """Menampilkan target yang sedang diatur (jika ada)."""
    if target_harian is None:
        print("Target harian: Belum diatur.")
    else:
        jam, menit = divmod(target_harian, 60)
        if jam:
            print(f"Target harian: {target_harian} menit ({jam} jam {menit} menit)")
        else:
            print(f"Target harian: {target_harian} menit")


def hapus_target_harian():
    """Menghapus target harian yang tersimpan."""
    global target_harian
    if target_harian is None:
        print("Belum ada target untuk dihapus.")
    else:
        target_harian = None
        print("Target harian telah dihapus.")


def cek_progress_target():
    """Menghitung total waktu belajar dan membandingkan dengan target (jika ada)."""
    if target_harian is None:
        print("Belum ada target. Silakan atur target terlebih dahulu.")
        return

    total = sum(c['durasi'] for c in catatan)
    sisa = target_harian - total
    persen = int(total / target_harian * 100) if target_harian else 0

    print(f"Total hari ini: {total} menit")
    if sisa <= 0:
        print(f"Selamat! Target tercapai ✅ (tercapai {abs(sisa)} menit lebih)")
    else:
        print(f"Sisa untuk mencapai target: {sisa} menit ({persen}% terpenuhi)")


def target_menu():
    """Sub-menu untuk fitur Target Harian."""
    while True:
        print("\n=== Menu Target Harian ===")
        lihat_target_harian()
        print("1. Atur/Ubah target")
        print("2. Hapus target")
        print("3. Cek progres terhadap target")
        print("4. Kembali")

        p = input("Pilih: ").strip()
        if p == "1":
            set_target_harian()
        elif p == "2":
            hapus_target_harian()
        elif p == "3":
            cek_progress_target()
        elif p == "4":
            break
        else:
            print("Pilihan tidak valid")


def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")
    print("5. Target harian")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    elif pilihan == "5":
        target_menu()
    else:
        print("Pilihan tidak valid")