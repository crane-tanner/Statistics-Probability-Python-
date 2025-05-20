import scipy.stats as st

# print(st.norm.cdf() ) returns the probability of a quantity or observation
# being less than or equal to the value z for a normal distribution with the specified mean and standard deviation.

# print(st.norm.sf(159,150, 8.75))) returns the probability of a quantity or observation
# being greater than the value z for a normal distribution with the specified mean and standard deviation.

# print(st.norm.ppf(.4, 150, 8.75)) # returns the score below given a probability
# print(st.norm.isf(.20, 150, 8.75)) # returns the score above given a probability


# input two IQs, making sure that IQ1 is less than IQ2
IQ1 = float(input())
IQ2 = float(input())

while IQ1 > IQ2:
    print("IQ1 should be less than IQ2. Enter numbers again.")
    IQ1 = float(input())
    IQ2 = float(input())

prob_al = st.norm.sf(IQ1, 100, 15)
# Calculate the probability that a randomly selected person has an IQ greater than or equal to IQ1.

prob_am = st.norm.cdf(IQ1, 100, 15)
# Calculate the probability that a randomly selected person has an IQ less than or equal to IQ1.

prob_bet = st.norm.cdf(IQ2, 100, 15) - st.norm.cdf(IQ1, 100, 15)

# Calculate the probability that a randomly selected person has an IQ between IQ1 and IQ2

print(f'The probability that a randomly selected person \n has an IQ greater than or equal to {IQ1} is {prob_al:.6f}.')
print(f'The probability that a randomly selected person \n has an IQ less than or equal to {IQ1} is {prob_am:.6f}.')
print(f'The probability that a randomly selected person \n has an IQ between {IQ1} and {IQ2} is {prob_bet:.6f}.')
