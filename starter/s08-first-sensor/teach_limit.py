# ครั้งที่ 8 · การบ้าน ⭐⭐⭐ (โจทย์รวมคาบ 7 + 8) — ใช้ปุ่มสอนเกณฑ์ให้บอร์ด
#
# วงจร: flex ที่ D0 · ปุ่มที่ D10 · LED ที่ D2 (ครบ 3 ชิ้น)
# ทำไม: เกณฑ์ 2500 ตั้งจาก sim · ของจริงและมือแต่ละคนได้ค่าไม่เท่ากัน → ให้ผู้ใช้สอนเกณฑ์เอง
#   กดครั้งที่ 1 = จำค่าตอนเหยียด · กดครั้งที่ 2 = จำค่าตอนงอ
#   เกณฑ์ = ค่ากลางระหว่างสองค่านั้น → งอเกินเกณฑ์ ไฟติด
# ใบ้: ใช้วิธี "เพิ่งกดลงไป" จาก count_press.py และวิธีเปิดปิดไฟจาก flex_led.py ⭐

from machine import ADC, Pin
import time

FLEX_PIN = 1
BUTTON_PIN = 9
LED_PIN = 3
WAIT = 0.05

flex = ADC(Pin(FLEX_PIN))
flex.atten(ADC.ATTN_11DB)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
led = Pin(LED_PIN, Pin.OUT)

step = 0                # 0 = รอจำค่าเหยียด · 1 = รอจำค่างอ · 2 = สอนเสร็จแล้ว ใช้งานได้
straight_value = 0
bent_value = 0
limit = 0
was_pressed = False

print("เหยียดนิ้ว แล้วกดปุ่ม")
while True:
    value = flex.read()
    pressed = button.value() == 0
    # ⭐⭐⭐ TODO:
    #   1. ถ้าเพิ่งกดลงไป และ step เป็น 0 → จำ value ไว้ใน straight_value · step = 1 · print บอกให้งอนิ้ว
    #   2. ถ้าเพิ่งกดลงไป และ step เป็น 1 → จำ value ไว้ใน bent_value
    #      limit = ค่ากลางของ straight_value กับ bent_value (ใช้ // 2 ให้ได้จำนวนเต็ม) · step = 2 · print เกณฑ์
    #   3. ถ้า step เป็น 2 → value ตั้งแต่ limit ขึ้นไป ไฟติด ไม่อย่างนั้นไฟดับ
    #   4. จำ pressed ไว้ใน was_pressed
    time.sleep(WAIT)

# ทดสอบใน sim: แถบ 0% กดปุ่ม → แถบ 100% กดปุ่ม → เกณฑ์ ≈ 2104 · ลากแถบไปมา ตัวเลขถึงเกณฑ์ไฟติด (50% ≈ 2337 ก็ติดแล้ว)
