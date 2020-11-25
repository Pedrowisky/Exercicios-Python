# calcular a area de uma parede e quanto de tinta seria necessário para pinta-la
# cada litro pinta uma area de 2m²
width = float(input('Wall width: '))
height = float(input('Wall height: '))
area = width * height
tint = area / 2
print('The area of the wall with the dimensions of {} x {} is: {}m²'
      '\nThe necessary amount of tint will be: {}l '.format(width, height, area, tint))
