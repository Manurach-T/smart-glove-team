BENDS = [0, 25, 50, 75, 100]              
VALUES = [1422, 1974, 2337, 2594, 2786]

# ⭐⭐ TODO 1: ตัวเลขเพิ่มขึ้นเท่าไรในแต่ละช่วง (ตัวถัดไป − ตัวนี้) เก็บใส่ลิสต์
def steps(values):
    """[1422, 1974, 2337] → [552, 363]"""
    result = []
    for i in range(len(values)):
        if i < len(values)-1:
            result.append(values[i+1] - values[i])
    return result

# ⭐⭐ TODO 2: หาช่วงที่ตัวเลขเพิ่มมากที่สุด คืนลิสต์ [งอเริ่ม, งอจบ] (วิธีหาค่ามากสุดแบบ most_bent คาบ 3)
def most_sensitive(bends, values):
    """ช่วงที่ไวที่สุด เช่น [0, 25]"""
    gaps = steps(values)
    best = 0
    most_gap = 0
    for i in range(len(gaps)):
        if gaps[i] > best:
            most_gap = gaps[i]
            best = i
    return [bends[best], bends[best + 1]]

# ⭐⭐ TODO 3: เหมือน TODO 2 แต่หาช่วงที่ตัวเลขเพิ่ม "น้อย" ที่สุด
def least_sensitive(bends, values):
    """ช่วงที่ไวน้อยที่สุด เช่น [75, 100]"""
    gaps = steps(values)
    best = 0
    least_gap = 0
    for i in range(len(gaps)):
        if gaps[i] < best:
            least_gap = gaps[i]
            best = i
    return [bends[best], bends[best + 1]]

print("เพิ่มทีละช่วง:", steps(VALUES))
print("ไวที่สุด:", most_sensitive(BENDS, VALUES))
print("ไวน้อยที่สุด:", least_sensitive(BENDS, VALUES))
# ผลที่ถูก: เพิ่มทีละช่วง: [552, 363, 257, 192] · ไวที่สุด: [0, 25] · ไวน้อยที่สุด: [75, 100]
