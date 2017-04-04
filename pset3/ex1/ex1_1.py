#Kyle Verdeyen
#Problem set 3, exercise 1, problem 1
#Computational Genomics: Data Analysis
#usage: ex1_1.py genotype_population.csv

import numpy as np
import sys

gene_pop = np.loadtxt(sys.argv[1], skiprows=1, usecols=range(1,
