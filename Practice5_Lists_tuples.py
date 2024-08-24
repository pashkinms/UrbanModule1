immutable_var = 2, 'string', 3.5
print(immutable_var)
# immutable_var[0] = 3
# нельзя обращаться непосредственно к элементам кортежа, в отличие от списка. К элементам списка, являющегося элементом кортежа, обращаться можно

mutable_list = [1, 6.5, 'string']
print(mutable_list)
mutable_list[1]+=3
print(mutable_list)