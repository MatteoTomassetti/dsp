# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples are both collections of items. For example, a list can be defined as
```
my_list = [1,2,3,4,5]
```
and a tuple could be
```
my_tuple = (1,2,3,4,5)
```

The main difference between lists and tuples is that while the first are dynamic arrays, the second are static.
This means that tuples are immutable and their elements cannot be changed. On the other hands, one can insert new elements to a list (with commands such as `append` or `extend`) and can also remove elements (with `remove` or `pop`).

Tuples are more efficient than lists and it's always a good practice to use them if one needs to store a set of costant values. Tuples can also work as dictionary keys because they countain immutable values. Lists, on the other hand, are unhashable and they cannot be used as dictionary keys or in sets.


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists are sets are both dynamic collections of elements, but the elements in set are all distinct.

An example of list could be

```
my_list = [1,2,3,4,5]
```
while for a set we have

```
my_set = set([1,2,3,4,5])
```

When finding elements, one prefers to use sets because `in` is a very fast operation on them. For instance, if we search the number 3 in a list or set containing the same elements, the search in faster on the set.

```
python -m timeit -s "x=[1,2,3,4,5,6,7,8]" "3 in x"
10000000 loops, best of 3: 0.0889 usec per loop

python -m timeit -s "x=set([1,2,3,4,5,6,7,8])" "3 in x"
10000000 loops, best of 3: 0.0609 usec per loop
```





---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

`lambda` is construct that can be used, together with `def` to define a function in python. For instance

```
def square(x):
  return x**2.
```

is equivalent to

```
square = lambda x: x**2.
```

Moreover, `lambda` can be used to create anonymous functions, which mean that it can be used to create a function without assigning it to a variable. For example the following piece of code

```
students = [("Mark","C"),("Tom","A"),("Lisa","F"),("Nina","B")]
sorted(students,key = lambda x:x[1])
```

Returns the input list sorted according to the grade of the student.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehension is useful when one wants to transform a list into another list by either applying a function to its elements, or selecting only certain elements, or both.

For instance, we return the square of all the elements of a list using list comprehension the following way

```
my_list = [1,4,5,7,2,3,5,6,9,5,4,8,10,12]
squared_list = [ x**2 for x in my_list ]
```

Equivalently, we can get the same answer with `map`

```
squared_list_map = map(lambda x:x**2,my_list)
```

In this particular example `map` performs poorly with respect to list comprehension.

```
python -m timeit -s "my_list=[1,4,5,7,2,3,5,6,9,5,4,8,10,12]" "[ x**2 for x in my_list ]"
1000000 loops, best of 3: 1.53 usec per loop

python -m timeit -s "my_list=[1,4,5,7,2,3,5,6,9,5,4,8,10,12]" "map(lambda x:x**2,my_list)"
100000 loops, best of 3: 2.44 usec per loop
```

However, `map` can be faster when it is not coupled with `lambda`. For instance,
```
python -m timeit -s "my_list=[1,4,5,7,2,3,5,6,9,5,4,8,10,12]" "[ abs(x) for x in my_list ]"
1000000 loops, best of 3: 1.34 usec per loop
python -m timeit -s "my_list=[1,4,5,7,2,3,5,6,9,5,4,8,10,12]" "map(abs,my_list)"
1000000 loops, best of 3: 1.03 usec per loop
```

Another example of things we could do with list comprehension is selecting only the odd numbers from the same list.
The solution with list comprehension is

```
odd_numbers = [ x for x in my_list if x%2 == 1 ]
```

and the equivalent solution with `filter` is

```
odd_numbers_filter = filter(lambda x: x%2==1 ,my_list)
```

`filter` is usually slower than list comprehension:

```
python -m timeit -s "my_list=[1,4,5,7,2,3,5,6,9,5,4,8,10,12]" "[ x for x in my_list if x%2 == 1 ]"
1000000 loops, best of 3: 1.64 usec per loop
python -m timeit -s "my_list=[1,4,5,7,2,3,5,6,9,5,4,8,10,12]" "filter(lambda x: x%2==1 ,my_list)"
100000 loops, best of 3: 2.24 usec per loop
```

List comprehension can be use to create a set:
```
new_set = set([n for n in range(9)])
```

Other another example can be
```
r = [0,1,2]
new_set = {(x,y) for x in r for y in r}
```
which creates a set with all the permutations of the elements in `r`


Dictionary comprehension can be very useful to create dictionaries:

```
new_dict = {n : n+5 for n in range(10)}
```

or initialize all values of a dictionary:

```
new_dict={n: 0 for n in range(10)}
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

937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850 days

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





