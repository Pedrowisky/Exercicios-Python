# dobro, triplo e raiz quadrada de um numero
num = int(input('Type a number: '))
# square_root = pow(num, 1/2) >> can also be done inside the format =)
print('The double is: {}. \n'
      'The triple is: {}. \n'
      'The square root is: {:.2f}.'.format(num * 2, num * 3, num ** (1/2)))
