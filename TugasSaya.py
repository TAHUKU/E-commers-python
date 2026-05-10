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
            "nomer": i + 1,
            "kategori" : random.choice(kategori_list),
            "product_id": f"PRD-{i:04d}",
            "nama_produk": f"Produk-{i}",
            "harga": random.randint(10, 200) * 1000,
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
# Mengurutkan data dari harga tertinggi ke terenda, menggunakan selection sort
# =================================================================

def selection_sort_by_price(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            # Membandingkan properti 'harga' dari objek
            if arr[j]['harga'] > arr[min_idx]['harga']:
                min_idx = j
        # Tukar seluruh objek di posisi i dengan objek di posisi min_idx
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Memuat data dari file JSON yang telah disimpan
file_name = "dataBelanja.json"
with open(file_name, 'r') as f:
    products_data_for_selection = json.load(f)
    sorted_products_by_price = selection_sort_by_price(products_data_for_selection.copy())

# PERBAIKAN PADA LOOP CETAK
print("Top 10 Produk Setelah Selection Sort (Harga Terendah):")
for i, product in enumerate(sorted_products_by_price[:10], start=1):
    # Sekarang kita panggil variabel 'product'
    print(f"{i}. {product['nama_produk']} | kategori: {product['kategori']} |Harga: Rp{product['harga']:,} | Rating: {product['rating']}")
    
def insetion_sort_by_rating(arr):
    n = len(arr)
    for i in range(1, n):
        key_item = arr[i]
        j = i - 1
        while j <= 0 and key_item['rating'] < arr[j]['rating']:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

# Memuat data dari file JSON yang telah disimpan
file_name = "dataBelanja.json"
with open(file_name, 'r') as f:
    products_data = json.load(f)
    sorted_products_by_rating = insetion_sort_by_rating(products_data.copy())

# PERBAIKAN PADA LOOP CETAK
print("\nTop 10 Produk Setelah Insertion Sort (Rating Tertinggi):")
for i, product in enumerate(sorted_products_by_rating[:10], start=1):
    print(f"{i}. {product['nama_produk']} | Rating: {product['rating']} | Harga: Rp{product['harga']:,}")