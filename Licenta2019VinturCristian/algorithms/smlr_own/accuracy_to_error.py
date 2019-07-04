import sys

vals = []
with open(sys.argv[1], 'r') as f:
	vals = list(map(float, f.readlines()))

with open(sys.argv[1], 'w') as f:
	for val in vals:
		f.write(str(1 - val / 100.0) + "\n")
