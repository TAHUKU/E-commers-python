import json
import random

def data_barang(num=200):
    dataset = []
    for i in range(num):
        dataset.append({
            "nomer": i + 1,
            "product_id": f"PRD-{i:04d}",
            "nama_produk": f"Produk-{i}",
            "harga": random.randint(5, 500) * 1000,
            "rating": round(random.uniform(1.0, 5.0), 1)
        })
    return dataset

data_awal = data_barang(200)
with open("data_produk.json", "w") as f:
    json.dump(data_awal, f, indent=4)

# Pengurutam berdasarkan harga (Descending: tinggi ke rendah)

def urutkan_barang_sesuai_harga(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j]['harga'] > arr[max_idx]['harga']:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

# Pengurutan berdasarkan rating (Ascending: rendah ke tertinggi)

def urutkan_barang_sesuai_rating(arr):
    n = len(arr)
    for i in range(1, n):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and key_item['rating'] < arr[j]['rating']:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

# menampilkan
# Membuat data dari JSON

with open("data_produk.json", "r") as f:
    data_produk = json.load(f)

# Menampilkan 
print("=== top 10 produk: Harga tertinggi (Selection sort) ===")
hasil_harga = urutkan_barang_sesuai_harga(data_produk.copy())
for i, product in enumerate(hasil_harga[:10], start=1):
    print(f"{i}. {product['nama_produk']} |Harga: Rp{product['harga']:,} | Rating: {product['rating']}")

print("\n=== top 10 produk: Rating tertinggi (Insertion sort) ===")
hasil_rating = urutkan_barang_sesuai_rating(data_produk.copy())
for i, product in enumerate(hasil_rating[:10], start=1):
    print(f"{i}. {product['nama_produk']} |Rating: {product['rating']} | Harga: Rp{product['harga']:,}")