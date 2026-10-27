# ครั้งที่ 4 — เกมหาบั๊กฟังก์ชัน
#
# ไฟล์นี้มีบั๊ก 4 จุด
#   บั๊ก 1–3 ไม่มีตัวแดงเลย แต่ผลที่พิมพ์ออกมาผิด
#   บั๊ก 4 ขึ้นตัวแดง
# 1. กด Run แล้วเทียบกับ "ต้องได้" ท้ายแต่ละบรรทัด จดว่าบรรทัดไหนผิด
# 2. หาว่าผิดเพราะเครื่องไหน แก้ทีละจุด แล้วรันซ้ำจนถูกครบ 4 บรรทัด

BENT_LIMIT = 2200
ADC_MAX = 4095


def to_percent(value):
    """แปลงค่า 0–4095 เป็นเปอร์เซ็นต์ (ปัดเป็นจำนวนเต็ม)"""
    percent = round(value * 100 / ADC_MAX)


def count_bent(values):
    """นับนิ้วที่งอ (ตั้งแต่ BENT_LIMIT ขึ้นไป)"""
    count = 0
    for value in values:
        if value >= BENT_LIMIT:
            count = count + 1
        return count


def need_more(value, limit):
    """ต้องงออีกเท่าไรถึงเกณฑ์ (limit ลบ value)"""
    return limit - value


def say(word):
    """คืนประโยคที่ถุงมือจะพูด"""
    print("ถุงมือพูดว่า: " + word)


print(to_percent(4095))                    # ต้องได้ 100
print(count_bent([2500, 1300, 2600]))      # ต้องได้ 2
print(need_more(BENT_LIMIT, 1900))         # ต้องได้ 300 (นิ้วอยู่ที่ 1900 ต้องงออีกเท่าไร)
sentence = say("ใช่")
print(sentence + "!")                      # ต้องได้ ถุงมือพูดว่า: ใช่!
