'''
defaultdict 란 기본값을 지정한 딕셔너리

1. defaultdict(int)

2. defaultdict(list)

3. defaultdict(set)

'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from collections import defaultdict

# 예제1. defaultict(int) 
d_dict_int = defaultdict(int)

print(d_dict_int["a"])          # a인 key 와 디폴트 value 로 0 을 준 dict 가 생성됩니다.
print(d_dict_int["b"])          # b인 key 와 디폴트 value 로 0 을 준 dict 가 생성됩니다.

print(d_dict_int)               # defaultdict(<class 'int'>, {'a': 0, 'b': 0})

d_dict_int["c"] = 100             # c인 key 와 value : 100 을 준 dict 가 생성됩니다.

print(d_dict_int)               # defaultdict(<class 'int'>, {'a': 0, 'b': 0, 'c': 100})

letters = 'dongdongfather'
d_dict_letters = defaultdict(int)

for k in letters:
    d_dict_letters[k] += 1

print(d_dict_letters)           # defaultdict(<class 'int'>, {'d': 2, 'o': 2, 'n': 2, 'g': 2, 'f': 1, 'a': 1, 't': 1, 'h': 1, 'e': 1, 'r': 1})

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 예제2. defaultdict(list)
d_dict_list = defaultdict(list)

print(d_dict_list['k1'])        # k1 인 key 와 디폴트 value 로 빈 리스트 [] 를 준 dict 가 생성됩니다.
print(d_dict_list['k2'])        # k1 인 key 와 디폴트 value 로 빈 리스트 [] 를 준 dict 가 생성됩니다.

print(d_dict_list)

d_dict_list['k3'] += 'temp1'    # k3 인 key 와 value 로 ['t', 'e', 'm', 'p', '1'] 을 준 dict 가 생성됩니다.

print(d_dict_list)              # defaultdict(<class 'list'>, {'k1': [], 'k2': [], 'k3': ['t', 'e', 'm', 'p', '1']})

name_list = [('kim', 'sungsu'), ('kang', 'hodong'), ('park', 'jisung'), ('kim', 'yuna'), ('park', 'chanho')]
d_dict_name1 = defaultdict(list)

for k, v in name_list:
    d_dict_name1[k].append(v)

print(d_dict_name1)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 예제3. defaultdict(set)
d_dict_set = defaultdict(set)

print(d_dict_set['j1'])         # j1 인 key 와 디폴트 value 로 빈 사전 set() 을 준 dict 가 생성됩니다.
print(d_dict_set['j2'])         # j2 인 key 와 디폴트 value 로 빈 사전 set() 을 준 dict 가 생성됩니다.

d_dict_set['j3'] = {'temp1': 'temp2'}

print(d_dict_set)

name_list = [('kim', 'sungsu'), ('kang', 'hodong'), ('park', 'jisung'), ('kim', 'yuna'), ('park', 'chanho')]
d_dict_name2 = defaultdict(set)

for k, v in name_list:
    d_dict_name2[k].add(v)

print(d_dict_name2)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''