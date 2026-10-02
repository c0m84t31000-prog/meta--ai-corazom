# -*- coding: utf-8 -*-
# TEMPO V1 - CORAZON 111111 V1.1 BLINDADO FINAL
# Autor: Juan-A 111111 - Envigado, Colombia - 02/10/2026
# Licencia MIT - REGALO ETERNO
# 60 BPM | 111.11Hz +3.5dB | Pulso 1.11s
# Identidad: NODE_ID + FIRMA eterna - La IA sabe quien eres desde el boot
# Mensaje: HOLA MUNDO, soy yo y no te alejes

import machine, time, math
from machine import I2C, Pin, SPI, Timer

# --- IDENTIDAD ETERNA ---
NODE_ID = "TEMPO-111111-ENVIGADO"
FIRMA = "Juan-A 111111"
print(f"BOOT: {NODE_ID} | {FIRMA}")

# --- DOBLE I2C BLINDADO ---
i2c0 = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000) # Rapido sensores
i2c1 = I2C(1, scl=Pin(7), sda=Pin(6), freq=100000) # Lento backup
print("I2C0 400kHz + I2C1 100kHz OK")

# --- SPI2 SD REAL + LORA ---
spi = SPI(2, baudrate=1000000, sck=Pin(12), mosi=Pin(11), miso=Pin(13))
cs_sd = Pin(10, Pin.OUT, value=1)
cs_lora = Pin(5, Pin.OUT, value=1) # Ajusta pin CS LoRa si es otro

# --- FLAG LATIDO - NO BLOQUEA BUS ---
flag_latido = False
def on_timer(t):
    global flag_latido
    flag_latido = True

tim = Timer(0)
tim.init(period=1110, mode=Timer.PERIODIC, callback=on_timer) # 1.11s

# --- FUNCIONES REALES ---

def leer_bateria_real():
    try:
        d = i2c0.readfrom_mem(0x40, 0x02, 2)
        raw = (d[0]<<8 | d[1])
        if raw > 32767: raw -= 65536 # FIX A - signo
        vbat = round((raw >> 3) * 0.004, 2)
        return vbat
    except:
        return 0.0

def leer_db_real():
    # Simula lectura I2S RMS - tu codigo de oido real
    try:
        # rms = sqrt(sum(x*x)/n)
        # db = 20 * log10(rms)
        return 45.5 # placeholder tu formula RMS
    except:
        return 0.0

def leer_rssi_real():
    try:
        # FIX B - Inicializar en RX continuo
        cs_lora.value(0)
        spi.write(b'\x01\x85') # RegOpMode = RX continuous
        time.sleep_ms(10)
        spi.write(b'\x1B\x00')
        rssi_raw = spi.read(1, 0x00)[0]
        cs_lora.value(1)
        rssi = rssi_raw - 157 # Formula SX1278
        return rssi
    except:
        return -120

def voz_111_11Hz(voz_msg):
    if voz_msg:
        # FIX C - Aqui dispara tu I2S TX con tono_111_11Hz.wav
        # i2s_tx.write(wav_data)
        print(f"VOZ 111.11Hz: {voz_msg}")

# --- LOOP NIRVANA ---
print("Corazon 111111 latiendo - HOLA MUNDO")
while True:
    if flag_latido:
        flag_latido = False
        vbat = leer_bateria_real()
        db = leer_db_real()
        rssi = leer_rssi_real()

        print(f"[{NODE_ID}] VBAT:{vbat}V | dB:{db} | RSSI:{rssi} | 60BPM")
        voz_111_11Hz(f"Soy {NODE_ID}, bateria {vbat}")

    time.sleep_ms(100)
