import json
import random

def data_barang(num=200):
    kategori_list = ["Elektronik", "Pakaian", "Buku"]
    dataset = []
    for i in range(num):
        dataset.append({
            "nomer": i + 1,
            "kategori": random.choice(kategori_list),
            "product_id": f"PRD-{i:04d}",
            "nama_produk": f"Produk-{i}",
            "harga": random.randint(5, 500) * 1000,
            "rating": round(random.uniform(1.0, 5.0), 1)
        })
    return dataset

data_awal = data_barang(200)
with open("data_produk.json", "w") as f:
    json.dump(data_awal, f, indent=4)

# discending harga tertinggi ke terendah
def urutkan_barang_sesuai_harga(arr): 
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j]['harga'] > arr[max_idx]['harga']:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

# Ascending terendah ke tertinggi
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

with open("data_produk.json", "r") as f:
    data_produk = json.load(f)

print("\n" + "="*70)
print("TOP 10 PRODUK - HARGA TERTINGGI KE TERENDAH")
print("="*70)
hasil_harga = urutkan_barang_sesuai_harga(data_produk.copy())
for i, p in enumerate(hasil_harga[:10], 1):
    print(f"{i:2}. {p['nama_produk']:15} | {p['kategori']:12} | Rp{p['harga']:12,} | {p['rating']}")

print("\n" + "="*70)
print("TOP 10 PRODUK - RATING TERENDAH KE TERTINGGI")
print("="*70)
hasil_rating = urutkan_barang_sesuai_rating(data_produk.copy())
for i, p in enumerate(hasil_rating[:10], 1):
    print(f"{i:2}. {p['nama_produk']:15} | {p['kategori']:12} | {p['rating']} | Rp{p['harga']:12,}")
print("="*70)