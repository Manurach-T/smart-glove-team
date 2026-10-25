# ครั้งที่ 5 — ทบทวน def: ฟังก์ชันเหมือน f(x) ในวิชาคณิต
#
# วิชาคณิต: f(x) = 2x + 1  →  f(3) = 2(3) + 1 = 7
# Python:   def f(x):
#               return 2 * x + 1
#           f(3) ถูก "แทนที่" ด้วยค่าที่ return คือ 7
#
# ไฟล์นี้มีแต่ def กด Run แล้วไม่มีอะไรขึ้น = ปกติ ทดสอบใน Shell ตามค่าท้ายไฟล์
# ทุกเครื่องต้อง return ห้าม print ในเครื่อง
# ต้องวางไว้โฟลเดอร์เดียวกับ glove_rules.py (คาบ 4) เพราะข้อสุดท้าย import ไปใช้

from glove_rules import finger_state

PASS_SCORE = 50


# ⭐ TODO 1: f(x) = 2x + 1
def f(x):
    return 0


# ⭐ TODO 2: พื้นที่สี่เหลี่ยม = กว้าง × ยาว
def area(width, height):
    return 0


# ⭐⭐ TODO 3: คืน True ถ้า score ถึง PASS_SCORE ไม่ถึงคืน False
def is_pass(score):
    return False


# ⭐⭐ TODO 4: คืนค่าที่มากกว่า ห้ามใช้ max
def bigger(a, b):
    return 0


# ⭐⭐⭐ TODO 5: ผลรวมทุกค่าใน values ห้ามใช้ sum
def total(values):
    return 0


# ⭐⭐⭐ TODO 6: คืน list สภาพของทุกนิ้ว เรียก finger_state ทีละค่าแล้ว append
def states(values):
    return []


# ทดสอบใน Shell:
#   f(3) → 7          f(0) → 1          f(3) + f(1) → 10
#   area(4, 5) → 20
#   is_pass(50) → True     is_pass(49) → False
#   bigger(3, 8) → 8       bigger(8, 3) → 8
#   total([2010, 2060, 1985]) → 6055     total([]) → 0
#   states([1300, 1900, 2400]) → ['เหยียด', 'งอครึ่ง', 'งอสุด']
