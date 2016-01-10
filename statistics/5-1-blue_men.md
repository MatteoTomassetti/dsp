[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

_**In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.**_

**Note: The working directory is /ThinkStats2/code and the code is in Python 3**


First, we define the distribution of heights for men
```python
import scipy.stats
mu = 178 # cm
sigma = 7.7 # cm
distr_height = scipy.stats.norm(loc=mu,scale=sigma)
```

In the following piece of code we define a function that converts length in foot and inches to cm
```python
def height_in_SU(foot,inches):
    total_inches = inches + foot * 12
    return total_inches * 2.54
```

We use this function to convert the height limits in cm
```python
min_height = height_in_SU(5,10)
max_height = height_in_SU(6,1)
```

Finally, we compute the fraction the US male population in the indicated height range
```python
frac_ppl = distr_height.cdf(max_height)-distr_height.cdf(min_height)

print(str(round(frac_ppl,3))+" percent of the male population is between 5' 10"+'"'+" and 6' 1"+'"')
# 0.343
```
