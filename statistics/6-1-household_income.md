[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

*The distribution of income is famously skewed to the right. In this exercise, we’ll measure how strong that skew is.
The Current Population Survey (CPS) is a joint effort of the Bureau of Labor Statistics and the Census Bureau to study income and related variables. Data collected in 2013 is available from http://www.census.gov/hhes/www/cpstables/032013/hhinc/toc.htm. I downloaded hinc06.xls, which is an Excel spreadsheet with information about household income, and converted it to hinc06.csv, a CSV file you will find in the repository for this book. You will also find hinc2.py, which reads this file and transforms the data.
The dataset is in the form of a series of income ranges and the number of respondents who fell in each range. The lowest range includes respondents who reported annual household income “Under $5000.” The highest range includes respondents who made “$250,000 or more.”
To estimate mean and other statistics from these data, we have to make some assumptions about the lower and upper bounds, and how the values are distributed in each range. hinc2.py provides InterpolateSample, which shows one way to model this data. It takes a DataFrame with a column, income, that contains the upper bound of each range, and freq, which contains the number of respondents in each frame.
It also takes log_upper, which is an assumed upper bound on the highest range, expressed in log10 dollars. The default value, log_upper=6.0 represents the assumption that the largest income among the respondents is 106, or one million dollars.
InterpolateSample generates a pseudo-sample; that is, a sample of household incomes that yields the same number of respondents in each range as the actual data. It assumes that incomes in each range are equally spaced on a log10 scale.
Compute the median, mean, skewness and Pearson’s skewness of the resulting sample. What fraction of households reports a taxable income below the mean? How do the results depend on the assumed upper bound?*

First, we read the data

```python
import pandas
filename = "hinc06.csv"
data = pandas.read_csv(filename,header = None,skiprows=9)
```

Next, we create a DataFrame that contains two columns: the upper bound of each income range and the number of respondents in each range

```python
import numpy as np
cols = data[[0, 1]]

dataframe = []
for _, row in cols.iterrows():
    lbl_range, numb_ppl = row.values
    numb_ppl = int(numb_ppl.replace(",", "")) # replace the coma
    lbl_range = lbl_range.split()[-1].replace("$","").replace(",", "")
    if(lbl_range=="over"):
        lbl_range = np.inf
    else:
        lbl_range = int(lbl_range)
    dataframe.append((lbl_range,numb_ppl))

df = pandas.DataFrame(dataframe)
df.columns = ["income","freq"]

```

We use the function `InterpolateSample` in `hinc2.py` to generate a pseudo sample. We set `log_upper=6`

```python
import hinc2
pseudo_sample = 10.**hinc2.InterpolateSample(df)
```

Computing different statistics on the pseudo sample

```python
import thinkstats2
print("Mean of the pseudo sample = ",pseudo_sample.mean())
# Mean of the pseudo sample =  74278.7429235
print("Standard deviation of the pseudo sample = ",pseudo_sample.std())
# Standard deviation of the pseudo sample =  93946.9041046
print("Median of the pseudo sample = ",np.median(pseudo_sample))
# Median of the pseudo sample =  51226.9330656
print("Skewness of the pseudo sample = ",thinkstats2.Skewness(pseudo_sample))
# Skewness of the pseudo sample =  4.94992380539
print("Pearson skewness of the pseudo sample = ",thinkstats2.PearsonMedianSkewness(pseudo_sample))
# Pearson skewness of the pseudo sample =  0.736127134715
cdf = thinkstats2.Cdf(pseudo_sample)
print("Fraction of incomes below the mean = ",cdf[pseudo_sample.mean()])
# Fraction of incomes below the mean =  0.660005879567
```

Now, let's change the upper bound to higher values, for istance we report all of the above quantities for `log_upper=7` and `log_upper=8`
      
```python
pseudo_sample = 10.**hinc2.InterpolateSample(df,log_upper=7)
print("Mean of the pseudo sample = ",pseudo_sample.mean())
# Mean of the pseudo sample =  124267.432614
print("Standard deviation of the pseudo sample = ",pseudo_sample.std())
# Standard deviation of the pseudo sample =  559608.493872
print("Median of the pseudo sample = ",np.median(pseudo_sample))
# Median of the pseudo sample =  51226.9330656
print("Skewness of the pseudo sample = ",thinkstats2.Skewness(pseudo_sample))
# Skewness of the pseudo sample =  11.603690553
print("Pearson skewness of the pseudo sample = ",thinkstats2.PearsonMedianSkewness(pseudo_sample))
# Pearson skewness of the pseudo sample =  0.391564704262
cdf = thinkstats2.Cdf(pseudo_sample)
print("Fraction of incomes below the mean = ",cdf[pseudo_sample.mean()])
# Fraction of incomes below the mean =  0.856563066521

pseudo_sample = 10.**hinc2.InterpolateSample(df,log_upper=8)
print("Mean of the pseudo sample = ",pseudo_sample.mean())
# Mean of the pseudo sample =  457453.52263971645
print("Standard deviation of the pseudo sample = ",pseudo_sample.std())
# Standard deviation of the pseudo sample =  4434938.6092212098
print("Median of the pseudo sample = ",np.median(pseudo_sample))
# Median of the pseudo sample =  51226.933065623722
print("Skewness of the pseudo sample = ",thinkstats2.Skewness(pseudo_sample))
# Skewness of the pseudo sample =  14.892459817044712
print("Pearson skewness of the pseudo sample = ",thinkstats2.PearsonMedianSkewness(pseudo_sample))
# Pearson skewness of the pseudo sample =  0.274790997546
cdf = thinkstats2.Cdf(pseudo_sample)
print("Fraction of incomes below the mean = ",cdf[pseudo_sample.mean()])
# Fraction of incomes below the mean =  0.978629407634
```

As expected, we can see that the moment-based skewness increases as the upper bound increases. On the other hand, the Pearson Skewness decreases and this has to do with the fact that changing the upper buond has a great effect of the standard deviation, which largerly increases.
This proves that for this example the Pearson  skewness is not a good statistics.
