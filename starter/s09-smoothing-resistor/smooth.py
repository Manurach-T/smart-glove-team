# ครั้งที่ 9 — ทำค่าให้นิ่ง: อ่านหลายครั้งแล้วเฉลี่ย
# วงจรเดิมคาบ 8 · ใน sim เปิด "สัญญาณรบกวน" ที่การ์ดของ flex ก่อน
# ลอง COUNT = 1 / 5 / 20 แล้วดูว่า 10 บรรทัดแกว่งกว้างแค่ไหน

from machine import ADC, Pin
import time

FLEX_PIN = 1      # D0
COUNT = 5         # อ่านกี่ครั้งแล้วเฉลี่ย
LINES = 10        # พิมพ์ 10 บรรทัดแล้วจบ
WAIT = 0.2        # วินาที

flex = ADC(Pin(FLEX_PIN))
flex.atten(ADC.ATTN_11DB)


# ⭐ TODO: อ่าน count ครั้ง บวกเก็บไว้ใน total แล้วหารด้วย count
def read_average(count):
    """อ่าน flex count ครั้งติดกัน แล้วคืนค่าเฉลี่ย (จำนวนเต็ม)"""
    # ตอนนี้อ่านครั้งเดียว (เหมือน COUNT = 1) → แก้ให้วน count ครั้ง
    return flex.read()


for line in range(LINES):
    print(read_average(COUNT))
    time.sleep(WAIT)
