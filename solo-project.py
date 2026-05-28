import random as r

# 오늘 할 일들을 입력 및 중복 제거
tasks = input("오늘 할 일들을 입력해 주세요: ").split(",")
tasks = list(set(map(str.strip, tasks)))

# 오늘 할 취미를 입력 및 중복 제거
hobby = input("평소에 즐겨하는 취미를 입력해 주세요: ").split(",")
hobby = list(set(map(str.strip, hobby)))

# 할 일 리스트에서 공백 제거
if "" in tasks:
  tasks.remove("")

# 할 일을 입력하지 않았을 경우
if not tasks:
  print("오늘 할 일이 입력되지 않았습니다. 오늘 하루만큼은 쉽시다!")
# 할 일을 입력했을 경우
else:
  # 할 일 순서 섞기
  r.shuffle(tasks)
  print(f"오늘의 할 일의 순서는")
  for i in range(0, len(tasks)):
    print(f"{i+1}. {tasks[i]}")
  print("입니다.")

# 취미 리스트에서 공백 제거
if "" in hobby:
    hobby.remove("")

# 취미가 입력되지 않았을 경우 기본 취미 지정
if not hobby:
  hobby = ["명상", "독서", "산책"]
  print("적어주신 취미가 없으셔서 평범한 취미를 골라드릴게요.")

print(f"오늘 하실 취미활동은 {r.choice(hobby)} 입니다.")