def algortima():
    print("Mengurutkan data dengan algorimata Selection sort: Tinggi badan siswa...")
    tinggi = [180, 130, 140, 100, 120]
    print(f'data tinggi awal: {tinggi}')
    
    n = len(tinggi)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if tinggi[j] < tinggi[min_index]:
                min_index = j
        tinggi[i], tinggi[min_index] = tinggi[min_index], tinggi[i]
        
    print(f'data tinggi akhir: {tinggi}')
    
algortima()