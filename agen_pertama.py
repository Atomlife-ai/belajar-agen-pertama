import pandas as pd

# Versi sederhana tanpa API dulu, biar langsung jalan di GitHub
# Ini simulasi otak agen

def cari_di_excel(nama_item):
    print(f"[TOOL] Cari di Excel: {nama_item}")
    try:
        df = pd.read_excel("data.xlsx")
        hasil = df[df.apply(lambda r: nama_item.lower() in str(r).lower(), axis=1)]
        if hasil.empty:
            return "Tidak ketemu di Excel"
        return f"Ketemu di Excel:\n{hasil.to_string()}"
    except Exception as e:
        return f"Error baca Excel: {e}"

def cari_di_web_perusahaan(nama_item):
    print(f"[TOOL] Cari di Web Perusahaan: {nama_item}")
    return f"Di web perusahaan, {nama_item} harganya Rp 27.000"

def jalankan_agen(pertanyaan):
    print(f"USER: {pertanyaan}\n")
    
    # Langkah 1: Cek Excel dulu (aturan agen)
    hasil1 = cari_di_excel(pertanyaan)
    print(hasil1)
    
    # Langkah 2: Kalau Excel kosong / tidak ada harga, lanjut
    if "Tidak ketemu" in hasil1 or "Error" in hasil1 or "harga" in hasil1.lower():
        hasil2 = cari_di_web_perusahaan(pertanyaan)
        print(hasil2)
        print("\n=== JAWABAN FINAL AGEN ===")
        print(f"Gabungan: {hasil1} + {hasil2}. Sumber: Excel & Web Perusahaan")
    else:
        print("\n=== JAWABAN FINAL AGEN ===")
        print(hasil1)

jalankan_agen("Kabel NYM 2x1.5")
