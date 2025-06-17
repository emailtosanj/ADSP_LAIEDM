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

--Python

# "*X[y == digit].T"
# code in double quotes

X -  refers to dataframe / numpy array.
"*" Feature for "unpacking" the elements of an iterable
(the transposed data for a specific digit) so they can be passed as separate arguments, 
most likely to a plotting function to plot the coordinates of those data points.

#Data Exploration and Visualization
path--MyDrive/adsp_laiedm/week_3_data_analysis_visualization/data_exploration_visualization
/practical_application/LVC_1_Practical_Application_Exploratory_Data_Analysis.ipynb

We have effectively reduced the dimensionality of the images, from 64 to 2, using t-SNE and PCA, and plotted the 2D embeddings and projections.
Out of the two methods used above, t-SNE takes a longer time to generate embeddings but gives better visualizations with well-separated clusters for each handwritten digit.
The annotations show that while PCA gives the same clusters, the overall plot represents more of a blob and is not as well-separated as t-SNE.
t-SNE is good for visualizing the data in lower dimensions but is very slow and should only be used on small datasets, whereas PCA is more computationally efficient and can be used on large datasets as well.

# PCA - Principal Component Analysis
The principal components are Eigenvectors of the sample Covariance Matrix.

L divergence - how or what is the unit of measure is for Kullbacl-Leibler divergence

For Kullback-Leibler (KL) divergence, the unit of measure depends on the base of the logarithm used in its calculation.

KL Divergence (units):
KL Divergence is used to meaure how one divergence differs from another.
In summary, the unit of measure for KL divergence is typically bits or nats, determined by the base of the logarithm used in its formula.

Bits: If the logarithm base is 2 , the unit is bits. This is often used when dealing with information theory and relates to the expected number of bits needed to encode samples from one distribution when using a code based on the other distribution.
Nats: If the logarithm base is the natural logarithm , the unit is nats. This is a more natural unit in mathematical contexts and is often used in machine learning and statistics.

K-Means:
K-Means is an iterative algorithm that tries to find the best possible placement for the cluster centroids to minimize the within-cluster sum of squares (WCSS).
Local Optimum: A good clustering solution, but potentially not the very best one. The algorithm stops here because it can't find a better solution by making small adjustments.
Global Optimum: The absolute best possible clustering solution that minimizes the objective function.
