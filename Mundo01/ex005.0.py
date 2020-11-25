# soma, multiplicação, divisao, divisao int, exponencial
num1 = int(input('1 Value: '))
num2 = int(input('2 Value: '))
soma = num1 + num2
m = num1 * num2
div = num1 / num2
div_int = num1 // num2
ex = num1 ** num2
print('Sum: {}, multiplication: {}, division: {:.2f}'.format(soma, m, div), end=', ')
print('int division: {}, exponential: {}'.format(div_int, ex))
