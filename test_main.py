import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self) : 
       fighand=plt.gca()
       figdat = fighand.get_lines()[0].get_xydata()
       this_x, this_y = zip(*figdat)
       figdat = fighand.get_lines()[2].get_xydata()
       this_x2, this_y2 = zip(*figdat)
       self.assertTrue( len(this_x)==200, "you graph has the wrong number of coordinates" )
       for i in range( len(this_x) ) :
           self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "the x-coordinates in your plot are incorrect" )
           bar = np.sqrt(rval*(1-pval)/pval/pval/(i+1))*st.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.fabs( this_y2[i]/this_y[i] - rval/pval )<bar, "the estimators appear to have been computed incorrectly" )
