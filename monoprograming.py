#5200411001 Ratna Rochmanningrum
#5200411013 Ulul Rahmawati Putri
#5200411094 Yusi Erlita
#5200411260 Muhammad Nurmansyah

print("============MANAJEMEN MEMORI==============\n")
print("============MONOPROGRAMING==============\n")
ram = int(input("Kapasitas RAM (MBps): "))
so = int(input("Sistem Operasi yang dipakai: "))
memo = int(input("Kapasitas Memori yang dipakai: "))

sampah = ram - (so + memo)

print("=============================\n")
print("Kapasitas RAM :",ram,"MBps")
print("Sistem Operasi yang dipakai :",so)
print("Memori yang terpakai :",memo,"MBps")
print("Kapasitas Sampah memori :",sampah,"MBps")
