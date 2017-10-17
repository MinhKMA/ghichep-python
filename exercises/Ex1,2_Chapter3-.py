#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
hourly rate for hours worked above 40 hours.

#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the
program. 

====================================================================


while True:
    try:
        hour = float(input('Enter Hours:'))
        rate = float(input('Enter Rate:'))
        break
    except:
        print('Vui long nhap mot so')
while hour < 0:
    print('vui long nhap so duong')
    hour = float(input('Enter Hours:'))
    break
while rate < 0:
    print('vui long nhap so duong')
    rate = float(input('Enter Rate:'))
    break
if hour > 40:
    x = (hour - 40) * rate * 1.5 + 40 * rate
    print ('pay:',x)
else:
    x = hour * rate
    print ('pay:',x)
