# 🔍 Escáner de Puertos  

Este script permite escanear un rango de puertos definido por el usuario en un host.  
Informa qué puertos están abiertos o cerrados. Su diseño es simple y legible.  

🌍 Idiomas disponibles | [INGLÉS](README.md) 🔁 [ESPAÑOL](README.es.md) 

## ✨ Características  
- Entrada del usuario: host y rango de puertos.  
- Muestra el resultado de cada puerto (CERRADO ❌ / ABIERTO ✅) e imprime un resumen final con estos últimos.  
- Solo realiza escaneo TCP.  
- No detecta servicios ya que únicamente muestra si el puerto está abierto o cerrado.  

## 📚 Requisitos  
- Python 3.x  
- No requiere paquetes adicionales.  

## 🎯 Uso  
Clona el repositorio y ejecuta el script desde la terminal:  

```bash
python port_scanner.py
```
🐍 [Ir al código](port_scanner.py)   

❗Se solicitará la dirección IP y un rango de puertos.

## ✍️ Example
<img width="318" height="297" alt="image" src="https://github.com/user-attachments/assets/3bc70b56-a3ba-4da8-80ac-4dab03cec727" />

## ⏳ Consejo (Solo Windows)
Si quieres comparar los resultados del script con la actividad de red actual en tu máquina, ejecuta en la terminal CMD:

```bash
netstat -b
```
Este comando muestra las conexiones activas y los ejecutables que las utilizan (puede requerir privilegios de administrador).

Sin embargo, si solo necesitas ver los puertos y sus estados (sin ejecutables), puedes usar:
```bash
netstat -an
```

## 📌 Recommendaciones
- Usa rangos pequeños para reducir el tiempo de escaneo.
- Ten en cuenta que los firewalls o herramientas de seguridad pueden bloquear o registrar tus escaneos.
- Ajusta el valor de settimeout() según la latencia de tu red.
- Puede que necesites privilegios de administrador/root para escanear puertos bajos (<1024).

⚠️ Escanea únicamente sistemas que sean tuyos o para los que tengas permiso expreso. El escaneo no autorizado puede ser ILEGAL ⚠️





