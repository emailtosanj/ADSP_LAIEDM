#From week1 project assessment
#Reference section
#error message
##TypeError: unsupported operand type(s) for &: 'str' and 'Categorical'

#rating is a category hence above logical operators combination wont work, because first one produces the series
#and second operation does not work because it is a category (string) data type and using comparison operator is invalid

#Hence two ways to solve this
#approach 1 - convert the data type using pd.to_numeric aftetr filtering the 'Not_given' rating record from the dataframe.

#approach 2 - apply the specific rating of 5 which is implicit since only rating 5 is defined in dataset after rating 4
#- which matched the requirement rating > 4.


#reference links
#https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html
#https://seaborn.pydata.org/
#https://seaborn.pydata.org/tutorial/color_palettes.html
#https://seaborn.pydata.org/generated/seaborn.heatmap.html
#https://pandas.pydata.org/docs/reference/series.html
#https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html#scipy.stats.binom
--

#Fundamentals (Hypothesis Testing)

### #Fundamental rule of choosing which test to be done

### #z-test - is done when the population standard deviation in known

### #t-test - is done when the population standard deviation is not known and is to be derived from sample data.

**Probability** is a theoretical likelihood, while **Proportion** is an observed fraction from a dataset.


Hypothesis testing depends on the parameter of interest being tested. 

Hence, the symbol or notation is different for it.

* When testing a hypothesis about a population proportion, as seen in your notebook, the Greek letter π (pi) is commonly used to represent the true population proportion. In this case, the null hypothesis might be stated as H₀: π = [some hypothesized value].

* When testing a hypothesis about a population mean, the Greek letter μ (mu) is typically used to represent the true population mean. The null hypothesis might be stated as H₀: μ = [some hypothesized value].

* When testing a hypothesis about a population standard deviation, the Greek letter σ (sigma) is often used.

* When testing a hypothesis about the difference between two population means, you might see notation like H₀: μ₁ - μ₂ = 0, or H₀: μ₁ = μ₂.

* When testing a hypothesis about the difference between two population proportions, you might see notation like H₀: π₁ - π₂ = 0, or H₀: π₁ = π₂.