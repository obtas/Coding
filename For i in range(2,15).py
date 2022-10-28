def fizz_buzz(n):
    for i in range(1,n+1):
        word = ""
        if i % 3 == 0:
            word += "Fizz"
        if i % 5 ==0:
            word += "Buzz"
        if len(word) == 0:
            word += f"{i}"
        print(word)

fizz_buzz(5)
fizz_buzz(-1)

