print('yusuf and sons')
principal = float(input('enter amount:'))
time = float(input('enter time:'))
rate = float(input('enter rate:'))
simple_interrest = (principal*time*rate)/100
compond_interest = principal * ((1+rate/100)**time - 1)
print('simple interest is: %f'%(simple_interrest))
print('compound_interest is: %f'%(compond_interest))