# usual simle function
def add (x, y) :
    return x+y

print (add (4,5))

# the same function as lambda
add2 = lambda x,y: x+y
print (add2 (4,5))

# create lambda, add arguments ant put all this shit to another function
print((lambda x,y: x+y)(4,5))

# Lambdas made to be passed to higher-order functions
# Higher-order function can either take another func as an input or return another function as output or both.
# In example my_map takes my_func variable. And during call we pass lambda to my_func var.

def my_map (my_func, my_iter) :
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result. append (new_item)
    return result


nums = [3, 4, 5, 6, 71]
cubed = my_map(lambda x: x**3, nums)
print (cubed)