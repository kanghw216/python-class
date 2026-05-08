def factorial(n):
  if n <= 1:
    return 1
  return n * factorial(n - 1)

print(factorial(5))

# result = 1
# for i in range(1, 6): # 1부터 5까지
#     result *= i
# print(result) # 120