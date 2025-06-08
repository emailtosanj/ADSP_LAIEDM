Attempt #1
Jun 04, 5:35 PM
Marks: 2
Question 1
Correct Answer
Marks: 1/1

The probability of an employee leaving the company within 6 months is 0.6. If 10 employees are selected randomly, which of the following codes can be used to find the probability that 7 out of the 10 employees will leave the company within 6 months?
from scipy.stats import binom
1 - binom.pmf(k = 7,n = 10, p = 0.6)
from scipy.stats import binom
binom.cdf(k = 7,n = 10, p = 0.6)
from scipy.stats import binom
binom.pmf(k = 7,n = 10, p = 0.6)
You Selected
from scipy.stats import binom
1 - binom.cdf(k = 7,n = 10, p = 0.6)
Here, the parameters of the binomial distribution are n = 10 and p = 0.6. Now, we are to find the probability that 7 employees will leave the company within 6 months. That is P(X=7)

Note that binom.pmf(k,n,p) will calculate the probability P(X=k) that is X takes the value k.

So, the output of the below code will give the required probability:

from scipy.stats import binom
binom.pmf(k = 7,n = 10, p = 0.6)

Question 2
Incorrect Answer
Marks: 0/1

Several companies are working on the COVID vaccine. The probability of a vaccine getting approved by the CDC is 0.75. If 15 vaccines are randomly selected, which of the following codes can be used to find the probability of at least 6 getting approved by the CDC?
from scipy.stats import binom
binom.cdf(k = 6,n = 15, p = 0.75)
You Selected
from scipy.stats import binom
binom.pmf(k = 6,n = 15, p = 0.75)
from scipy.stats import binom
1 - binom.pmf(k = 6,n = 15, p = 0.75)
from scipy.stats import binom
1 - binom.cdf(k = 5,n = 15, p = 0.75) 
Correct Option
cdf() function is used to find the cumulative probability at most k successes in n number of trials where the probability of success for each trial is p.

 

Here, the parameters of the binomial distribution are n = 15 and p = 0.75. Now, we are to find the probability that at least 6 out of 15 vaccines get approved, which means P(X>=6).
Note that binom.cdf(k,n,p) will calculate the probability P(X<=k) that is X takes the value k or less than k.

P(X>=6)
= 1 - P(X<6)
[Please note that P(X>=k) = 1 - P(X<k) as the total probability is always 1]
= 1 - P(X<=5)
= 1 - binom.cdf(k=5,n=15,p=0.75)
So, the output of the below code will be the required probability:

import scipy.stats as stats
1-stats.binom.cdf(k=5,n=15,p=0.75)

Question 3
Correct Answer
Marks: 1/1

What is the difference between PDF and CDF?
PDF is used to find the absolute probability and CDF is used to find the cumulative probability

You Selected
CDF is used to find absolute probability and PDF is used to find cumulative probability.

Suppose X is a discrete random variable that follows a certain distribution, for example, Binomial Distribution. Then, the probability that X takes the value k, that is P(X=k) is an absolute probability, while the probability that X takes any value less than or equal to k, that is P(X<=k) is a cumulative probability. PDF function calculates the absolute probabilities while the CDF function calculates the cumulative probabilities. 

The PDF gives the probability density function, which describes the relative likelihood for a continuous random variable to take on a given value. It gives the probability of a specific outcome at a particular point in the distribution.

The CDF, on the other hand, gives the cumulative probability up to a certain value. It gives the probability that a random variable X takes on a value less than or equal to x, for any given value x. It describes the probability of a range of values up to that point, rather than the probability of a specific outcome at a particular point.

So, while the PDF is used to find the absolute probability at a specific point, the CDF is used to find the cumulative probability up to that point.


Question 4
Incorrect Answer
Marks: 0/1

73% is the probability that a cricket batsman will be out without making more than 10 runs during a rainy day.

If we select 5 players from a team of 11 players, which of the following code can be used to find the probability that at most 3 players will be out without making more than 10 runs during a rainy day?

from scipy.stats import binom
1 - binom.cdf(k = 3,n = 5, p = 0.73)
You Selected
from scipy.stats import binom
binom.cdf(k = 3,n = 5, p = 0.73)
Correct Option
from scipy.stats import binom
1 - binom.pmf(k = 3,n = 5, p = 0.73)            
from scipy.stats import binom
binom.pmf(k = 3,n = 5, p = 0.73)
The probability that at most 3 players will be out without making more than 10 runs during a rainy day is the probability P(X<=3).

Note that cdf() function calculates the probability that X takes a value less than or equal to k.

So, the output of the below code will give the required probability:

from scipy.stats import binom
binom.cdf(k = 3,n = 5, p = 0.73)