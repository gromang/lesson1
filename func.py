def get_summ(one,two,delimiter='&'):
    one = str(one)
    two = str(two)
    return f'{one}{delimiter}{two}'

result = get_summ('Learn','python')
print(result)
print(result.upper())
