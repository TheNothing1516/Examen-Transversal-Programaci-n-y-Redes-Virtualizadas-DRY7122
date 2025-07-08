# netconf_config_csr.py

from ncclient import manager

# Datos de conexión
router = {
    "host": "192.168.56.101",   # Cambia si es necesario
    "port": 830,
    "username": "devnet",
    "password": "cisco123",
    "hostkey_verify": False
}

# ======================================
# 1. Conexión SSH y comprobación de NETCONF
# ======================================
with manager.connect(**router) as m:
    print("✅ Conexión NETCONF establecida con el router CSR1000v")

    # ======================================
    # 2. Cambiar el nombre del router a Jimenez-Leiva
    # ======================================
    config_hostname = """
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>Jimenez-Leiva</hostname>
      </native>
    </config>
    """
    response = m.edit_config(target="running", config=config_hostname)
    print("✅ Hostname cambiado a Jimenez-Leiva")

    # 3. Crear loopback11 con IP 11.11.11.11/32
    # ======================================
    config_loopback11 = """
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <Loopback>
            <name>11</name>
            <ip>
              <address>
                <primary>
                  <address>11.11.11.11</address>
                  <mask>255.255.255.255</mask>
                </primary>
              </address>
            </ip>
          </Loopback>
        </interface>
      </native>
    </config>
    """
    response = m.edit_config(target="running", config=config_loopback11)
    print("✅ Interfaz Loopback11 creada con IP 11.11.11.11/32")
