import scipy.stats as st
import math

"""
The t.cdf() and t.sf() functions are used to find probabilities related to the 
-distribution. The scipy.stats library must be imported to use these functions.

t.cdf(t, df, mean, sd) returns the probability of a quantity or observation being less than or equal to the value t for a 
-distribution with the specified degrees of freedom, mean, and standard deviation.

 t.sf(t, df, mean, sd) returns the probability of a quantity or observation being greater than the value t for a 
-distribution with the specified degrees of freedom, mean, and standard deviation.

The t.ppf() and t.isf() functions are used to convert percentiles to critical values. 

t.ppf(p, df, mean, sd) returns the critical value for which the probability of a quantity or observation being below that critical value is p, for a 
-distribution with the specified degrees of freedom, mean, and standard deviation.

 t.isf(p, df, mean, sd) returns the critical value for which the probability of a quantity or observation being above that critical value is p, for a 
-distribution with the specified degrees of freedom, mean, and standard deviation.
"""
n = 50
pop_mean = 1.86
sam_mean = 2.1
sd = 1.57
df = 49

t = (sam_mean - pop_mean)/(sd/math.sqrt(n))
# print("t-stat:",t)

prob = st.t.sf(t, df)

print(f'The probability that another 50 household sample will have a sample mean of at least 2.1 is {prob:.6f}.')