# def remove_duplicates(number):
#     new_list = []
#     for num in number:
#         if num not in new_list:
#             new_list.append(num)
        
#     return new_list

# ids = [1,2,3,4,1,2,4,5,6,7]
# print(remove_duplicates(ids))


# Another way of returning non-repeated values from a list is to use set:

def remove_duplicates(number):
    return list(set(number))

ids = [1,2,3,4,2,1,6,5,3,7]
result = remove_duplicates(ids)
print(result)