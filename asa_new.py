import json
import random

# =====================================================
# MEMBUAT DATA PRODUK
# =====================================================
def generate_produk(jumlah=20):

    produk = []

    harga_awal = 100000
    rating_awal = 5.0

    for i in range(1, jumlah + 1):

        item = {
            "product_id": i,
            "nama_produk": f"Produk_{i}",

            # Harga selalu naik
            "harga": harga_awal + (i * 100000),

            # Rating selalu turun
            "rating": round(rating_awal - (i * 0.1), 1)
        }

        produk.append(item)

    return produk


# =====================================================
# SELECTION SORT
# HARGA ASCENDING
# =====================================================
def sort_harga_ascending(data):

    panjang = len(data)

    for i in range(panjang):

        posisi_min = i

        for j in range(i + 1, panjang):

            if data[j]["harga"] < data[posisi_min]["harga"]:
                posisi_min = j

        # Tukar data
        data[i], data[posisi_min] = data[posisi_min], data[i]

    return data


# =====================================================
# INSERTION SORT
# RATING DESCENDING
# =====================================================
def sort_rating_descending(data):

    for i in range(1, len(data)):

        current = data[i]
        j = i - 1

        while j >= 0 and data[j]["rating"] < current["rating"]:

            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = current

    return data


# =====================================================
# GENERATE DATA
# =====================================================
data_produk = generate_produk(100)


# =====================================================
# SIMPAN FILE JSON
# =====================================================
with open("produk.json", "w") as file:
    json.dump(data_produk, file, indent=4)


# =====================================================
# SORT HARGA ASCENDING
# =====================================================
data_harga = data_produk.copy()
hasil_harga = sort_harga_ascending(data_harga)


# =====================================================
# AMBIL 10 DATA DENGAN:
# HARGA ASCENDING + RATING DESCENDING
# =====================================================
top10 = []

last_rating = 5.1

for produk in hasil_harga:

    # Rating harus lebih kecil dari sebelumnya
    if produk["rating"] <= last_rating:

        top10.append(produk)

        last_rating = produk["rating"]

    if len(top10) == 10:
        break


# =====================================================
# OUTPUT
# =====================================================
print("\n")
print("=" * 70)
print("   TOP 10 PRODUK (HARGA ASCENDING + RATING DESCENDING)")
print("=" * 70)

print(f"{'No':<5} {'Nama Produk':<20} {'Harga':<18} {'Rating'}")
print("-" * 70)

for no, produk in enumerate(top10, start=1):

    print(
        f"{no:<5}"
        f"{produk['nama_produk']:<20}"
        f"Rp {produk['harga']:<15,}"
        f"{produk['rating']}"
    )

print("=" * 70)
print("Sorting selesai dilakukan.")