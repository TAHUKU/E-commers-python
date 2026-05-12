import json
import random

# 1. Menghasilkan Dataset
def data_barang(num=200):
    dataset = []
    for i in range(num):
        dataset.append({
            "nomer": i + 1,
            "product_id": f"PRD-{i:04d}",
            "nama_produk": f"Produk-{i}",
            "harga": random.randint(50, 500) * 1000, # Range 50rb - 500rb
            "rating": round(random.uniform(1.0, 5.0), 1)
        })
    return dataset

# Simpan ke JSON
data_awal = data_barang(200)
with open("data_produk.json", "w") as f:
    json.dump(data_awal, f, indent=4)

# 2. Selection Sort (Harga: Tinggi ke Rendah / Descending)
def urutkan_barang_sesuai_harga(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j]['harga'] > arr[max_idx]['harga']: # Tanda '>' untuk Descending
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

# 3. Insertion Sort (Rating: Tinggi ke Rendah / Descending)
def urutkan_barang_sesuai_rating(arr):
    n = len(arr)
    for i in range(1, n):
        key_item = arr[i]
        j = i - 1
        # Ubah tanda '<' menjadi '>' agar rating tertinggi ada di atas
        while j >= 0 and key_item['rating'] > arr[j]['rating']: 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

# --- EKSEKUSI DAN TAMPILAN ---

with open("data_produk.json", "r") as f:
    data_produk = json.load(f)

# Menampilkan Top 10 Harga Tertinggi
print(f"\n{'='*20} TOP 10 HARGA TERTINGGI (Selection Sort) {'='*20}")
print(f"{'No':<4} {'Nama Produk':<15} {'Harga':>15} {'Rating':>10}")
print("-" * 65)

hasil_harga = urutkan_barang_sesuai_harga(data_produk.copy())
for i, p in enumerate(hasil_harga[:10], start=1):
    print(f"{i:<4} {p['nama_produk']:<15} Rp {p['harga']:>12,} {p['rating']:>10}")

# Menampilkan Top 10 Rating Tertinggi
print(f"\n{'='*20} TOP 10 RATING TERTINGGI (Insertion Sort) {'='*20}")
print(f"{'No':<4} {'Nama Produk':<15} {'Rating':>10} {'Harga':>15}")
print("-" * 65)

hasil_rating = urutkan_barang_sesuai_rating(data_produk.copy())
for i, p in enumerate(hasil_rating[:10], start=1):
    print(f"{i:<4} {p['nama_produk']:<15} {p['rating']:>10} Rp {p['harga']:>12,}")