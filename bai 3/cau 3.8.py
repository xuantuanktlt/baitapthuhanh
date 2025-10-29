import math
pos = [0, 0]
while True:
    s = input("Nhập hướng di chuyển (ví dụ: UP 5), hoặc Enter để dừng: ")
    if not s:  
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        print("Hướng di chuyển không hợp lệ!")
distance = math.sqrt(pos[0]**2 + pos[1]**2)
print("Khoảng cách từ vị trí hiện tại đến (0,0) là:", int(round(distance)))
