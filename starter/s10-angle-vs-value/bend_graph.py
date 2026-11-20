BENDS = [0, 25, 50, 75, 100]            
VALUES = [1422, 1974, 2337, 2594, 2786]   

def bar(value):
    return "#" * (value // 100)

for i in range(len(BENDS)):
    print(BENDS[i], "%", VALUES[i], bar(VALUES[i]))