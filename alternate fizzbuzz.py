check = {
    3 : 'Fizz',
    5 : 'Buzz',
    7 : 'Spark',
    11 : 'Bell',
    13 : 'Penny'
}

def fizzbuzz(n):
    for i in range(1, n+1):
        output = ''
        for k, v in check.items():
            if i % k ==0:
                output += v
        print(output or i)

fizzbuzz(49)