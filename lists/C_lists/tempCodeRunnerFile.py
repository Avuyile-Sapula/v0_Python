def common_elements(arr1,arr2):
    new_list = [word for word in arr1 if word in arr2]
    print(new_list)

# Example:
common_elements(["a", "c", "d", "b"], ["b", "a", "y"]) #-> ['a', 'b']
common_elements([4, 7], [32, 7, 1, 4]) #-> [4, 7]
