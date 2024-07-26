# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
# print(max(student_scores))
# print(min(student_scores))
# li=student_scores.sort(reverse=True)
# li=student_scores.sort()
# print(student_scores[-1])

# angela's code:
highScore = 0
for score in student_scores:
  if score > highScore:
    highScore=score
print(f"The highest score in the class is: {highScore}")
