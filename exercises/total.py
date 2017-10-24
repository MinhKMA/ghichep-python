# Nhập vào dãy số . Tính tổng và giá trị trung bình của dãy số 

x = 0
t = [0]
total = 0
while True:
    x += 1
    print('Nhap vao so thu {0}: '.format(x))
    n = float(input())
    if n == 'done':
        break
    t.append(float(n))
print('Loadinggggggggggg\n\n')
for i in t:
    total = total + i
    # total += i
average = total/x
print('Total',total)
print('average',average)
