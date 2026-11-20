# ครั้งที่ 11 — ⭐ อ่าน flex 3 นิ้วพร้อมกัน (รันใน sim ก่อน แล้วรันบนถุงมือจริงด้วยโค้ดเดิม)
#
# ในกล่องบนหลังมือคือวงจรแบ่งแรงดันแบบคาบ 8 นิ้วละ 1 ชุด: 3V3 → ตัวต้านทาน 20 kΩ → ขา D → flex → GND
# คาบ 8 อ่าน 1 นิ้วด้วยตัวแปร flex ตัวเดียว · วันนี้เก็บเลขขาไว้ใน list แล้ววนสร้าง ADC ทีละนิ้ว

from machine import ADC, Pin
import time

FINGERS = ["โป้ง", "ชี้", "กลาง"]
FLEX_PINS = [9, 4, 3]     # D10 D3 D2 = GPIO 9 4 3 ตามวงจรในกล่องถุงมือ (F1 F2 F3) · อยู่บน ADC1 ทั้งหมด (GPIO 1–10)
WAIT = 0.2                # วินาที

flexes = []               # ADC ของแต่ละนิ้ว เรียงตาม FINGERS

# ⭐ TODO 1: วนตาม FLEX_PINS · ทุกขา สร้าง ADC(Pin(ขา)) ตั้ง .atten(ADC.ATTN_11DB) แล้ว append ใส่ flexes (4 บรรทัด)
for pin in FLEX_PINS:
    flex = ADC(Pin(pin))
    flex.atten(ADC.ATTN_11DB)   # ตัวเลข 0–4095 เหมือนคาบ 8
    flexes.append(flex)


# ⭐ TODO 2: อ่านทุกตัวใน flexes ด้วย .read() เก็บใส่ values ทีละตัว แล้วคืน values
def read_all():
    """ตัวเลขของทุกนิ้ว เรียงตาม FINGERS เช่น [2275, 3102, 3413]"""
    values = []
    for flex in flexes:
        values.append(flex.read())
    return values


while True:
    print(read_all())     # print ทั้ง list → ใน sim กดปุ่ม "กราฟ" จะเห็น 3 เส้น (1 เส้นต่อ 1 นิ้ว)
    time.sleep(WAIT)

# ทดสอบใน sim: โป้ง 0% · ชี้ 50% · กลาง 100% → [2275, 3102, 3413] (ตัวต้านทาน 20 kΩ เหมือนในกล่อง)
# ถุงมือจริง: ตัวเลขไม่เท่า sim (flex จริงแต่ละตัวต่างกัน) แต่ต้องงอนิ้วไหนแล้วตัวเลขช่องนั้นขึ้น