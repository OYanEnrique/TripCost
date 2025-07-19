dist=float(input('How far is the trip?\n'))
passagem=0.0
if dist<=200:
	passagem=0.50
	print(f'This trip costs {dist*passagem} $\n')
else:
	passagem=0.45
	print(f'This trip costs {dist*passagem} $\n')