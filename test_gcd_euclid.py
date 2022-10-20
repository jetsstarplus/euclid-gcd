from gcd_euclid import GCD

def test(x,y,expected_result):
    result=GCD(x,y)
    assert result == expected_result,f"GCD of {x} and {y} is {expected_result}, expected: {result}"

if __name__=="__main__":
    import timeit
    time_taken=timeit.timeit("test(270, 192,6)", setup="from __main__ import test")
    print(time_taken)
# Passed for the euclid's algorithm
# 0.548575898999843
