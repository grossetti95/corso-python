def manipola_lista():
    # Lista di 15 numeri da manipolare
    numeri = list(range(1, 16))
    print(f"Lista originale: {numeri}\n")
    # 1: Estrazione con slicing
    # a) Primi 5 elementi
    primi_5 = numeri[:5]
    # b) Ultimi 5 elementi
    ultimi_5 = numeri[-5:]
    