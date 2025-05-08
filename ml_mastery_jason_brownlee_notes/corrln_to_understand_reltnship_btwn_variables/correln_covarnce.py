# Reference : https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/

# generate related variables


#Definition of correlation:
    # correlation is a representation of relationship between two or three variables.
    # If the relationship is among variables more than two then its has multicolinearity relationship.
    # If the relationship is among two variables then its correlation.
    # Positive correlation : if change in one variable caused another variable to change in the same direction
    # Negative correlation : if change in one variable caused another variable to change in the opp. direction
    # No correlation : if change in one variable does not cause any change in another variable then it has no
    # -correlation  or zero correlation.

# What does the below code infers ?


import numpy as np
from numpy import mean
from numpy import std

#from numpy.random import randn
#from numpy.random import Generator
#from numpy.random import seed

from matplotlib import pyplot

from scipy.stats import pearsonr
from scipy.stats import spearmanr


# seed random number generator
#seed(1)

# PCG64 - Permuted Congruential Generator since numpy 1.17
#Construct a new Generator with the default BitGenerator (PCG64).
rng = np.random.default_rng(seed=1)

# Generator.standard_normal(size=None, dtype=np.float64, out=None)


#We will generate 1,000 samples of two variables with a strong positive correlation.
#The first variable will be random numbers drawn from a Gaussian distribution with a mean of 100 and
#a standard deviation of 20. The second variable will be values from the first variable with
#Gaussian noise added with a mean of 50 and a standard deviation of 10.

# prepare data
#data1 = 20 * randn(1000) + 100
data1 = 20 * rng.standard_normal(1000) + 100

#data2 = data1 + (10 * randn(1000) + 50)
data2 = data1 + (10 * rng.standard_normal(1000) + 50)

# summarize
print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))

covariance = np.cov(data1, data2)
print('covariance :')
print(covariance)

###

# calculate Pearson's correlation
#check the documentation for the below 3 lines to section "Refer : Karl Pearson Co-efficient"

corr, _ = pearsonr(data1, data2)
print('Pearsons correlation: %.3f' % corr)

#Refer spearmans correlation co-efficient
# calculate the spearmans's correlation between two variables


# seed random number generator
#seed(1)
# prepare data
#data1 = 20 * randn(1000) + 100
#np.random.default_rng(seed=1).standard_normal()
#data2 = data1 + (10 * randn(1000) + 50)
# calculate spearman's correlation

corr, _ = spearmanr(data1, data2)
print('Spearmans correlation: %.3f' % corr)
###

# plot
pyplot.scatter(data1, data2)
pyplot.show()

#Refer : Karl Pearson Co-efficient
#Karl Pearson Co-efficient - applicable to Gaussian or Gaussian like distribution
#Measures the linear relationship between two datasets.
#varies between max. range  of -1 to +1 implies an exact linear relationship betwen two datasets.

 # This function also performs a test of the null hypothesis that the
 #    distributions underlying the samples are uncorrelated and normally
 #    distributed.


# calculate the Pearson's correlation between two variables
# A notable relationship exists if the value of Karl pearson co-efficient falls in the range
# of -0.5 to 0.5.



#from numpy.random import randn
#from numpy.random import seed
# seed random number generator
#seed(1)

# prepare data
#data1 = 20 * randn(1000) + 100 #reuse from above
#data2 = data1 + (10 * rng.standard_normal(1000) + 50) #reuse from above


# Pearson’s correlation coefficient can be used to evaluate the relationship between more than two
# variables.
#
# This can be done by calculating a matrix of the relationships between each pair of variables in
# the dataset.
# The result is a symmetric matrix called a correlation matrix with a value of 1.0 along
# the diagonal as each column always perfectly correlates with itself.


