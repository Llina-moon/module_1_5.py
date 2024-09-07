immutable_var= (24, [1,7],True,'cat')
print(immutable_var)

immutable_var [1][0]= 3
print(immutable_var)

#кортеж является не изменяемой конструкцией,однако элементы можно изменить,например,значение в списке

mutable_list = [1,2,38,'banana']
mutable_list [2] = True
mutable_list.extend(['cola',000,5.6])
print(mutable_list)
