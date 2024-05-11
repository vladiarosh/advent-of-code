file = open("2015_2_input.txt")
boxes = file.read()
file.close()

lines = boxes.split('\n')
dimensions_split = [row.split("x") for row in lines]

dimensions_split_int = []
for lines in dimensions_split:
    sublist_int = [int(i) for i in lines]
    dimensions_split_int.append(sublist_int)

total_paper_length = 0
for i in dimensions_split_int:
    l = i[0]
    w = i[1]
    h = i[2]
    sides = [l*w, w*h, h*l]
    paper_length = sum(sides)*2 + min(sides)
    total_paper_length += paper_length

print("Elves need to order", total_paper_length, "square feet of paper")
