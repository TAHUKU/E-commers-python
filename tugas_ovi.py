import json
import random

# ==============================================================
# MEMBUAT DATA RANDOM
# ==============================================================
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


# Membuat data sampel
sample_data_count = 500
generated_data = get_sample_data(sample_data_count)

# Menyimpan ke file JSON
file_name = "dataBelanja.json"

with open(file_name, 'w') as f:
    json.dump(generated_data, f, indent=4)

print(f"Data sampel ({sample_data_count} produk) telah disimpan ke '{file_name}'.")


# ==============================================================
# SORTING GABUNGAN
# PRIORITAS:
# 1. Rating tertinggi ke terendah
# 2. Jika rating sama -> harga tertinggi ke terendah
# ==============================================================

def combined_sort(arr):
    n = len(arr)

    # Menggunakan Selection Sort
    for i in range(n):
        max_idx = i

        for j in range(i + 1, n):

            # Bandingkan rating
            if arr[j]['rating'] > arr[max_idx]['rating']:
                max_idx = j

            # Jika rating sama, bandingkan harga
            elif (
                arr[j]['rating'] == arr[max_idx]['rating']
                and
                arr[j]['harga'] > arr[max_idx]['harga']
            ):
                max_idx = j

        # Tukar data
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr


# ==============================================================
# MEMUAT DATA JSON
# ==============================================================

with open(file_name, 'r') as f:
    products_data = json.load(f)


# ==============================================================
# MENJALANKAN SORTING
# ==============================================================

sorted_products = combined_sort(products_data.copy())


# ==============================================================
# MENAMPILKAN HASIL
# ==============================================================

print("\nTop 20 Produk Setelah Sorting Gabungan")
print("(Rating Tertinggi & Harga Tertinggi)\n")

for product in sorted_products[:20]:
    print(
        f"{product['nama_produk']} "
        f"| Rating: {product['rating']} "
        f"| Harga: Rp{product['harga']:,}"
    )