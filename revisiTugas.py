import json
import random
import os

# =================================================================
# 1. FUNGSI UTILITAS (Data Management)
# =================================================================

def generate_sample_data(num=500):
    """Menghasilkan dataset produk acak."""
    dataset = []
    for i in range(num):
        dataset.append({
            "product_id": f"PRD-{i:04d}",
            "nama_produk": f"Produk-{i}",
            "harga": random.randint(10, 500) * 1000,
            "rating": round(random.uniform(1.0, 5.0), 1)
        })
    return dataset

def save_to_json(data, filename):
    """Menyimpan data ke file JSON."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"✅ Data berhasil disimpan ke '{filename}'\n")

def load_from_json(filename):
    """Memuat data dari file JSON."""
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as f:
        return json.load(f)

# =================================================================
# 2. ALGORITMA PENGURUTAN (Sorting Algorithms)
# =================================================================

def selection_sort_by_price(arr):
    """
    Mengurutkan produk berdasarkan HARGA (Ascending).
    Metode: Mencari nilai terkecil dan menukarnya ke depan.
    """
    data = arr.copy()  # Gunakan copy agar data asli tidak berubah
    n = len(data)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j]['harga'] < data[min_idx]['harga']:
                min_idx = j
        
        # Swap (Tukar posisi)
        data[i], data[min_idx] = data[min_idx], data[i]
        
    return data

def insertion_sort_by_rating(arr):
    """
    Mengurutkan produk berdasarkan RATING (Descending).
    Metode: Menyisipkan elemen ke posisi yang tepat seperti menyusun kartu.
    """
    data = arr.copy()
    for i in range(1, len(data)):
        key_item = data[i]
        j = i - 1
        
        # Geser elemen yang lebih kecil ke kanan
        while j >= 0 and key_item['rating'] > data[j]['rating']:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key_item
        
    return data

# =================================================================
# 3. FUNGSI DISPLAY
# =================================================================

def display_products(products, title, limit=5):
    """Menampilkan daftar produk ke konsol dengan format rapi."""
    print(f"--- {title} ---")
    for p in products[:limit]:
        print(f"ID: {p['product_id']} | {p['nama_produk']:<10} | "
              f"Harga: Rp{p['harga']:>7,} | Rating: {p['rating']}")
    print("-" * 50 + "\n")

# =================================================================
# MAIN EXECUTION
# =================================================================

if __name__ == "__main__":
    FILE_NAME = "dataBelanja.json"

    # Tahap 1: Persiapan Data
    raw_data = generate_sample_data(500)
    save_to_json(raw_data, FILE_NAME)

    # Tahap 2: Load Data
    products = load_from_json(FILE_NAME)

    if products:
        # Tahap 3: Sorting Harga (Selection Sort - Terendah)
        sorted_by_price = selection_sort_by_price(products)
        display_products(sorted_by_price, "TOP 5 HARGA TERENDAH (Selection Sort)")

        # Tahap 4: Sorting Rating (Insertion Sort - Tertinggi)
        sorted_by_rating = insertion_sort_by_rating(products)
        display_products(sorted_by_rating, "TOP 5 RATING TERTINGGI (Insertion Sort)")