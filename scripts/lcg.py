import random
seed = random.randint(0,0xFFFF)
lcg = seed
a = 257
m = 32768
print lcg

period = 0
lcg = (a * lcg + 1) % m
print lcg >> 13
period += 1


while (period < 1000):
	lcg = (a * lcg + 1) % m
	print lcg >> 13
	period += 1

print period


