# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

> How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> Lists and tuples are both collections of items. For example, a list can be defined as
```
my_list = [1,2,3,4,5]
```
and a tuple could be
```
my_tuple = (1,2,3,4,5)
```

> The main difference between lists and tuples is that while the first are dynamic arrays, the second are static.
This means that tuples are immutable and their elements cannot be changed. On the other hands, one can insert new elements to a list (with commands such as `append` or `extend`) or remove elements from it (with `remove` or `pop`)./ 

> Tuples are more efficient than lists and it's always a good practice to use them if one needs to store a set of costant values. Tuples can also work as dictionary keys because they countain immutable values. Lists, on the other hand, are unhashable and they cannot be used as dictionary keys or in sets.


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> Lists are sets are both dynamic collections of elements, but the elements in set are all distinct.

> An example of list could be
```
my_list = [1,2,3,4,5]
```
while for a set we have
```
my_set = set([1,2,3,4,5])
```

> When finding elements, one prefers to use sets because `in` is a very fast operation on them. For instance, if we search the number 3 in a list or set containing the same elements we get

> ```
> python -m timeit -s "x=[1,2,3,4,5,6,7,8]" "3 in x"
> 10000000 loops, best of 3: 0.0728 usec per loop

> python -m timeit -s "x=set([1,2,3,4,5,6,7,8])" "3 in x"
> 10000000 loops, best of 3: 0.0481 usec per loop
> ```

> which proves that searching element in a set is usuall faster.




---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> `lambda` is construct that can be used in place of `def` to define a function in python. For instance
```
def square(x):
  return x**2.
```

> is equivalent to
```
square = lambda x: x**2.
```

> Moreover, `lambda` can be used to create anonymous functions, which mean that it can be used to create a function without assigning it to a variable. For example the following piece of code
```
students = [("Mark","C"),("Tom","A"),("Lisa","F"),("Nina","B")]
print (sorted(students, key = lambda x:x[1]))
```

> Returns the input list sorted according to the grade of the student and the anonymous function is specified in the `key` argument.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

> List comprehension is useful when one wants to transform a list into another list by either applying a function to its elements, or selecting only certain elements, or both.

> For instance, list comprehension can be used to return a list containing the squares of the elements of a list in the following way
```
my_list = [1,4,5,7,2,3,5,6,9,5,4,8,10,12]
squared_list = [ x**2 for x in my_list ]
```

> Equivalently, one can get the same answer with the function `map`
```
squared_list_map = list(map(lambda x:x**2,my_list))
```

> In this particular example `map` performs worse than list comprehension:
```
python -m timeit -s "my_list=[1,4,5,7,2,3,5,6,9,5,4,8,10,12]" "[ x**2 for x in my_list ]"
1000000 loops, best of 3: 5.51 usec per loop
python -m timeit -s "my_list=[1,4,5,7,2,3,5,6,9,5,4,8,10,12]" "list(map(lambda x:x**2,my_list))"
100000 loops, best of 3: 7.04 usec per loop
> ```

> However, `map` in Python 3 is slightly faster than list comprehension when it is not coupled with `lambda`. For instance,
>```
python -m timeit -s "my_list=[1,4,5,7,2,3,5,6,9,5,4,8,10,12]" "[ abs(x) for x in my_list ]"
1000000 loops, best of 3: 1.88 usec per loop
python -m timeit -s "my_list=[1,4,5,7,2,3,5,6,9,5,4,8,10,12]" "list(map(abs,my_list))"
1000000 loops, best of 3: 1.53 usec per loop
```

> Another example of things we could do with list comprehension is selecting only certain elements from a list. For instance, if we want to select the odd numbers from a list we can do
```
odd_numbers = [ x for x in my_list if x%2 == 1 ]
```

> and the equivalent solution with the function `filter` is
```
odd_numbers_filter = list(filter(lambda x: x%2==1 ,my_list))
```

> `filter` is usually slower than list comprehension:
```
python -m timeit -s "my_list=[1,4,5,7,2,3,5,6,9,5,4,8,10,12]" "[ x for x in my_list if x%2 == 1 ]"
1000000 loops, best of 3: 2.73 usec per loop
python -m timeit -s "my_list=[1,4,5,7,2,3,5,6,9,5,4,8,10,12]" "list(filter(lambda x: x%2==1 ,my_list))"
100000 loops, best of 3: 3.99 usec per loop
```

> Set comprehension can be use to create a set:
```
new_set = set([n for n in range(9)])
```

> And other another example could be
```
r = [0,1,2]
new_set = {(x,y) for x in r for y in r}
```
which creates a set with all the permutations of the elements in `r`


> Dictionary comprehension can be very useful to initialize dictionaries:
```
new_dict = {n : n+5 for n in range(10)}
```

> or modify an existing dictionary
```
new_dict = {"a":1,"b":3}
new_dict = {key: value+1 if value == 1 else 0 for key,value in new_dict.items()}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py) --> code has been updated!

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py) --> code has been updated!

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py) --> code has been updated!

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py) --> code has been updated!





