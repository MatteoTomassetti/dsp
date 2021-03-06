[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

_**Using data from the NSFG, make a scatter plot of birth weight versus mother’s age. Plot percentiles of birth weight versus mother’s age. Compute Pearson’s and Spearman’s correlations. How would you characterize the relationship between these variables?**_

**Note: The working directory is /ThinkStats2/code and the code is in Python 3**

The first step is to read the data from the NSFG
```python
import nsfg
df = nsfg.ReadFemPreg()
live = df[df.outcome == 1] # we only consider live birth
live = live.dropna(subset=["totalwgt_lb","agepreg"]) # we remove all the NaN from the dataset

birth_weight = live.totalwgt_lb
mother_age = live.agepreg
```

Next, we produce a scatter plot of birth weight versus mother's age

![](../img/ex7_1_fig1.png)

that has been generated with the following code
```python
import thinkplot
thinkplot.Scatter(birth_weight,mother_age,label="",s=2)
thinkplot.Save(root="ex7_1_fig1",xlabel="Birth weight [lb]",ylabel="Mother's age [year]",axis=[0,16,10,48])
```

Now we bin the dataframe in bins of mother's age
```python
import thinkstats2
import numpy as np

nbins = 25
bins_age = np.linspace(10,48,nbins)
indices = np.digitize(mother_age,bins_age)
groups = live.groupby(indices)
```

For each bin, we compute the mean mother's age and the percentiles (25th,50th and 75th) of the birth weight

```python
mean_age = [group.agepreg.mean() for _, group in groups][1:-1]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for _,group in groups][1:-1]
perc_vals = [25,50,75] # percentiles to compute
weights = []
for percentile in perc_vals:
    weights.append([cdf.Percentile(percentile) for cdf in cdfs])

```

Next, we plot the result

![](../img/ex7_1_fig2.png)

The figure has been produced with the following code
```
import thinkplot
for i in range(len(perc_vals)):
    label = "%ith" % perc_vals[i]
    thinkplot.Plot(weights[i],mean_age,label=label)

thinkplot.Save(root="ex7_1_fig2",xlabel="Birth weight [lb]",ylabel="Mother's age [year]",axis=[0,16,10,48])
```

We can see that there's not a very strong correlation between these two variables. To study this in a more quantitative way, we compute the Pearson's and Spearman's correlaction coefficients:

```python
import scipy.stats
pearson_corr_coeff  = scipy.stats.pearsonr(birth_weight,mother_age)[0]
print("Pearson's correlation coefficient = ", pearson_corr_coeff)
# Pearson's correlation coefficient =  0.0688339703541
spearman_corr_coeff = scipy.stats.spearmanr(birth_weight,mother_age)[0]
print("Spearman's correlation coefficient = ",spearman_corr_coeff)
# Spearman's correlation coefficient =  0.0946100410966
```

We notice that the correlation coefficients are both really small, which means that there is no correlation between the birth weight and the mother's age.
