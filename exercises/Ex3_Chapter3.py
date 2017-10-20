# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the
# score is out of range, print an error message. If the score is between 0.0 and 1.0,
# print a grade using the following table:


#    Score  Grade
#    >= 0.9  A
#    >= 0.8  B 
#    >= 0.7  C
#    >= 0.6  D
#    < 0.6   F

=========================================

x = float(input('Enter score:'))
while not 0 <= x <= 1:
    print('Input again')
    x = float(input('Enter score:'))
if x < 0.6:
    print('F')
elif 0.6 <= x < 0.7:
    print('D')
elif 0.7 <= x < 0.8:
    print('C')
elif 0.8 <= x < 0.9:
    print('B')
else:
    print('A')
