student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

height_sum = sum(student_heights)

average_height = height_sum / len(student_heights)

print(average_height)
