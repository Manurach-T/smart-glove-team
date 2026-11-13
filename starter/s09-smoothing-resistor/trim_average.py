# ครั้งที่ 9 — ⭐⭐⭐ ตัดหัวตัดท้ายก่อนเฉลี่ย (รันบนคอมด้วย Local Python 3 หรือใน sim ก็ได้)
#
# ตัวเลข 5 ตัวนี้คือ 5 ครั้งแรกที่ sim อ่านได้ (สัญญาณรบกวน "น้อย" · แถบงอ 0% · ค่าจริง 1422)
# ตัวที่ 2 (1572) คือ "ค่ากระโดด" · เฉลี่ยธรรมดายังโดนมันดึงขึ้นไปเป็น 1453
# แก้: ตัดตัวมากสุด 1 ตัว กับตัวน้อยสุด 1 ตัวทิ้งก่อน แล้วเฉลี่ยที่เหลือ

READINGS = [1414, 1572, 1415, 1440, 1428]
TRUE_VALUE = 1422


def average(values):
    """ค่าเฉลี่ยธรรมดา (เหมือน read_average ใน smooth.py แต่รับ list)"""
    total = 0
    for value in values:
        total = total + value
    return total // len(values)


# ⭐⭐⭐ TODO: รวมทุกตัว แล้วลบตัวมากสุดกับตัวน้อยสุดออก หารด้วยจำนวนที่เหลือ (len − 2)
def trimmed_average(values):
    """ค่าเฉลี่ยหลังตัดตัวมากสุด 1 ตัว และตัวน้อยสุด 1 ตัวทิ้ง · values ต้องมีอย่างน้อย 3 ตัว"""
    return 0


print("เฉลี่ยธรรมดา:", average(READINGS), "ห่างค่าจริง", average(READINGS) - TRUE_VALUE)
print("ตัดหัวตัดท้าย:", trimmed_average(READINGS), "ห่างค่าจริง", trimmed_average(READINGS) - TRUE_VALUE)
