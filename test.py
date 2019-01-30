from scipy.misc import comb

sum = 0;
for i in range(16):
    sum += comb(16, i) * pow(9, 20-i);

sum /= pow(10, 20);
print(sum);
