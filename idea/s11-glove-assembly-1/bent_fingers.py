FINGERS = ["โป้ง", "ชี้", "กลาง"]
LIMIT = 2844

# ⭐⭐ TODO: วนทีละช่อง ช่องไหนตัวเลขเกิน limit ให้ append ชื่อนิ้วช่องเดียวกัน (names[i]) ใส่ result
def bent_fingers(values, names, limit):
    """[2275, 3102, 3413] → ["ชี้", "กลาง"]"""
    result = []
    for i in range(len(values)):
        if values[i] > limit:
            result.append(names[i])
    return result

for values in [[2275, 2275, 2275], [2275, 3102, 3413], [3413, 3413, 3413]]:
    print(values, "งอ:", bent_fingers(values, FINGERS, LIMIT))