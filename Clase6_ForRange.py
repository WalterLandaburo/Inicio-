print("BLOQUE DE CÓDIGO")
print("for VARIABLE in SECUENCIA:")
print("")
print("")
print("")
#Datos ---------++++

clientes = ["marta", "carlos", "", "frida"]



for i in range(len(clientes)):
    if clientes[i] == "":
        print("Dato no válido")
        continue
    else:     
        print(f"Cliente {i + 1}: {clientes[i].title()}")
    