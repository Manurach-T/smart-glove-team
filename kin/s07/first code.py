# ครั้งที่ 6 — กระพริบ LED ดวงแรก (ไฟล์นี้รันบนบอร์ด ไม่ใช่บนคอม)
#
# ต่อวงจร: ขา D2 → ตัวต้านทาน 220 โอห์ม → ขายาวของ LED (+) → ขาสั้นของ LED (−) → GND
# ตัวต้านทานจำกัดกระแสไว้ประมาณ 6 mA ถ้าไม่มี กระแสจะมากจน LED หรือขาบอร์ดเสียได้

from machine import Pin
import time

LED_PIN = [2, 3 , 4 , 5]      # ขา D2 บน XIAO คือ GPIO3 (โค้ดต้องใช้เลข GPIO ไม่ใช่ชื่อที่พิมพ์บนบอร์ด)
DELAY = 0.5      # วินาที ติดครึ่งวิ ดับครึ่งวิ

# Pin.OUT = บอร์ดเป็นฝ่ายจ่ายไฟออกขานี้ (คาบ 7 จะใช้ Pin.IN อ่านปุ่ม)
led = [Pin(LED_PIN[0], Pin.OUT),Pin(LED_PIN[1], Pin.OUT),Pin(LED_PIN[2], Pin.OUT),Pin(LED_PIN[3], Pin.OUT)]

# บอร์ดไม่มีวันจบโปรแ(กรมเอง ใช้ while True วนไปเรื่อย ๆ จนกด Stop หรือถอดสาย
while True :
    led[0].value(1)         # 1 = ขาเป็น 3.3V ไฟไหลผ่าน LED → ติด
    led[1].value(0)
    led[2].value(0)
    led[3].value(0)
    time.sleep(DELAY)    # ต้องรอ ไม่งั้นติด-ดับเร็วจนตาเห็นเป็นติดค้าง
    led[0].value(0)         # 0 = ขาเป็น 0V ไม่มีไฟไหล → ดับ
    led[1].value(1)
    led[2].value(0)
    led[3].value(0)
    time.sleep(DELAY)
    led[0].value(0)
    led[1].value(0)
    led[2].value(1)
    led[3].value(0)
    time.sleep(DELAY)
    led[0].value(0)
    led[1].value(0)
    led[2].value(0)
    led[3].value(1)
    time.sleep(DELAY)   
    led[0].value(0)         
    led[1].value(0)
    led[2].value(1)
    led[3].value(0)
    time.sleep(DELAY)
    led[0].value(0)
    led[1].value(1)
    led[2].value(0)
    led[3].value(0)
    time.sleep(DELAY)
    led[0].value(1)
    led[1].value(0)
    led[2].value(0)
    led[3].value(0)


# ลองแก้:
# 1. DELAY = 0.1 กับ DELAY = 2 ต่างกันยังไง
# 2. ถ้าลบ time.sleep บรรทัดสุดท้ายทิ้ง ไฟจะเป็นยังไง (ลองแล้วอธิบายว่าทำไม)