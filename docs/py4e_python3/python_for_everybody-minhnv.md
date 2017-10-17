# Python for Everybody-Exploring Data Using Python 3
## Mục lục
- [Chương 1: Why should you learn to write program?](#chuong1)
	
	+ [1.1 Computer hardware architecture](#1.1)
	+ [1.2 Understanding programming](#1.2)
	+ [1.3 Words and sentences](#1.3)
	+ [1.4 Conversing with Python](#1.4)
	+ [1.5 Terminology: interpreter and compiler](#1.5)
	+ [1.6 Writing a program](#1.6)
	+ [1.7 What is a program?](#1.7)
	+ [1.8 The building blocks of programs](#1.8)
	+ [1.9 What could possibly go wrong?](#1.9)
	+ [1.10 Glossary](#1.10)
	
<a name="chuong1"></a>	
## Chương 1

<a name="1.1"></a>
### Kiến trúc phần cứng máy tính 

- Central Processing Unit (hay CPU) : Nếu máy tính của bạn được đánh giá ở mức 3 Gigahertz có nghĩa CPU của bạn có thể thực hiện 3 tỷ phép tính trên một giây 
- Main Memory: Được sử dụng để CPU lưu trữ thông tin nhanh chóng và có tốc độ nhanh gần bằng CPU. Nhưng thông tin lưu trữ đó sẽ bị mất đi khi máy tính tắt.
- Secondary Memory: Cũng dùng để lưu trữ thông tin nhưng với tốc độ chậm hơn Main Memory và thông tin lưu trữ vẫn được giữ nguyên khi máy tính tắt. Ví dụ như ổ đĩa, USB,...
- Các thiết bị input, output như màn hình, chuột, bàn phím,... Chúng là tất cả những công cụ để ta tương tác với máy tính.
- Hầu hết các máy tính ngày nay đều có kết nối mạng để truy xuất các thông tin qua mạng.

<a name="1.2"></a>
### Hiểu chương trình

Hai kỹ năng để trở thành một lập trình viên 

- Đầu tiên bạn phải biết về ngôn ngữ lập trình và hiểu ngôn ngữ lập trình và ngữ pháp của nó.  
- Thứ hai bạn phải xây dựng được ý tưởng để giải quyết các vấn để của bài toán

<a name="1.3"></a>
### Words and sentences

Các reserved words trong python dùng để giao tiếp với python:

|-----|-----|--------|-----|------|
| and | del | global | not | with |
| as | elif | if | or | yield |
| assert | else | import | pass |
| break | except | in | raise |
| class | finally | is | return |
| continue | for | lambda | try |
| def | from | nonlocal | while |

**Lưu ý: khi đặt tên biến là tránh đặt trùng với các từ khóa của Python**

Sử dụng `print` để in ra màn hình một chuỗi ký tự:

``print('Hello world!')``

<a name="1.4"></a>
### Làm việc với python

- Trước tiên bạn phải cài đặt phần mềm python và tìm cách khởi động nó trên máy tính của bạn 
- Tại terminal hoặc command windows bạn gõ 'python':

```sh
Python 3.5.1 (v3.5.1:37a07cee5969, Dec 6 2015, 01:54:25)
[MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Dấu nhắc ``>>>``là trình thông dịch của Python để hỏi bạn, "Bạn muốn gì python làm gì tiếp theo? "Python đã sẵn sàng để tương tác với bạn. 

Ví dụ:

```sh
>>> print('Hello world!')
Hello world!
>>> print 'We will have a feast tonight unless you say
File "<stdin>", line 1
print 'We will have a feast tonight unless you say
^
SyntaxError: Missing parentheses in call to 'print'
>>>
```

Bạn sẽ nhận được một thông báo khi thực hiện sai cứ pháp

<a name="1.5"></a>
### Thuật ngữ: thông dịch viên và trình biên dịch

- CPU hiểu được một ngôn ngữ gọi là ngôn ngữ máy và được biểu diễn bằng 0 và 1 nhưng cú pháp của nó thì phức tạp hơn nhiều so với python. Vì vậy có rất ít người lập trình viết bằng ngôn ngữ máy. Thay vào đó, chúng tôi xây dựng các dịch giả khác nhau để cho phép các lập trình viết các ngôn ngữ bậc cao như Python hay JavaScript và những người dịch này sẽ chuyển đổi các chương trình này sang ngôn ngữ thực thi bằng ngôn ngữ máy bằng CPU.

- Các chương trình được viết bằng ngôn ngữ cấp cao được các máy tính có thể hiểu được bằng cách sự dụng một thông dịch hoặc biên dịch lại mã để tạo một phiên bản ngôn ngữ máy.

- Những dịch giả ngôn ngữ lập trình này chia thành hai loại chính: phiên dịch và trình biên dịch.

- Python là một thông dịch viên và khi chúng ta đang chạy Python tương tác, chúng ta có thể gõ một dòng lệnh Python (một câu) và Python xử lý nó ngay lập tức và đã sẵn sàng cho chúng ta để gõ một dòng khác của Python.

- Một số dòng Python nói với Python rằng bạn muốn nó nhớ một số giá trị cho sau này. Chúng ta cần chọn tên cho giá trị đó để nhớ và chúng ta có thể sử dụng tên biểu tượng đó để lấy giá trị sau đó. Chúng tôi gọi nó là biến 

Ví dụ 

```sh
>>> x = 6
>>> print(x)
6
>>> y = x * 7
>>> print(y)
42
>>>
```

- Một trình biên dịch cần phải được giao toàn bộ chương trình trong một tập tin, và sau đó nó chạy một quá trình để dịch các mã nguồn cao cấp vào máy ngôn ngữ và sau đó trình biên dịch đặt ngôn ngữ máy kết quả vào một tệp cho sau đó thực hiện.

- Trình thông dịch Python được viết bằng một ngôn ngữ cấp cao được gọi là "C".

Hiểu nôm na thì biên dịch là dịch một lần hết toàn bộ mã nguồn của một chương trình còn thông dịch là chạy đến câu lệnh nào thì dịch câu lệnh đó. Ví dụ cổ điển là thông dịch giống như một thông dịch viên dịch tiếng Việt sang tiếng Anh cho một người nước ngoài trong khi giao tiếp trực tiếp, khi họ nghe đến câu nào thì dịch đến câu đó, còn biên dịch giống như dịch một cuốn sách, sau khi dịch toàn bộ cuốn sách mới đem tới cho người đọc.( tham khảo thêm từ ngoài)

<a name="1.6"></a>
### Viết một chương trình

- Khi chúng ta muốn viết một chương trình, chúng ta sử dụng một trình soạn thảo văn bản để viết các lệnh Python vào một tệp, được gọi là kịch bản. Theo quy ước, các tập lệnh Python có tên kết thúc bằng .py.

- Để thực thi kịch bản, bạn phải thông báo cho trình thông dịch Python tên của tệp:

```sh
python <name.py>
```

<a name="1.7"></a>
### Thế nào là một chương trình ?

- Định nghĩa của một chương trình ở mức cơ bản nhất của nó là một chuỗi các câu lệnh Python đã được tạo ra để làm điều gì đó.

- Một ví dụ về tìm từ lặp lại nhiều lần trong một đoạn văn sau: "the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car"

```sh
name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
	if bigcount is None or count > bigcount:
	bigword = word
	bigcount = count

print(bigword, bigcount)
```

<a name="1.8"></a>
### The building blocks of programs

- Input: Nhập dữ liệu từ bên ngoài như bàn phím hay tập tin hoặc GPS...

- Output: Hiển thị kết quả của chương trình trên màn hình hoặc lưu trữ chúng trong một tệp hoặc có thể ghi vào một thiết bị.

- Sequential execution: Thực hiện các câu lệnh theo thứ tự chúng gặp phải trong kịch bản.

- Conditional execution: Kiểm tra các điều kiện nhất định trước khi thực hiện hay bỏ qua chúng.

- Repeated execution: Thực hiện một số báo cáo lặp đi lặp lại thường sử dụng với biến.

- Reuse: Viết một chú thích, hướng dẫn và gán cho nó một cái tên. Sử dụng lại khi cần trong suốt chương trình của bạn. 

<a name="1.9"></a>
### What could possibly go wrong?

- Syntax errors: Đây là những lỗi đầu tiên bạn sẽ thực hiện và cách dễ nhất để khắc phục. Một SyntaxError nghĩa là có thể bạn đã mặc lỗi về cú pháp 

- Logic errors: Lỗi logic là khi chương trình của bạn có cú pháp tốt nhưng có một sai lầm trong thứ tự của các câu lệnh thực thi hoặc các câu lệnh thực thi không gắn kết với nhau.

- Semantic errors : Lỗi ngoại lệ. Ví dụ như bạn viết một chương trình máy tính bỏ túi gồm các chức năng cộng trừ nhân chia. Thoạt nhìn có vẻ như rất đơn giản, chỉ cần yêu cầu người dùng nhập vào 2 số và phép tính, thực hiện phép tính rồi trả lại kết quả cho người dùng. Nhưng chương trình này sẽ báo lỗi nếu người dùng thực hiện một phép tính chia với số chia là 0. Đó là loại lỗi chỉ xảy ra trong khi chương trình chạy.

<a name="10"></a>
### Chú thích

- bug: Một lỗi trong chương trình.

- high-level language: Một ngôn ngữ lập trình bậc cao gần gũi với ngôn ngữ con người.

- prompt: Khi một chương trình hiển thị một thông báo và tạm dừng cho người dùng gõ một số nhập vào chương trình.

 
## Chương 3: Conditional execution

### 3.1 Boolean expressions

Một biểu thức boolean là một biểu thức đúng hoặc sai. Ví dụ: 

```sh
>>> 5 == 5
True
>>> 5 == 6
False
```

True và False là giá trị đặc biệt thuộc class bool chứ chúng không phải là một chuỗi 

```sh 
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```

Toán tử `==` là một trong những toán tử so sánh. Ngoài ra có: 

```sh 
x != y	#x không bằng y  
x > y	#x lớn hơn y
x < y	#x nhỏ hơn y
x >= y	#x lớn hơn hoặc bằng y
x <= y  #x nhở hơn hoặc bằng y
x is y	#x giống y
x is not y #x không giống y
```

### 3.2 Logical operators

Có 3 loại toán tử logic là and, or và not 

``x > 0 and x < 10``

là True khi x nằm trong khoảng từ 0 đến 10

``n%2 == 0 or n%3 == 0``

là True khi một trong hai biểu thức đúng. Tức là n chia hết cho 2 hoặc 3

Cuối cùng toán tử not phủ nhận một biểu thức boolean. Vì thế nếu not (x>y) là True nếu x < y

### 3.3 Conditional execution

Ví dụ đơn giản của câu lệnh if 

```sh
if x > 0 :
    print('x is positive')
```

Biểu thức boolean sau if gọi là điều kiện và kết thúc câu lệnh bằng dấu `:` và câu lệnh thực thi sau đó thụt vào 4 dấu cách

Nếu điều kiện True thì thực hiện câu lệnh thực thi trong if ( nhưng khối lệnh thụt vào ) Nếu False thì sẽ bỏ qua khối lệnh đó   

### 3.4 Alternative execution

Hình thức thứ hai của câu lệnh if trong đó có hai khả năng. Ví dụ:

```sh
if x%2 == 0 :
    print('x is even')
else :
	print('x is odd')
```

Nếu x chia hết cho 2 thì in ra mà hình `x is even` và ngược lại sẽ in ra màn hình `x is odd`

### 3.5 Chained conditionals

Đôi khi có nhiều hơn hai khả năng

```sh
if x < y:
	print('x is less than y')
elif x > y:
	print('x is greater than y')
else:
	print('x and y are equal')
```

Nếu biểu thức `x < y` là True thì in ra màn hình `x is less than y`. Nếu `x < y` là False thì thực hiện kiểm tra biểu thức `x > y`. Nếu `x < y` laf True thì sẽ in ra màn hình `x is greater than y` ngược lại thì sẽ là trường hợp cuối cùng `x and y are equal`

Không có giới hạn về số lượng các câu lệnh elif. 

### 3.6 Nested conditionals

Một điều kiện cũng có thể đặt trong điều kiện khác. Ví dụ 

```sh
if x == y:
	print('x and y are equal')
else:
	if x < y:
		print('x is less than y')
	else:
		print('x is greater than y')
```

Toán tử logic cung cấp một cách để đơn giản hóa các câu lệnh có điều kiện đặt lồng trong nhau:

```sh
if 0 < x:
	if x < 10:
		print('x is a positive single-digit number.')
```

Có thể thay bằng:

```sh
if 0 < x and x < 10:
	print('x is a positive single-digit number.')
```

### 3.7 Catching exceptions using try and except

Đây là một chương trình qui đổi từ độ F sang độ Catching

```sh
inp = input('Enter Fahrenheit Temperature: ')
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)
```

Nếu chạy chương trình này và kiểu biến đầu vào không hợp lệ thì nó sẽ báo lỗi

```sh
python fahren.py
Enter Fahrenheit Temperature:72
22.22222222222222

python fahren.py
Enter Fahrenheit Temperature:fred
Traceback (most recent call last):
  File "fahren.py", line 2, in <module>
    fahr = float(inp)
ValueError: could not convert string to float: 'fred'
```

try và except được dùng để xử lý các lỗi ngoại lệ 

```sh
inp = input('Enter Fahrenheit Temperature:')
try:
	fahr = float(inp)
	cel = (fahr - 32.0) * 5.0 / 9.0
	print(cel)
except:
	print('Please enter a number')
```

Python bắt đầu bằng cách thực hiện chuỗi các câu lệnh trong khối try. Nếu không có lỗi gì nó sẽ bỏ qua khối except. Còn lại nếu khối try xảy ra lỗi Python sẽ thực thi câu lệnh trong khối except

Kết quả:

```sh
python fahren2.py
Enter Fahrenheit Temperature:72
22.22222222222222


python fahren2.py
Enter Fahrenheit Temperature:fred
Please enter a number
```

## Chương 5: Iteration

### Updating variables

Một mô hình phổ biến trong các câu lệnh gán là câu lệnh gán để cập nhật một biến, trong đó giá trị mới của biến phụ thuộc vào biến cũ.

``x = x + 1``

Điều này có nghĩa là "lấy giá trị hiện tại của x cộng 1 và sau đó cập nhật giá trị mới của x."

Nếu bạn cố gắng cập nhật một biến không tồn tại nó sẽ báo lỗi. Bởi vì chưa gán một giá trị cho biến đó.

```sh
>>> x = x + 1
NameError: name 'x' is not defined
```

Trước khi bạn có thể cập nhật một biến, bạn phải khởi tạo nó:

```sh
x = 0 
x = x + 1
```

### The while statement

```sh
n = 5
while n > 0:
	print(n)
	n = n - 1
print('Blastoff!')
```

Đây là một chương trình đếm ngược từ 5 đến 1 và in ra màn hình `Blastoff`

Nó có nghĩa là, "hiển thị giá trị của n và sau đó giảm giá trị của n đi giá trị bằng 1 cho đến khi giá trị của n > 0. Khi n = 0 thì dừng vòng lặp và hiển thị `Blastoff` "

Quá trình làm việc trong vòng lặp while

- 1.Đánh giá các điều kiện: True hay False
- 2.Nếu điều kiện là False, thoát vòng lặp while và tiếp tục thực hiện câu lệnh tiếp theo
- 3.Nếu điều kiện là đúng, thực hiện khối lệnh trong while và sau đó quay trở lại bước 1

### Infinite loops

Ví dụ một lòng lặp vô hạn:

```sh
n = 10
while True:
	print(n, end=' ')
	n = n - 1
print('Done!')
```

Ví dụ: giả sử bạn muốn nhập dữ liệu từ người dùng cho đến khi chúng ta nhập `done`

```sh
while True:
	line = input('> ')
	if line == 'done':
		break
	print(line)
print('Done!')
```

Vòng lặp sẽ kết thúc khi gặp `break`

Kết quả:

```sh 
> hello there
hello there
> finished
finished
> done
Done!
```

### Finishing iterations with continue

Đôi khi bạn đang lặp lại một vòng lặp và muốn kết thúc vòng lặp lại hiện tại và ngay lập tức nhảy tới lần lặp kế tiếp

Trong trường hợp đó, bạn có thể sử dụng câu lệnh continue để bỏ qua lần lặp kế tiếp mà không cần hoàn thành phần thân của vòng lặp cho lần lặp hiện tại.

Dưới đây là ví dụ về một vòng lặp sao chép dữ liệu đầu vào của nó cho đến khi người dùng nhập "done", nhưng dòng bắt đầu bằng kí tự # sẽ không được in ra màn hình:

```sh
while True:
	line = input('>
	if line[0] == '#
		continue
	if line == 'done
		break
	print(line)
print('Done!')
```

Kết quả:

```sh
> hello there
hello there
> # don't print this
> print this!
print this!
> done
Done!
```

Tất cả các dòng được in ngoại trừ một trong những bắt đầu với dấu # bởi vì khi continue được thực thi nó kết thúc vòng lặp hiện tại và chuyển sang vòng lặp tiếp theo nên sẽ bỏ qua lệnh print sau nó.

### Definite loops using for

Đôi khi chúng ta muốn lặp lại một loạt những thứ như một danh sách các từ, các dòng trong một tập tin, hoặc một danh sách các con số... Chúng ta có thể sử dụng vòng lặp xác định for

Chúng ta sử dụng vòng lặp while là một vòng lặp không xác định bởi vì nó chỉ đơn giản là vòng lặp cho đến khi một điều kiện trở thành Sai, trong khi vòng lặp for lặp lại qua một tập hợp các mục được biết đến để nó chạy qua nhiều lần lặp vì có các mục trong tập hợp.

Cú pháp của một vòng lặp for tương tự với vòng lặp while trong đó có một `statement` và một `loop body`

```sh
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
	print('Happy New Year:', friend)
print('Done!')
```

Trong đó 

Kết quả:

```sh
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
Done!
```

