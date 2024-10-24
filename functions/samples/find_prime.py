#  function to find if a given number is prime?

def is_prime(n) -> bool:
    if n <=1:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True

def xyz():
    pass


# print(is_prime(5))
# print(is_prime(4))