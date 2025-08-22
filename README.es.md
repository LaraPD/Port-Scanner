# 🔍 Escáner de Puertos  

Este script permite escanear un rango de puertos definido por el usuario en un host.  
Informa qué puertos están abiertos o cerrados. Su diseño es simple y legible.  

🌍 Idiomas disponibles | [INGLÉS](README.md) 🔁 [ESPAÑOL](README.es.md) 

## ✨ Características  
- Entrada del usuario: host y rango de puertos.  
- Muestra el resultado de cada puerto (ABIERTO ✅ / CERRADO ❌).  
- Imprime un resumen final con los puertos abiertos.  
- Solo realiza escaneo TCP (no UDP).  
- No detecta servicios: únicamente muestra si el puerto está abierto o cerrado.  

## 📚 Requisitos  
- Python 3.x  
- No requiere paquetes adicionales.  

## 🎯 Uso  
Clona el repositorio y ejecuta el script desde la terminal:  

```bash
python port_scanner.py
```
❗You will be prompted for target IP and a port range

## ✍️ Example
<img width="318" height="297" alt="image" src="https://github.com/user-attachments/assets/3bc70b56-a3ba-4da8-80ac-4dab03cec727" />

## 📌 Recommendations
- Use small ranges to reduce scan time.
- Be aware that firewalls or security tools may block or log your scans.
- Increase/decrease the settimeout() value depending on network latency.
- Maybe you need administrator/root privileges to scan lower ports (<1024).

⚠️ Only scan systems you own or have explicit permission to test. Unauthorized scanning may be ILLEGAL ⚠️


