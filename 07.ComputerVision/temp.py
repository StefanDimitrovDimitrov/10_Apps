

n=[0,1,1,2,3,5,8]

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b


print(list(fibonacci(n)))