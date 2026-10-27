lowb =  1700
higb = 2000
thumb = int(input("thumb val"))
index = int(input("index val"))
mid = int(input("middle val"))
if thumb < 0 or thumb > 4095 or index < 0 or index > 4095 or mid < 0 or mid > 4095:
    print("invalid")
#display val
print("thumb val: ", thumb)
print("index val: ", index)
print("middle val: ", mid)
#thumb val
if thumb < lowb:
    thumb = str("stra")
elif thumb < higb:
    thumb = str("semi")
else:
    thumb = str("bent")
#index val
if index < lowb:
    index = str("stra")
elif index < higb:
    index = str("semi")
else:
    index = str("bent")
#mid val
if mid < lowb:
    mid = str("stra")
elif mid < higb:
    mid = str("semi")
else:
    mid = str("bent")
# ACTUAL TEST
if thumb == "stra" and index == "stra" and mid == "stra":#stop
    print("program says: stop")
elif thumb == "stra" and index == "bent" and mid == "bent":#yes
    print("program says: yes")
elif thumb == "bent" and index == "bent" and mid == "bent":#no
    print("program says: no")
elif thumb == "stra" and index == "bent" and mid == "stra":#this
    print("program says: that one")
elif thumb == "bent" and index == "stra" and mid == "stra":#toilet
    print("program says: toilet")
elif thumb == "bent" and index == "bent" and mid == "stra":#self made
    print("program says: fuck you  nigger go die in a house fire you losy piece of shit. Your purpose in life is nothing, you serve zero purpose, you should KILL YOUSELF NOW!!!!!")
elif thumb == "bent" and index == "stra" and mid == "semi":#gojo
    print("program says: DOMAIN EXPANSION: INFINITE VOID")
elif thumb == "stra" and index == "stra" and mid == "bent":#gun
    print("program says: GUN")
else:
    print("uhhhh I'll write the code it  later.")