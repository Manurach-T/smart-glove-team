t=0
i=0
m=0
r=0
l=0

st=int(input('How much is the straight threshold? '))
# usually 1700
bt=int(input('How much is the bend threshold?     '))
# usually 2200


thumb=int(input('How bending is ur thumb?            '))
if thumb<0 or thumb>4095:
    print('Error')
elif thumb<st:
    t=1
elif thumb<bt:
    t=2
else:
    t=3

index=int(input('How bending is ur index?            '))
if index<0 or index>4095:
    print('Error')
elif index<st:
    i=1
elif index<bt:
    i=2
else:
    i=3

middle=int(input('How bending is ur middle?           '))
if middle<0 or middle>4095:
    print('Error')
elif middle<st:
    m=1
elif middle<bt:
    m=2
else:
    m=3
    
ring=int(input('How bending is ur ring?             '))
if ring<0 or ring>4095:
    print('Error')
elif ring<st:
    r=1
elif ring<bt:
    r=2
else:
    r=3
    
no=int(input('How bending is ur little?           '))
if no<0 or no>4095:
    print('Error')
elif no<st:
    l=1
elif no<bt:
    l=2
else:
    l=3

# 1= straight
if t==3 and i==1 and m==1 and r==3 and l==3:
    print ('ห้องน้ำ')
elif t==3 and i==1 and m==3 and r==3 and l==3:
    print ('อันนี้')
elif t==1 and i==1 and m==1 and r==1 and l==1:
    print ('หยุด')
elif t==3 and i==3 and m==1 and r==3 and l==3:
    print ('fuck u')
elif t==1 and i==3 and m==3 and r==3 and l==3:
    print ('เยี่ยม')
elif t==3 and i==3 and m==3 and r==3 and l==3:
    print ('ไม่')
elif t==1 and i==3 and m==3 and r==3 and l==1:
    print ('โทรศัพท์')
elif t==1 and i==1 and m==1 and r==3 and l==3:
    print ('ปืน')
elif t==1 and i==1 and m==3 and r==3 and l==1:
    print ('I love u')
elif t==3 and i==3 and m==3 and r==3 and l==1:
    print ('สัญญา')
elif t==2 and i==2 and m==1 and r==1 and l==1:
    print ('OK')
elif t==3 and i==3 and m==3 and r==1 and l==3:
    print ('ขอแต่งงาน')
elif t==3 and i==1 and m==3 and r==3 and l==1:
    print ('อยากฟังเพลง')
else:
    print ('undefined')