"""
問1

ある学校の授業の時間割が与えられる。
一つの教室で同時にできる授業は一つまで。
学校に教室は最低幾つ必要か？
[(開始時間, 終了時間), ...]

"""

classes1 = [(0, 50), (50, 100)]
answer1 = 1

classes2 = [(0, 50), (50, 100), (25, 75)]
answer2 = 2

classes3 = [(10, 50), (20, 30), (60, 100), (70, 90)]
answer3 = 2

classes4 = [(900, 910), (940, 12000), (950, 1120), (1100, 1130), (1500, 1900), (1800, 2000)]
answer4 = 3

def overlaps(a, b):
  return b[0] < a[0] and a[0] < b[1]

def solution(classes):
  num_classes = len(classes)
  max_rooms = 1
  for i in range(num_classes):
    rooms = 1
    for j in range(num_classes):
      if i == j:
        continue
      if overlaps(classes[i], classes[j]):
        rooms += 1
        max_rooms = max(max_rooms, rooms)
      
  return max_rooms

assert solution(classes1) == answer1
assert solution(classes2) == answer2
assert solution(classes3) == answer3
assert solution(classes4) == answer4
print('ok')