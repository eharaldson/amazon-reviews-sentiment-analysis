import bz2
from collections import Counter
import re
import nltk
import numpy as np

nltk.download('punkt')

train_file = bz2.BZ2File('raw_data/train.ft.txt.bz2')
test_file = bz2.BZ2File('raw_data/test.ft.txt.bz2')

train_file = train_file.readlines()
test_file = test_file.readlines()