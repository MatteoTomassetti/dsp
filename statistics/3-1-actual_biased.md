[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

*Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.
Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.
Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.
Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb.*

The working directory is `/ThinkStats2/code` and the code is in Python 3

```
import chap01soln
df = chap01soln.ReadFemResp()
```

We construct the Probability Mass Function of `numkdhh`, the number of children under 18

```
import thinkstats2
pmf = thinkstats2.Pmf(df.numkdhh)
```

We now compute the **biased distribution**
```
def BiasPmf(pmf, label=''):
    new_pmf = pmf.Copy(label=label)
    
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    
    new_pmf.Normalize()
    return new_pmf

biased = BiasPmf(pmf, label='biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()
```

Finally, we compute the means of the two pmfs

```
print("Mean unbiased=", pmf.Mean())
print("Mean biased = ",biased.Mean())
```
