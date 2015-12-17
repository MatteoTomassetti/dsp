#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

import numpy as np
import sys
import re

class MarkovText():
  
  def __init__(self):
    # default number of words to return
    self.n_words = 40
    # default minimum number of words for each line to be considered
    self.n_ignore = 4
  
  def read_text(self,filename):
    self.all_words = []
    with open(filename, 'r') as f:
      for line in f:
        # we remove the punctuation marks
        words_in_line = map(lambda x:x.strip('_()'),line.split())
        # remove all words that are number (i.e. Chapter or Section numbers)
        words_in_line = filter(lambda x:x.isdigit()==False,words_in_line)
        dummy_chars = ['"',"_","--","(",")"]
        for dummy_char in dummy_chars:
          words_in_line = [dummy.replace(dummy_char,'') for dummy in words_in_line]
        if(len(words_in_line)>self.n_ignore):
          self.all_words.extend(words_in_line)
    
    self.all_words = np.array(self.all_words)
    return self.all_words
  
  def rnd_text(self,filename):
    self.read_text(filename)
    # generate a random number from 0 to len(self.all_words)-1
    # so that we can pick up the first two words
    idx = np.random.randint(0,len(self.all_words))
    self.text = self.all_words[idx].title() + " " + self.all_words[idx+1]
    # where do this pair of words appear?
    while(len(self.text.split())<self.n_words):
      idx_first_word = np.where(self.all_words==self.all_words[idx])
      mask_good = [self.all_words[dummy+1]==self.all_words[idx+1] for dummy in idx_first_word]
      idx_second_word = idx_first_word[0][mask_good]
      idx_third = np.random.choice(idx_second_word+2)
      self.text = self.text + " " + self.all_words[idx_third]
      idx = idx_third-1
    
    self.text += "."

if __name__ == "__main__":
  mt = MarkovText()
  filename = sys.argv[1]
  try:
    mt.n_words = int(sys.argv[2])
  except ValueError:
    print("The number of words should an integer!")
  
  mt.rnd_text(filename)
  print mt.text





