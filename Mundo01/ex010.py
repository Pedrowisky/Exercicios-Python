# converter real em dólar
real_coin = float(input('How much money do you have on your wallet?: '))
dollar = real_coin / 5.30
print('With R${} you can have US${:.2f} dollars'.format(real_coin, dollar))
