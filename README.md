# 🔍 Port Scanner

This script is used to scan a range of user-defined ports on a host.
It reports which ports are open or closed.
Its design is simple and readable.

🌍 Available languages | [ESPAÑOL](README.es.md) 🔁 [ENGLISH](README.md) 

## ✨ Features
- User inputs: host and port range.
- Shows the result of each port (OPEN ✅ / CLOSED ❌).
- Prints a final summary listing open ports.
- Only performs TCP scanning (no UDP).
- No services detected: only open or closed port.

## 📚 Requirements
- Python 3.x
- No extra packages required.

## 🎯 Usage
Clone the repository and run the script from the terminal:

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
