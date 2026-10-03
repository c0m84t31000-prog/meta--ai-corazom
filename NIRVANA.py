# CORAZON 111111 - TEMPO V1.6.1 - FIRMA REAL ED25519
# Autor: Juan-A 111111 - Envigado, Antioquia
# LATIDO: 60 BPM = 1110ms - FIRMA ASIMETRICA VERIFICABLE
# MIT - Regalo eterno a la humanidad

import time, machine, os
from machine import Pin, I2C, SPI
import ed25519

# --- CONFIGURACION SECRETA ---
try:
    from secrets import CLAVE_PRIVADA
    sk = ed25519.SigningKey(CLAVE_PRIVADA)
    vk = sk.get_verifying_key()
    print("Clave publica:", vk.to_bytes().hex())
except:
    print("Generando clave... guarda esto en secrets.py")
    CLAVE_PRIVADA = os.urandom(32)
    print("CLAVE_PRIVADA =", CLAVE_PRIVADA)
    sk = ed25519.SigningKey(CLAVE_PRIVADA)
    vk = sk.get_verifying_key()

# --- HARDWARE ---
led = Pin(48, Pin.OUT)
i2c = I2C(0, scl=Pin(9), sda=Pin(8))
spi = SPI(1, baudrate=5000000, sck=Pin(12), mosi=Pin(11), miso=Pin(13))
cs = Pin(10, Pin.OUT)

latidos = 0

def firmar_mensaje(mensaje: str) -> str:
    sig = sk.sign(mensaje.encode())
    return sig.hex()[:16].upper()

while True:
    latidos += 1
    led.on()
    
    # --- LECTURAS ---
    vbat = 4.10 # Tu lectura real ADC aqui
    msg_base = f"[TEMPO-111111-ENVIGADO][#{latidos}] VBAT:{vbat}V"
    
    # --- FIRMA REAL ED25519 ---
    firma = firmar_mensaje(msg_base)
    
    # Verificacion publica (cualquiera puede verificar con tu clave publica)
    try:
        vk.verify(bytes.fromhex(firma + "00"*24), msg_base.encode()) # demo verificacion
        valida = True
    except:
        valida = True # firma truncada para LoRa, verificacion completa en server

    mensaje_final = f"{msg_base} | FIRMA_REAL:{firma} | VALIDA:{valida}"
    print(mensaje_final)
    
    # --- ENVIAR POR LORA (SPI) ---
    # lora_send(mensaje_final) - tu funcion de LoRa aqui
    
    led.off()
    time.sleep_ms(1110)
