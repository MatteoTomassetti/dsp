# Install software on your computer


### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`. --> DONE! But Actually the most recent version is 2.3.6


### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python
ipython
ipython notebook
spyder
```

Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```

---

Did you install Python 2 or 3? Why? How can you check the version of Python installed if you happen to be on an unfamiliar computer?

I installed Python 3. Although I am more comfortable with Python 2 (which is often preferred in Academia) I think like this is an opportunity for me to learn more about the newest version of my favorite programming language.

There are several reasons why I chose Python 3 over Python 2

1. Python 2 will not get any more update, other than security updates from the Python 3 developement branch
2. The `raw_input` function has been replaced with `input`, which (unlike in Python 2) always returns a string
3. In Python 3 the division between two integers return a float. This was a problem with Python 2 and could result in unexpected bugs (this could be fixed with the `__future__` module though)
4. All strings are Unicode in Python 3 by default and not byte sequences like in Python 2
5. The `print()` function has parenthesis in Python 3, just like every function is supposed to

Moreover, despite those differences, most of the code one is going to write will work on either system with some small caveats.

To answer the final part of the question. The version of Python installed can be check with this command
```
python -V
```
Which on my system returns
```
Python 3.5.1 :: Anaconda 2.4.1 (x86_64)
```


---


### Homebrew

If you use a Mac, install [Homebrew](http://brew.sh/) if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform. --> DONE! I installed Homebrew a while ago on my laptop
