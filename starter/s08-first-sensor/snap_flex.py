# ครั้งที่ 8 · การบ้าน ⭐⭐ (โจทย์รวมคาบ 7 + 8) — กดปุ่มแล้วจดค่า flex
#
# วงจร: flex ที่ D0 (คาบ 8) · ปุ่มกด ขาหนึ่ง → D10 · อีกขา → GND (คาบ 7)
# กดปุ่ม 1 ครั้ง = จดค่า 1 บรรทัด · กดค้างไว้ก็จดครั้งเดียว
# ใบ้: เปิด count_press.py คาบ 7 ดูคู่กัน · นี่คือจุดเริ่มของ "สอนคำใหม่" ในเฟส 2 (ทำท่าค้าง แล้วกดปุ่มเก็บค่า)

from machine import ADC, Pin
import time

FLEX_PIN = 1
BUTTON_PIN = 9          # D10 บน XIAO = GPIO9
STRAIGHT_LIMIT = 1900
BENT_LIMIT = 2500
WAIT = 0.05             # รอให้ปุ่มหยุดเด้ง (sim ทำปุ่มเด้งเหมือนของจริง)

flex = ADC(Pin(FLEX_PIN))
flex.atten(ADC.ATTN_11DB)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)   # ไม่กด = 1 · กด = 0


def flex_state(value):
    """เหมือน flex_state.py ที่ทำในคาบ"""
    if value < STRAIGHT_LIMIT:
        return "เหยียด"
    elif value < BENT_LIMIT:
        return "งอครึ่ง"
    else:
        return "งอสุด"


count = 0
was_pressed = False     # รอบที่แล้วกดอยู่ไหม

while True:
    pressed = button.value() == 0
    # ⭐⭐ TODO: ถ้าเพิ่งกดลงไป (รอบนี้กด แต่รอบที่แล้วไม่กด)
    #            อ่านค่า flex · เพิ่ม count ทีละ 1 · print("ครั้งที่", count, value, flex_state(value))
    #            แล้วอย่าลืมจำ pressed ไว้ใน was_pressed ให้รอบหน้า
    time.sleep(WAIT)

# ทดสอบใน sim: ลากแถบไว้ 0% กดปุ่ม → ครั้งที่ 1 1422 เหยียด · ลากไป 100% กดปุ่ม → ครั้งที่ 2 2786 งอสุด
# กดค้างไว้นาน ๆ ต้องขึ้นแค่บรรทัดเดียว
