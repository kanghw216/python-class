def countdown(n):
  if n < 1:
    print('발사')
    return 

  print(n)
  countdown(n - 1)
  
countdown(5)