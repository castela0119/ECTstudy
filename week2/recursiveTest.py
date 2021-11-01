def test(n):
    if n >= 5:
        print('탈출중입니다.')
        return
    else:
        print(f'현재 n : {n} 이 쌓였습니다.')
    test(n+1)

print("Welcome to Recursive!")
test(1)
print("Welcome to Elice!")