#  most times the logical oerators are used in compounding the conditions
#  applied on more than one condition
# the result is always boolean

# types of operators
#  and
#  or
#  not

# And truth table			
# C1	C2	Result	
# T	    T	T	
# T	    F	F	
# F	    T	F	
# F	    F	F	

# OR truth table		
# C1	C2	Result
# T	    T	T
# T	    F	T
# F     T	T
# F	    F	F

# Not	
# condition	result
# T	        F
# F	        T




c1 = True
c2 = False

print(c1 and c2)
print(c1 or c2)

# using the not
print(not c1)
print(not c2)
print(not(c1 or c2))

