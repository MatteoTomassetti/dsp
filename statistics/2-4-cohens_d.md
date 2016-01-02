[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

*Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length? *

The working directory is `/ThinkStats2/code`
```
# importing the NSFG data
import nsfg
df = nsfg.ReadFemPreg()

firsts = df[df.birthord == 1] # first babies
others = df[df.birthord != 1] # others

print("Median weight for first babies = ",firsts.totalwgt_lb.median())
print("Median weight for other babies = ",others.totalwgt_lb.median())
# Median weight for first babies =  7.3125
# Median weight for other babies =  7.375
```

If one looks at the **median** weight for first and other babies, the conclusion is that first babies are slighlty less heavier than other babies.

Next, we compute the Cohen's d statistic

```
# Cohen's d statistic
import math
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

print(CohenEffectSize(firsts.totalwgt_lb,others.totalwgt_lb))
# -0.08893641177719079
```

and find that the fact that we are selecting first or other babies, does not have a large effect on the weight of an baby since the Cohen's d is less than 0.09 standard deviations.

The difference between the two groups in pregnancy length is also small (0.029) if one consider only pregnancies that last at least 27 weeks for other babies. However, if all pregnancies are considered, we find that

```
print(CohenEffectSize(firsts.prglngth,others.prglngth))
#1.0930083433621403
```
which means that first babies pregnancies are significantly longer than other babies pregnancies since the Cohen's d is large.

