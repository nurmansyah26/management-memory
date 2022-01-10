#5200411001 Ratna Rochmanningrum
#5200411013 Ulul Rahmawati Putri
#5200411094 Yusi Erlita
#5200411260 Muhammad Nurmansyah

print("============MANAJEMEN MEMORI==============")
print("============MULTIPROGRAMING==============")
ram = int(input("Kapasitas RAM (MBps) : "))
so = int(input("Sistem Operasi yang dipakai (MBps) : "))
prog1 = int(input("Kapasitas Program 1 : "))
prog2 = int(input("Kapasitas Program 2 : "))
prog3 = int(input("Kapasitas Program 3 : "))

totalprog = (prog1 + prog2 + prog3)
sisa = (ram - (so + totalprog))

print("==================")
print("=======Output======")
print("Kapasitas RAM = ",ram,"MBps")
print("Sistem Operasi yang dipakai = ",so,"MBps")
print("Kapasitas Program 1 =",prog1,"MBps")
print("Kapasitas Program 2 :",prog2,"MBps")
print("Kapasitas Program 3 :",prog3,"MBps")
print("Total Kapasitas program 1-3 =",totalprog,"MBps")
print("Sisa Kapasitas nya adalahhh =",sisa,"MBps")

