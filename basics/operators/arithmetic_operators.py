#  used to perform arithmetics on the variables / numbers
# types of arithmetic operators
# plus -- + (can be used on numbers and strings)
# subtracct -- -(can be used on numbers )
# multiply -- * (can be used on numbers )
# divide -- / (can be used on numbers )
# modulus -- % (can be used on numbers )
# exponent -- ** (can be used on numbers )

num1 = 10
num2 = 20

msg = "Hello! "
name = "Alex"

#-------------- plus operator -------------
# can be used on numbers and strings 
print(num1 + num1)
print(msg + name)

#-------------- minus operator -------------
# can be used only on numbers
print(num1 - num2)
print(abs(num1 - num2))

#-------------- multiply operator -------------
# can be used only on numbers
print(num1 * num2)

#-------------- division operator -------------
# can be used only on numbers
print(num1 / num2)
# never use the denominator as zero as it results in a runtime error
num2 = 0
print(num1 / num2)

#-------------- exponent operator -------------
# can be used only on numbers
a = 2
b =3
print(5**3)
print(a**b)




