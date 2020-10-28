import matplotlib.pyplot as plt
import numpy as np

def negative_binomial(r,p) :
  # Your code to generate the binomial random variable goes here
  
  
pval, rval = 0.8, 3
ssum, ssum2, indices, p_estimator, r_estimator = 0, 0, np.zeros(200), np.zeros(200), np.zeros(200)
for i in range(200) : 
  # Add code to setup the numpy arrays called indices, p_estimator and r_estimator to generate the desired
  # plot here.
  
  
  
# This will plot the graph for the data.  You should not need to adjust this.
plt.plot( indices, p_estimator, 'ro' )
plt.plot( [0,200], [pval,pval], 'k--' )
plt.plot( indices, r_estimator, 'bo' )
plt.plot( [0,200], [rval,rval], 'g--' )
plt.xlabel("Number of random variables")
plt.ylabel("Estimator")
plt.savefig("negative_binomial_estimator.png")
