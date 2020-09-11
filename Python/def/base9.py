# 1行のif lambda式
y = 5
x = 10 if y >10 else 5
print(x)

lambda_a = lambda x: x * x
print(lambda_a(x))

lambda_b = lambda x,y,z:x*y-z

print(lambda_b(5,5,5))

# 条件式付きlambda
lambda_c = lambda x,y:y if y >x else x

print(lambda_c(5,5))
