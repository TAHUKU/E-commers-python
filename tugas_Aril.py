import json
import random

# =================================================================
# MEMBUAT DATA RANDOM
# =================================================================
def get_sample_data(num=500):
    kategori_list = ["Elektronik", "Pakaian", "Buku"]
    dataset = []
    for i in range(num):
        dataset.append({
            "product_id": f"PRD-{i:04d}",
            "nama_produk": f"Produk-{i}",
            "harga": random.randint(10, 500) * 1000,
            "rating": round(random.uniform(1.0, 5.0), 1)
        })
    return dataset


# Menghasilkan dan menyimpan data sampel
sample_data_count = 500
generated_data = get_sample_data(sample_data_count)

file_name = "dataBelanja.json"
with open(file_name, 'w') as f:
    json.dump(generated_data, f, indent=4)

print(f"Data sampel ({sample_data_count} produk) telah disimpan ke '{file_name}'.")


# =================================================================
# 1. SELECTION SORT (Berdasarkan HARGA)
# =================================================================
def selection_sort_by_price(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            # Membandingkan properti 'harga' dari objek
            if arr[j]['harga'] > arr[max_idx]['harga']:
                max_idx = j
        # Tukar seluruh objek di posisi i dengan objek di posisi min_idx
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr


# Memuat data dari file JSON yang telah disimpan
file_name = "dataBelanja.json"
with open(file_name, 'r') as f:
    products_data_for_selection = json.load(f)

# Mengaplikasikan Selection Sort berdasarkan harga
sorted_products_by_price = selection_sort_by_price(products_data_for_selection.copy())

print("Top 10 Produk Setelah Selection Sort (Harga Tertinggi):")
for product in sorted_products_by_price[:10]:
    print(f" - {product['nama_produk']} | Harga: Rp{product['harga']:,} | Rating: {product['rating']}")

# =================================================================
# 2. INSERTION SORT (Berdasarkan RATING)
# =================================================================
def insertion_sort_by_rating(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        # Mengurutkan ascending (rating terendah ke tertinggi)
        while j >= 0 and key_item['rating'] < arr[j]['rating']:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr


# Memuat data dari file JSON yang telah disimpan
file_name = "dataBelanja.json"
with open(file_name, 'r') as f:
    products_data = json.load(f)

# Mengaplikasikan Insertion Sort berdasarkan rating
sorted_products_by_rating = insertion_sort_by_rating(products_data.copy())

print("Top 10 Produk Setelah Insertion Sort (Rating Terendah):")
for product in sorted_products_by_rating[:10]:
    print(f" - {product['nama_produk']} | Rating: {product['rating']} | Harga: Rp{product['harga']:,}")