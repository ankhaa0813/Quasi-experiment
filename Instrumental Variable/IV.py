
# for data cleaning and analysis 
import pandas as pd 
import numpy as np
# These libraries will be used for main econometric analysis 
import statsmodels as sm 
import statsmodels.formula.api as smf
import linearmodels.iv as IV
# main data will be called from this library which is also available in R software with same name
# it is very easy accessible from different development environment such as JupiterNote, VScode
import wooldridge
#for visualiazation 
import matplotlib.pyplot as plt
# calling data and its description
card=wooldridge.data('card')
# save it as data frame using panda
# Information about  DATA and METHODOLOGY are found from README file
card=pd.DataFrame(card)
#data description
df = wooldridge.data('card', description=True)
card.head
#1st stage
fst_for ='educ~nearc4+IQ+exper+black+married+fatheduc+motheduc'
# with several potantial control variables
fst_sta =smf.ols(fst_for,data=card ).fit()
fst_sta.summary() # to see the result in table
#extracting fitted values from the 1st stage equation
educ_hat=fst_sta.fittedvalues
#2nd stage
sec_for ='lwage~educ_hat+IQ+exper+black+married+fatheduc+motheduc'
sec_sta =smf.ols(sec_for,data=card ).fit()
sec_sta.summary()  
# In order to implement IV regression with library, you need to use bracket for your endogenous variable, 
# for this case educ, and isntrumenttal variable, nearc4
main_equation='lwage~1+IQ+exper+black+married+fatheduc+motheduc+[educ~nearc4]'
main_results =IV.IV2SLS.from_formula(main_equation,data=card ).fit()
# you can also imlement estimation without defining equation before
#main_results =IV.IV2SLS.from_formula(dependent=card['lwage'], exog=card[['IQ','exper','black','married', 'fatheduc' 'motheduc']], endog=card['educ'], instruments=card['nearc4']).fit()
main_results.summary