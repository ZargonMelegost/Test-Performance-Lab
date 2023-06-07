
with open("file1.txt") as file_1:
    cx, cy = map(float, file_1.readline().split())
    radius = float(file_1.readline())

with open("file2.txt") as file2:
    counter = 0
    for line in file2:
        line = line.replace("\n", "")
        counter += 1
        px, py = map(float, line.split())
        if counter >= 100:
            raise ValueError("Количество точек от 1 до 100, превышено количенство точек")


        distance = ((px - cx) ** 2 + (py - cy) ** 2) ** 0.5
        if distance == radius:
            print(0)
        elif distance < radius:
            print(1)
        else:
            print(2)