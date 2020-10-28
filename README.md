# Method of moments for the negative binomial random variable

The probablity mass function for the negative binomial random variable is:

![](https://render.githubusercontent.com/render/math?math=P(X=x)=\binom{x-1}{r-1}p^r(1-p)^{x-r})

This distribution function is a funciton of two parameters and we can derive the following expressions for the expectation and variance of the random variable:

![](https://render.githubusercontent.com/render/math?math=\mathbb{E}(X)=\frac{r}{p}\qquad\textrm{var}(X)=\frac{r(1-p)}{p^2})

Furthermore, we have also established that we can estimate the sample mean and the second central moment about the mean (the variance) by sampling the random variable ![](https://render.githubusercontent.com/render/math?math=X_i) multiple times and then using:

![](https://render.githubusercontent.com/render/math?math=\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_i\qquad\widehat{\mu_2}=\frac{1}{n}\sum_{i=1}^{n}(X_i-\overline{X})^2)

__Your task in this exercise is to use the method of moments to derive estimators for the parameters of a negative binomial.  You should then write a program to plot how the values of these estimators change as the number of samples they are computed from increases just as you did for the Bernoulli, geometric and binomial random variables.__

To complete the exercise you will need to  

1. Finish the function `negative_binomial`. This function should take two parameters `r` and `p`. It should return a negative binomial random variable from a distribution with parameters `r` and `p`. 
2. Set the first element of the list called `indices` equal to 1, the second element of the list called `indices` to 2 and so on.
3. Set the first element of the list called `p_estimator` equal to an estimate of the p parameter of the distribution that is calculated by generating 1 negative binomial random variable with parameters `rval` and `pval`, the second element of the list `p_estimator` equal to an estimate of the p parameter of the distribution that is calculated by generating 2 negative binomial random variables with parameters `rval` and `pval`, set the third element of the list called `p_estimator` equal to an estimate of the parameter of the distribution that is calculated by generating 3 negative binomial random variables with parameters `rval` and `pval` and so on until you have computed an estimate of the p parameter of the distribution from 200 negative binomial random variables. 
4. Set the first element of the list called `r_estimator` equal to an estimate of the r parameter of the distribution that is calculated by generating 1 negative binomial random variable with parameters `rval` and `pval`, the second element of the list `r_estimator` equal to an estimate of the p parameter of the distribution that is calculated by generating 2 negative binomial random variables with parameters `rval` and `pval`, set the third element of the list called `r_estimator` equal to an estimate of the parameter of the distribution that is calculated by generating 3 negative binomial random variables with parameters `rval` and `pval` and so on until you have computed an estimate of the r parameter of the distribution from 200 negative binomial random variables. 

When your code is complete a graph will be generated.  The red dots are the values of the method of moments estimator for the p parameter of the distribution you sampled from.  The black dashed line is then the true value of the parameter.  The blue dots are the values of the method of moments estimator for the r parameter of the distribution you sampled from.  The green dashed line is then the true value of the parameter.  
