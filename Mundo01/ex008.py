# distância de metros em outras medidas
distance = float(input('Type a distance: '))
km = distance / 1000
hm = distance / 100
dam = distance / 10
dm = distance * 10
cm = distance * 100
mm = distance * 1000
print('The measure of {} meters matches: '
      '\n{}km '
      '\n{}hm '
      '\n{}dam '
      '\n{:.0f}dm '
      '\n{:.0f}cm '
      '\n{:.0f}mm'.format(distance, km, hm, dam, dm, cm, mm))
