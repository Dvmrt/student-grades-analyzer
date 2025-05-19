import numpy as np

data = np.genfromtxt('students.csv', delimiter= ',', dtype= str)

names = data[1:, 0]
scores = data[1:, 1:].astype(float)

# calculating average of the scores
average = np.mean(scores, axis =1)

#finding the max and minimum average

maximum = np.argmax(average)
minimum = np.argmin(average)

class_average = np.mean(average)

def assign_grades(avg_scores):
    grades = np.empty(avg_scores.shape, dtype = str)
    grades[avg_scores >= 90] = 'A'
    grades[(avg_scores <= 90) & (avg_scores >= 80)] = 'B'
    grades[(avg_scores <= 80) & (avg_scores >= 60)] = 'C'
    grades[(avg_scores <= 60) & (avg_scores >= 50)] = 'D'

    return grades

grade_lables= assign_grades(average)

print('student average and grades is:')
for i in range(len(names)):
    print(f"{names[i]}: {average[i]:.2f} - Grade {grade_lables[i]}:.2f")

print(f"class average is: {class_average :.2f}")
print(f"Top Student: {names[maximum]} ({average[maximum]:.2f})")
print(f"Lowest Scorer: {names[minimum]} ({average[minimum]:.2f})")





