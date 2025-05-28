from scipy.stats import chi2

# df = 9
# x2 = 12.25

# area = chi2.cdf(x2, df) # finding prob as area under the curve

# print(area)


df = 9
a = 0.98

perc = chi2.ppf(a, df)

print(perc)