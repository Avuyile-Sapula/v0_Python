
def divisors(num):
    nums = []
    for i in range(1,num+1):
        if num % i == 0:
            nums.append(i)
    print(nums)

# Example:
divisors(15) #-> [1, 3, 5, 15]
divisors(7) #-> [1, 7]
divisors(24) #-> [1, 2, 3, 4, 6, 8, 12, 24]

