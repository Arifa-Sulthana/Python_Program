# Input a Python list of student heights
student_heights = input().split()
t_H=0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  print(student_heights)
  t_H = t_H+student_heights[n]
print("total height = "+ str(t_H))
nos=len(student_heights)
print("number of students = "+str(nos))
a_h=round(t_H/nos)
print("average height = "+str(a_h))
