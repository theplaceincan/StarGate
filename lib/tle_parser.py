
LINE_1 = "1 25544U 98067A   26302.56368278  .00005507  00000-0  10765-3 0  9997"
LINE_2 = "2 25544  51.6333 355.1294 0007050 324.3141  35.7375 15.49100842592585"            

print(len(LINE_1))
print(len(LINE_2))

line_1_split = LINE_1.split()
line_2_split = LINE_2.split()

print(line_1_split)
print(line_2_split)