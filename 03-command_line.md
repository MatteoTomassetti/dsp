# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.


> * `**cd**`, to navigate the file system

> * `**pwd**`, to check the current directory

> * `**mkdir**`, to create a directory

> * `**rm -rf**`, to remove a directory

> * `**ls**`, to check the content of a directory

> * `**scp / cp**`, to copy files

> * `**mv**`, to move files

> * `**more**`, to check the content of a file

> * `**head**`, to display the first 10 lines of a file

> * `**tail**`, to display the last 10 lines of a file

> * `**grep -r “something” * **`, to look for a string within all files in a directory

> * `**chmod ugo+rwx * **`, to change the reading, writing and execution permission of a file / directory

> * `**touch**`, to create a new file

> * `**du -sh **`, to know the size of a file

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> * `**ls**` lists all files in the current folder (in alphabetical order)

> * `**ls -a**` list all files, without ignoring hiddens files, the current folder and the folder above that

> * `**ls -l**` shows more details, like the permission, ownership, size and modification date of each file

> * `**ls -lh**` makes the size "human readable", i.e. it's going to be in B, K, M, ...

---


---

What does `xargs` do? Give an example of how to use it.

> **xargs** is useful when combined with other command. Let me go over a few examples:

> * `echo a b c d e f| xargs -n 3`


> This command splits the inputs into three columns and return
> ```
a b c
d e f
```

> * `find . -name "dummy*" | xargs rm`


> This command finds all the files whose name starts with "dummy" and deletes them

> * `find . -name "paper*" | xargs grep "natbib"`


> This finds the string "natbib" on all files whose name starts with "paper"

---

