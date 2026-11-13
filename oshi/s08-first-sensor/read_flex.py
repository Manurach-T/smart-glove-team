# ครั้งที่ 8 — อ่านค่า flex sensor ตัวแรก (รันบนบอร์ด)
#
# วงจรแบ่งแรงดัน: 3V3 → ตัวต้านทานคงที่ → ขา D0 → flex → GND
# งอมาก → ความต้านทานของ flex มาก → แรงดันที่ D0 มาก → ตัวเลขมาก (ตรงกับใจ: งอ = ค่าขึ้น)

from machine import ADC, Pin
import time

FLEX_PIN = 1      # D0 บน XIAO = GPIO1 · ต้องเป็น ADC1 (GPIO 1–10) เพราะ ADC2 ใช้ไม่ได้ตอนเปิด WiFi
WAIT = 0.2        # วินาที อ่าน 5 ครั้งต่อวินาที พอให้อ่านตัวเลขบนจอทัน

flex = ADC(Pin(FLEX_PIN))
flex.atten(ADC.ATTN_11DB)   # ให้วัดได้เกือบเต็ม 3.3 V · ตัวเลขออกมาเป็น 0–4095

while True:
    # ⭐ TODO: อ่านค่าจาก flex ด้วย flex.read() เก็บในตัวแปร value แล้ว print ออกมา (2 บรรทัด)
    value = flex.read()
    print(value)
    time.sleep(WAIT)

# ทดสอบ: เหยียดนิ้ว ค่าต่ำ · งอนิ้ว ค่าสูงขึ้น
# ลอง: Thonny เมนู View → Plotter จะเห็นตัวเลขเป็นกราฟ
