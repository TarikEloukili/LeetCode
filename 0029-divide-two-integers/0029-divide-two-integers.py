class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 0:
            raise ValueError("Cannot divide by zero.")
        if dividend == 0:
            return 0

        INT_MAX = 2**31 - 1  
        INT_MIN = -2**31      

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            current_divisor, multiple = divisor, 1
            while dividend >= (current_divisor << 1):
                current_divisor <<= 1
                multiple <<= 1
            dividend -= current_divisor
            quotient += multiple

        result = -quotient if negative else quotient
        
        return min(max(INT_MIN, result), INT_MAX)
