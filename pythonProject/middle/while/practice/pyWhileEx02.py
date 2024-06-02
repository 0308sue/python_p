# 1~9단 구구단 출력 형식 = #1단# 1 x 1 = 1
i = 1

while i < 10 :
    print(f"# {i} 단")
    j = 1
    while j < 10 :
        print(f"{i} * {j} = {i*j}")
        j += 1

    i+= 1

