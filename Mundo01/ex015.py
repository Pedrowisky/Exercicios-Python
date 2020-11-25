# aluguel - R$60 por dia - R$0.15 por km
days = int(input('Days rented: '))
km = float(input('Km driven: '))
# cost_days = 60 * days
# cost_km = 0.15 * km
# total = cost_km + cost_days
total = (60 * days) + (0.15 * km)
print('You must pay the total of R${:.2f}'.format(total))
