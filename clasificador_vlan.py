def clasificar_vlan(vlan):
    if 1 <= vlan <= 1005:
        return "VLAN del rango normal"
    elif 1006 <= vlan <= 4094:
        return "VLAN del rango extendido"
    else:
        return "VLAN inválida"

try:
    vlan = int(input("Ingrese número de VLAN: "))
    resultado = clasificar_vlan(vlan)
    print(f"Resultado: {resultado}")
except ValueError:
    print("Debe ingresar un número válido.")
