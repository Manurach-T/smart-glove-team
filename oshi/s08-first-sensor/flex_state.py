# ครั้งที่ 8 ⭐⭐ — บอกว่านิ้วเหยียด งอครึ่ง หรืองอสุด จากค่า flex
#
# เกณฑ์ตั้งจาก sim ของครู (เหยียด ≈ 1422 · งอครึ่ง ≈ 2337 · งอสุด ≈ 2786) · คาบ 10 จะวัดเกณฑ์จริงของถุงมือเรา

from machine import ADC, Pin
import time

FLEX_PIN = 1
STRAIGHT_LIMIT = 1900   # ต่ำกว่านี้ = เหยียด
BENT_LIMIT = 2500       # ตั้งแต่ค่านี้ขึ้นไป = งอสุด

flex = ADC(Pin(FLEX_PIN))
flex.atten(ADC.ATTN_11DB)


def flex_state(value):
    """แปลงตัวเลข 0–4095 เป็นคำ (เครื่องคิดเลข: ต้อง return)"""
    # ⭐⭐ TODO: คืน "เหยียด" / "งอครึ่ง" / "งอสุด" ตามเกณฑ์ข้างบน (เหมือน finger_state คาบ 2)
    return "?"


while True:
    value = flex.read()
    print(value, flex_state(value))
    time.sleep(0.2)

# ทดสอบ: 1200 → เหยียด · 1900 → งอครึ่ง · 2500 → งอสุด
