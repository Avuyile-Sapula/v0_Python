def fizz_buzz(max_num):
    for i in range(1,max_num+1):
        if i%3 == 0:
            if i%5 != 0:
                print(i)
        elif i%5 == 0:
            if i%3 != 0:
                print(i)
# Example:
fizz_buzz(18)
# 3
# 5
# 6
# 9
# 10
# 12
# 18

fizz_buzz(33)
# 3