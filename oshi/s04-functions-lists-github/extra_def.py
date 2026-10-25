# เสร็จแล้วทำต่อ (def) ครั้งที่ 4 — เครื่องเล็ก ๆ ของถุงมือ 5 ข้อ ไต่ระดับ
#
# ต้องอยู่โฟลเดอร์เดียวกับ glove_rules.py (ข้อ ⭐⭐⭐ import ไปใช้) และทำ glove_rules.py เสร็จแล้ว
# ไฟล์นี้มีแต่ def กด Run แล้วทดสอบใน Shell ตามค่าท้ายไฟล์ · ทุกเครื่องต้อง return

from glove_rules import gesture_name

BENT_LIMIT = 2200
NAMES = ["โป้ง", "ชี้", "กลาง", "นาง", "ก้อย"]


# ⭐ TODO 1: คืน True ถ้า value ถึง BENT_LIMIT ไม่ถึงคืน False
def is_bent(value):
    return False


# ⭐ TODO 2: คืนชื่อนิ้วช่องที่ index · ถ้าเลขช่องไม่มีจริง (ติดลบ หรือ 5 ขึ้นไป) คืน "?"
def finger_name(index):
    return "?"


# ⭐⭐ TODO 3: คืน list ชื่อนิ้วที่งอ เรียก is_bent กับ finger_name ที่ทำไว้
def bent_names(values):
    return []


# ⭐⭐ TODO 4: คืนเลขช่องที่ค่ามากสุด (most_bent.py คาบ 3) ห้ามใช้ max
def max_index(values):
    return 0


# ⭐⭐⭐ TODO 5: a กับ b เป็น list ค่า 3 นิ้ว [โป้ง, ชี้, กลาง]
#               คืน True ถ้า gesture_name ของทั้งสองได้คำเดียวกัน
def same_gesture(a, b):
    return False


# ทดสอบใน Shell:
#   is_bent(2200) → True        is_bent(2199) → False
#   finger_name(2) → 'กลาง'     finger_name(5) → '?'
#   bent_names([1300, 2400, 2900, 1500, 2200]) → ['ชี้', 'กลาง', 'ก้อย']
#   max_index([1300, 2400, 2900, 1500, 2200]) → 2
#   same_gesture([2310, 2405, 2398], [2285, 2440, 2420]) → True    (ไม่ กับ ไม่)
#   same_gesture([2310, 2405, 2398], [1310, 2395, 2410]) → False   (ไม่ กับ ใช่)
