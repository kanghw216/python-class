def Hanoi(n, start, end, sub):
  if n == 1:
    print(start,'->',end)
    return
  
  Hanoi(n - 1, start, sub, end)
  print(start,'->',end)
  Hanoi(n - 1, sub, end, start)

n = int(input("원판 개수: "))
Hanoi(n, 'A', 'C', 'B')