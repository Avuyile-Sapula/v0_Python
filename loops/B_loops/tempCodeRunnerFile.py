# The function does not return a value, just prints.
def div_by_either(num1,num2, max_num):
    for i in range(1,max_num):
        if i%num1==0 or i%num2 ==0:
            print(i)
 

# Example:
div_by_either(4, 3, 16)
# 3
# 4
# 6
# 8
# 9
# 12
# 15