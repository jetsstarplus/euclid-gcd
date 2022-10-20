from gcd_builtin import GCD

def test(x,y,expected_result):
    result=GCD(x,y)
    assert result == expected_result,f"GCD of {x} and {y} is {expected_result}, expected: {result}"

if __name__=="__main__":
    import timeit
    time_taken=timeit.timeit("test(270, 192,6)", setup="from __main__ import test")
    print(time_taken)
# Passed for the built in function GCD

# 0.23717257499993138
