# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
counter = 0
total_height = 0
for each_student_height in student_heights:
    total_height += each_student_height
    counter += 1
average_height = round(total_height / counter)
print(average_height)
