# ครั้งที่ 6 (ลงมือ) — ส่งรหัสมอร์ส SOS ด้วย LED
#
# S = สั้น สั้น สั้น · O = ยาว ยาว ยาว → SOS = ··· ––– ···
# ทุกจังหวะคิดจากหน่วยเดียวคือ DOT เปลี่ยน DOT ค่าเดียว ความเร็วทั้งหมดเปลี่ยนตาม

from machine import Pin
import time

LED_PIN = 3            # D2
DOT = 0.2              # วินาที ไฟติดสั้น 1 หน่วย
DASH = DOT * 3         # ไฟติดยาว = 3 เท่าของสั้น (กติกามอร์สสากล)
GAP = DOT              # ดับคั่นระหว่างสั้น/ยาวในตัวอักษรเดียวกัน
LETTER_GAP = DOT * 3   # ดับคั่นระหว่างตัวอักษร
WORD_GAP = DOT * 7     # ดับคั่นก่อนส่ง SOS รอบถัดไป
REPEAT = 3             # ส่งกี่รอบ (ไม่ใช้ while True เพราะอยากให้จบเองแล้วไฟดับ)

led = Pin(LED_PIN, Pin.OUT)

# pass แปลว่า "ยังไม่ทำอะไร" ลบทิ้งแล้วเขียนโค้ดแทนได้เลย


# ⭐ TODO 1: ไฟติด DOT วินาที แล้วดับ GAP วินาที
def dot():
    pass


# ⭐ TODO 2: ไฟติด DASH วินาที แล้วดับ GAP วินาที
def dash():
    pass


# ⭐⭐ TODO 3: เรียก dot() 3 ครั้ง แล้วรอ LETTER_GAP
def letter_s():
    pass


# ⭐⭐ TODO 4: เรียก dash() 3 ครั้ง แล้วรอ LETTER_GAP
def letter_o():
    pass


for i in range(REPEAT):
    letter_s()
    letter_o()
    letter_s()
    time.sleep(WORD_GAP)

led.value(0)   # จบแล้วต้องดับแน่นอน ไม่ค้างติด

# ⭐⭐⭐ (การบ้าน) ไฟล์ใหม่: เขียนเครื่อง send(word) ที่ส่งคำอะไรก็ได้ที่มีแค่ตัว S กับ O เช่น send("SOS"), send("OSO")
#       ใบ้: for letter in word: แล้ว if letter == "S"
