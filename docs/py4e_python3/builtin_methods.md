

# Special Method Names

## Basics

- methods `__str__` được gọi khi bạn thực hiện lệnh `print(x)`

VD:

```sh
In [2]: x = 5

In [3]: print(x)
5

In [4]: x.__str__()
Out[4]: '5'
```

## Classes That Act Like Iterators

|You Want…|So You Write…|And Python Calls…|
|---------|-------------|-----------------|
|to iterate through a sequence|iter(seq)|seq.__iter__()|
|to get the next value from an iterator|next(seq)|seq.__next__()|
|to create an iterator in reverse order|reversed(seq)|seq.__reversed__()|

VD: một vòng lặp for có thể hoạt động trên một Iterator.

```sh
for x in seq:
    print(x)
```

Python3 sẽ gọi đến `seq.__iter__()` để tạo một iterator, sau đó gọi tới method `__next__()` để lấy từng giá trị của x và method tăng lên đến khi raises a stopIteration exception
 
## Computed Attributes

|You Want…|So You Write…|And Python Calls…|
|---------|-------------|-----------------|
|to get a computed attribute(unconditionally)|x.my_property|x.__getattribute__('my_property')|
|to get a computed attribute(fallback)|x.my_property|x.__getattr__('my_property')|
|to set an attribute|x.my_property = value|x.__setattr__('my_property', value)|
|to delete an attribute|del x.my_property|x.__delattr__('my_property')|
|to list all attributes and methods|dir(x)|x.__dir__()|


- Python sẽ gọi phương thức __getattr__ bất cứ khi nào bạn yêu cầu một thuộc tính chưa được xác định.

VD:

```sh
In [19]: class foo():
   ....:     def __init__(self,a,b):
   ....:         self.a=a
   ....:         self.b=b
   ....:         

In [20]: x = foo(2,3)

In [21]: print(x.a)
2

In [22]: print(x.b)
3

In [23]: print(x.c)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-23-5fc46a94f9bf> in <module>()
----> 1 print(x.c)

AttributeError: 'foo' object has no attribute 'c'
```

- Bây giờ Count lớp của tôi đã __getattr__ 

```sh
In [38]: class foo():
   ....:     def __init__(self,a,b):
   ....:         self.a=a
   ....:         self.b=b
   ....:     def __getattr__(self, c):
   ....:         self.__dict__[item]=0
   ....:         return 0
   ....:     

In [39]: x = foo(2,3)

In [40]: print(x.a)
2

In [41]: print(x.b)
3

In [42]: print(x.c)
0
```
- Nếu bạn có method __getattribute__ trong class python sẽ gọi tới method này kể cả nó có tồn tại hay không 

```sh
In [56]: class foo():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.c=0
    def __getattribute__(self, item):
        if item == 'c':
            raise AttributeError
        return object.__getattribute__(self,item)
   ....:     

In [57]: x = foo(2,3)

In [58]: x.c
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-58-c4cfefbee49a> in <module>()
----> 1 x.c

<ipython-input-56-77b0eacb105a> in __getattribute__(self, item)
      6     def __getattribute__(self, item):
      7         if item == 'c':
----> 8             raise AttributeError
      9         return object.__getattribute__(self,item)
     10 

AttributeError: 
```

## Classes That Act Like Functions

|You Want…|So You Write…|And Python Calls…|
|---------|-------------|-----------------|
|to get a value by its key|x[key]|x.__getitem__(key)|
|to set a value by its key|x[key] = value|x.__setitem__(key, value)|
|to delete a key-value pair|del x[key]|x.__delitem__(key)|
|to provide a default value for missing keys|x[nonexistent_key]|x.__missing__(nonexistent_key)|


VD: Hiển thị value của key 

```sh
In [13]: a['minh']
Out[13]: 20
```
Tương đương

```sh
In [14]: a.__getitem__('minh')
Out[14]: 20
```

VD: Gán value cho key 

``a['Duyen'] = 20``

Tương đương 

``a.__setitem__('Duyen',20)``

VD: Xóa cặp key:value

``del a['Duyen']``

Tương đương 

``a.__delitem__('Duyen')``

## Classes That Can Be Compared

|You Want…|So You Write…|And Python Calls…|
|---------|-------------|-----------------|
|equality|x == y|x.__eq__(y)|
|inequality|x != y|x.__ne__(y)|
|less than|x < y|x.__lt__(y)|
|less than or equal to|x <= y|x.__le__(y)|
|greater than|x > y|x.__gt__(y)|
|greater than or equal to|x >= y|x.__ge__(y)|

## Classes That Can Be Serialized

|You Want…|So You Write…|And Python Calls…|
|---------|-------------|-----------------|
|to serialize an object (new pickling protocol)|pickle.dump(x, file, protocol_version)|x.__reduce_ex__(protocol_version)|

VD:  

```sh
In [32]: a = {'minh' : 20, 'duyen' : 20}

In [33]: import json

In [34]: with open('/home/minhkma/test.json', 'w') as f:
   ....:     json.dump(a, f, json)
   ....:     
```

```sh
cat /home/minhkma/test.js
{"minh": 20, "duyen": 20}
```

## Classes That Act Like Functions
|You Want…|So You Write…|And Python Calls…|
|---------|-------------|-----------------|
|to “call” an instance like a function|my_instance()|my_instance.__call__()|


VD: __call__

```sh
In [15]: class foo():
   ....:     def __call__(self,a):
   ....:         print(a)
   ....:         

In [16]: a = foo()

In [17]: a(5)
5
```

VD: __init__

```sh
In [60]: class foo():
   ....:     def __init__(self,a):
   ....:         print(a)
   ....:         

In [61]: x = foo(5)
5
```
