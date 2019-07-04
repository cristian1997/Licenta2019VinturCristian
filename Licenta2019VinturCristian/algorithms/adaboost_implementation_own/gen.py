from random import uniform

def generate_data(filename, m):
	with open(filename, 'w') as out:
		for _ in range(m):
			x1, x2, x3 = uniform(0, 1), uniform(0, 1), uniform(0, 1)
			# label = 1 if (x1 ** 2 + x2 ** 2 >= 75) else -1
			label = 0 if ((x1 <= 0.5 and x2 <= 0.2) or (x1 > 0.6 and x2 > 0.3)) else 1
			# label = -1 if (x1 <= 20 or x1 >= 60) else 1
			out.write('{} {} {} {}\n'.format(x1, x2, x3, label))

generate_data('../datasets/2vars/train.txt', 100)
generate_data('../datasets/2vars/test.txt', 100)
