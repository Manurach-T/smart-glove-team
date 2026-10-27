# ครั้งที่ 4 — ย้ายกฎจำท่า 3 นิ้วจาก three_fingers.py มาเป็นฟังก์ชัน
#
# เดิมกฎชุดนี้ถูกคัดลอกไปไว้ทั้งใน three_fingers.py และ glove_log.py
# ถ้าจะเปลี่ยนเกณฑ์ต้องแก้สองที่ ตอนนี้ย้ายมาไว้ที่นี่ที่เดียว ไฟล์อื่น import ไปใช้
#
# ไฟล์นี้มีแต่ def กด Run แล้วไม่มีอะไรขึ้น = ปกติ
# ทดสอบใน Shell หลังกด Run เช่น  finger_state(1900)  หรือ  gesture_name(1310, 2395, 2410)

STRAIGHT_LIMIT = 1700   # ต่ำกว่านี้ = เหยียด
BENT_LIMIT = 2200       # ตั้งแต่ค่านี้ขึ้นไป = งอสุด


# ⭐ TODO 1: คืนคำว่า "เหยียด" / "งอครึ่ง" / "งอสุด" ตามเกณฑ์ข้างบน
#           ใช้ return แทน print
def finger_state(value):
    if value < STRAIGHT_LIMIT:
        print("straight")
        return "straight"
    elif value >= BENT_LIMIT:
        return "full bent"
        print("full bent")
    elif STRAIGHT_LIMIT <= value < BENT_LIMIT:
        return "half bent"
        print("half bent")
        


# ⭐⭐ TODO 2: เรียก finger_state กับทั้ง 3 นิ้ว แล้วใช้กฎ 5 ท่าเดิมจาก three_fingers.py
#            คืนคำของท่า หรือ "?" ถ้ามีนิ้วงอครึ่ง หรือไม่ตรงท่าไหนเลย
#   ไม่ = งอสุด งอสุด งอสุด          หยุด = เหยียด เหยียด เหยียด
#   ใช่ = เหยียด งอสุด งอสุด         อันนี้ = งอสุด เหยียด งอสุด
#   ห้องน้ำ = งอสุด เหยียด เหยียด    (เรียงเป็น โป้ง ชี้ กลาง)
def gesture_name(thumb_value, index_value, middle_value):
    """คืนคำของท่า 3 นิ้ว หรือ "?" ถ้าไม่แน่ใจ"""
    return "?"


# ทดสอบใน Shell:
#   finger_state(1699) → เหยียด    finger_state(1700) → งอครึ่ง    finger_state(2200) → งอสุด
#   gesture_name(2310, 2405, 2398) → ไม่      gesture_name(1310, 2395, 2410) → ใช่
#   gesture_name(2315, 1335, 1355) → ห้องน้ำ  gesture_name(1300, 1900, 2400) → ?
