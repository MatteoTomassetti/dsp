[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

_**In Section 9.3, we simulated the null hypothesis by permutation; that is, we treated the observed values as if they represented the entire population, and randomly assigned the members of the population to the two groups.
An alternative is to use the sample to estimate the distribution for the population, then draw a random sample from that distribution. This process is called resampling. There are several ways to implement resampling, but one of the simplest is to draw a sample with replacement from the observed values, as in Section 9.10.
Write a class named DiffMeansResample that inherits from DiffMeansPermute and overrides RunModel to implement resampling, rather than permutation.
Use this model to test the differences in pregnancy length and birth weight. How much does the model affect the results?**_

**Note: The working directory is `/ThinkStats2/code` and the code is in Python 3**

In order to answer the question we first implement the class `DiffMeansResample`, that (as requested) inherits from `hypothesis.DiffMeansPermute` and overried `RunModel` to implement resampling.

```python
import hypothesis

class DiffMeansResample(hypothesis.DiffMeansPermute):
    # implementing resampling with replacement for the two groups
    def RunModel(self):
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.m, replace=True)
        return group1, group2
```

The next step is to import the data set and store the values to test in the variable `data_to_test`

```python
# importing the NSFG data
import nsfg
df = nsfg.ReadFemPreg()
live = df[df.outcome == 1] # we only consider live birth
live = live.dropna(subset=["totalwgt_lb","agepreg"]) # we remove all the NaN from the dataset

firsts = live[live.birthord==1] # first babies
others = live[live.birthord!=1] # other babies

data_to_test = [[firsts.prglngth.values,others.prglngth.values],[firsts.totalwgt_lb.values,others.totalwgt_lb.values]]
```

Finally, we compute the p-values for `DiffMeansPermute` and `DiffMeansResample`

```python
what = ["Pregnancy length","Birth weight"]
for i in [0,1]:
    print("//////")
    print(what[i])
    hypo1 = hypothesis.DiffMeansPermute(data_to_test[i])
    hypo2 = DiffMeansResample(data_to_test[i])
    
    p_value1 = hypo1.PValue()
    p_value2 = hypo2.PValue()
    
    print("P-value (permutation)=",p_value1)
    print("P-value (resampling)=",p_value2)
    print("//////")
```

which leads to
```python
//////
Pregnancy length
P-value (permutation)= 0.177
P-value (resampling)= 0.19
//////
//////
Birth weight
P-value (permutation)= 0.0
P-value (resampling)= 0.0
//////
```

Therefore, the p-values for the two methods are very similar and there is no reason to choose one model over the other.
Based of the hypothesis tests performed here we can conclude that the difference in pregnancy length is not statistically significant and it is most likely due to randomness because the p-value is large (i.e. greater than 5%). On the other hand, the p-value when testing the difference in birth weight is zero, so it is likely that the population of first and other babies have different mean birth weight.
