# ครั้งที่ 8 · การบ้าน ⭐ (โจทย์รวมคาบ 7 + 8) — งอนิ้วแล้วไฟติด
#
# วงจร (งาน "การบ้านคาบ 8 ปุ่ม + flex" ใน sim):
#   flex แบบคาบ 8: 3V3 → ตัวต้านทาน 47k → D0 → flex → GND
#   LED แบบคาบ 7:  D2 → ตัวต้านทาน 220 → ขา A (ขายาว) → ขา C → GND
# ใบ้: เปิด button.py คาบ 7 ดูคู่กัน โครงเหมือนกันเกือบทุกบรรทัด

from machine import ADC, Pin
import time

FLEX_PIN = 1      # D0 บน XIAO = GPIO1 (คาบ 8)
LED_PIN = 3       # D2 บน XIAO = GPIO3 (คาบ 6–7)
BENT_LIMIT = 2500 # ตั้งแต่ค่านี้ขึ้นไป = งอสุด (เกณฑ์เดียวกับ flex_state.py)

flex = ADC(Pin(FLEX_PIN))
flex.atten(ADC.ATTN_11DB)
led = Pin(LED_PIN, Pin.OUT)

while True:
    # ⭐ TODO: อ่านค่า flex เก็บใน value
    #          ถ้า value ตั้งแต่ BENT_LIMIT ขึ้นไป ให้ไฟติด ไม่อย่างนั้นให้ไฟดับ
    time.sleep(0.05)

# ทดสอบใน sim: ลากแถบงอนิ้วไป 100% ไฟติด · กลับมา 0% ไฟดับ · 50% (≈ 2337) ไฟยังดับ
