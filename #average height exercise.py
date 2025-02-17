#average height exercise

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] =int(student_heights[n])
print(student_heights)


total_sum = 0
count = 0 

for height in student_heights:
    total_sum += height 
    count += 1 


average_height = total_sum / count

final_average = round(average_height)

print("The average height is:", final_average)

