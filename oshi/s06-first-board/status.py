# ครั้งที่ 6 — ไฟสถานะของถุงมือ (รันบนบอร์ด หรือ Wokwi)
#
# ถุงมือจริงมี LED ภายนอกที่ D2 ไว้บอกผู้ใช้ว่าตอนนี้เป็นยังไง
# แต่ละสถานะคือเครื่อง 1 เครื่อง (def) เรียกชื่อเดียวรู้เลยว่าไฟจะทำอะไร
# เครื่องแบบนี้ "ลงมือทำ" (สั่งไฟ) จึงไม่ต้อง return
#
# ผลที่ถูก: ไฟติดค้าง 1 วินาที → พัก → กระพริบเร็ว 5 ครั้ง → พัก → กระพริบช้า 2 ครั้ง

from machine import Pin
import time

LED_PIN = 3      # D2
FAST = 0.1       # วินาที กระพริบเร็ว
SLOW = 0.5       # วินาที กระพริบช้า
PAUSE = 1        # พักระหว่างสถานะ ให้ตาแยกออก

led = Pin(LED_PIN, Pin.OUT)


def blink(times, delay):
    """กระพริบ times ครั้ง ติดและดับครั้งละ delay วินาที (ให้มาแล้ว จาก blink_pattern.py)"""
    for i in range(times):
        led.value(1)
        time.sleep(delay)
        led.value(0)
        time.sleep(delay)


# ⭐ TODO 1: พร้อมใช้งาน = ไฟติดค้าง 1 วินาที แล้วดับ (แก้บรรทัดข้างล่าง)
def show_ready():
    led.value(0)


# ⭐⭐ TODO 2: กำลังสอนท่าใหม่ = กระพริบเร็ว 5 ครั้ง · ใบ้: เรียก blink ใช้ FAST
def show_teaching():
    led.value(0)


# ⭐⭐ TODO 3: ไม่แน่ใจว่าเป็นท่าอะไร = กระพริบช้า 2 ครั้ง · ใช้ SLOW
def show_unsure():
    led.value(0)


show_ready()
time.sleep(PAUSE)
show_teaching()
time.sleep(PAUSE)
show_unsure()

# ⭐⭐⭐ TODO 4: เขียน def show(mode) ที่ใช้ if เลือก
#   "ready" → show_ready() · "teaching" → show_teaching() · "unsure" → show_unsure()
#   mode อื่นไม่ทำอะไรเลย
# แล้วเปลี่ยน 5 บรรทัดข้างบนเป็น show("ready") · show("teaching") · show("unsure") คั่นด้วย time.sleep(PAUSE)
