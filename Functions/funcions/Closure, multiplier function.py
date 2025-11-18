def func1(x):
    def multiply(n):
        return n*x
    return multiply
result=func1(2)
print(result(5))

    
# Even after make_multiplier() khatam ho gaya, multiply() ko factor yaad hai.
# Yeh hi hota hai closure — function ke andar function, jo outer variable ko lock kar leta hai.


