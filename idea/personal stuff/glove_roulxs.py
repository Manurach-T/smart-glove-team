lowb =  1700
higb = 2000
def stance(fing):
    if fing < lowb:
        return "stra"
    elif fing < higb:
        return "semi"
    else:
        return "bent"
def sign(thumb,index,mid):
    if thumb == "stra" and index == "stra" and mid == "stra":#stop
        return "program says: stop"
    elif thumb == "stra" and index == "bent" and mid == "bent":#yes
        return "program says: yes"
    elif thumb == "bent" and index == "bent" and mid == "bent":#no
        return "program says: no"
    elif thumb == "stra" and index == "bent" and mid == "stra":#this
        return "program says: that one"
    elif thumb == "bent" and index == "stra" and mid == "stra":#toilet
        return "program says: toilet"
    elif thumb == "bent" and index == "bent" and mid == "stra":#self made
        return "program says: fuck you  nigger go die in a house fire you losy piece of shit. Your purpose in life is nothing, you serve zero purpose, you should KILL YOUSELF NOW!!!!!"
    elif thumb == "bent" and index == "stra" and mid == "semi":#gojo
        return "program says: DOMAIN EXPANSION: INFINITE VOID"
    elif thumb == "stra" and index == "stra" and mid == "bent":#gun
        return "program says: GUN"
    else:
        return("uhhhh I'll write the code for it later.")
thumb = int(input("thumb val"))
index = int(input("index val"))
mid = int(input("middle val"))
thumb = stance(thumb)
index = stance(index)
mid = stance(mid)
print(sign(thumb,index,mid))