

MOD = 10 ** 9 + 7

def power(num1, position_count):
    result = 1
    num1 = (num1 % MOD)
    
    while(position_count > 0):
        if position_count % 2 == 1:
            result = (result * num1) % MOD
        
        num1 = (num1 * num1) % MOD
        position_count //= 2
    
    return result


def count_good_number(num):
    even_pos = (num + 1) // 2
    odd_pos = (num // 2)

    return (power(5, even_pos) * power(4, odd_pos)) % MOD

print(count_good_number(4))