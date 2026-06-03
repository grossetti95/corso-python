# Generatore tabellina
n = int(input("DI quale numero vuoi la tavola? "))

print(f"\n=== Tavola del {n} ===")
for i in range (1, 11):
    print(f"{n} x {i:<2} = {n * i}")
    
risposta = input("\n Vuoi la tavola pitagorica completa? (s/n): ")
if risposta.lower() == 's':
    print("\n=== Tavola Pitagorica ===")
    print("   ", end="")
    for i in range(1, 11):
        print(f"{i:4}", end="")
    print()
    for i in range(1, 11):
        print(f"{i:3}|", end="")
        for j in range(1, 11):
            print(f"{i * j:4}", end="")
        print()
if risposta.lower() == "n":
    print("Va bene, alla prossima!")