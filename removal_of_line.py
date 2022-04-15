
from fpdf import FPDF
import os
import pathlib
from os import initgroups
import pandas as pd


test1file = pathlib.Path("test1.csv")
test2file = pathlib.Path('test2.csv')
output11file = pathlib.Path('output11.csv')

os.remove(test1file)
os.remove(test2file)
os.remove(output11file)


    


# data = pd.read_csv("test.csv")

# data = data.to_csv('test1.csv', header = False)

# data = pd.read_csv('test1.csv')

# data = data.to_csv('test2.csv', header = False, index=False)

# data = pd.read_csv('test2.csv')

# data.drop_duplicates(subset = "BatchJob Name",keep = 'first', inplace = True)
# df=data
# df.to_csv('output11.csv')
