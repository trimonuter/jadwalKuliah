def pangkat(a, b):
  hasil = 1
  for i in range(b):
    hasil *= a
  return hasil

basis = int(input("Masukkan basis: "))
eksp = int(input("Masukkan eksponen: "))

print(f"Hasil pangkat: {pangkat(basis, eksp)}")