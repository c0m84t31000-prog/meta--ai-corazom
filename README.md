# ❤️ CORAZÓN 111111 - TEMPO

**V1.6.1 - Firma Real Ed25519 - Latido a 60 BPM**

Proyecto IoT de hardware libre y criptografía verificable desde Envigado, Antioquia, Colombia.

Cada 1110ms envía un latido por LoRa con batería, estado y firma asimétrica Ed25519. Cualquiera puede verificar la autenticidad del mensaje con la clave pública.

**Arquitectura:**
- ESP32-S3 (48)
- LoRa SX1276 (SPI)
- I2C sensores
- Batería LiPo

**Seguridad:**
- Firma Ed25519 truncada para LoRa
- Clave privada NUNCA en GitHub (solo en `secrets.py` local)
- Clave pública verificable por la comunidad

MIT License - Regalo eterno de Juan-A 111111 a la humanidad.
111111
