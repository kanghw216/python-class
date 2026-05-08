def GCD(A, B):
  if B == 0:
    return A
  
  return GCD(B, A % B)
  
print(GCD(106, 16))