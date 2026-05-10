def algoritma():
    print("Algoritma Insertion sort: nomer antrian")
    antrian = [5, 20, 10, 12, 33]
    print(f'data awal {antrian}')
    
    for i in range(1, len(antrian)):
        key = antrian[i]
        j = i - 1
        while j >= 0 and key < antrian[j]:
            antrian[j + 1] = antrian[j]
            j -= 1
        antrian[j + 1] = key
        
    print(f'data akhir {antrian}')
    
algoritma()