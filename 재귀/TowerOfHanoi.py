def hanoi(n, start, end, sub):
    # 탈출 조건: 원판이 1개일 때는 그냥 바로 옮기면 끝!
    if n == 1:
        print(f"원판 1을 {start}에서 {end}로 이동")
        return

    # 1단계: n-1개를 시작점에서 보조 기둥(sub)으로 이동
    hanoi(n - 1, start, sub, end)

    # 2단계: 가장 큰 원판을 목적지로 이동
    print(f"원판 {n}을 {start}에서 {end}로 이동")

    # 3단계: 보조 기둥에 있던 n-1개를 목적지(end)로 이동
    hanoi(n - 1, sub, end, start)

# 실행: 원판 3개를 'A'에서 'C'로 이동 (B는 보조 기둥)
hanoi(3, 'A', 'C', 'B')

#AI 사용