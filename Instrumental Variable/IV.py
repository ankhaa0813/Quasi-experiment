#Code for Instrumental variable approach and You will find information about context of the data and methodology from README file 
# for data cleaning and analysis 
import pandas as pd 
import numpy as np
# These libraries will be used for main econometric analysis 
import statsmodels as sm 
import statsmodels.formula.api as smf
import linearmodels.iv as IV
# main data will be called from this library which is also available in R software with same name
import wooldridge
#for visualiazation 
import matplotlib.pyplot as plt
import seaborn as sn
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
# In order to check whether our instumental variable satisfies relevance assumption we can see the correlation matrix of the dataframe
corr_data=card[['lwage', 'educ','nearc4', 'black', 'married', 'fatheduc', 'motheduc']] # getting subsample to make correlation matrix readable
corr_mat=corr_data.corr() #calculating corr matrix and saving it to corr_mat
sn.heatmap(corr_mat, annot=True) #drawing graph
plt.show() # show correaltoin matrix
#extracting fitted values from the 1st stage equation
educ_hat=fst_sta.fittedvalues
#2nd stage
sec_for ='lwage~educ_hat+IQ+exper+black+married+fatheduc+motheduc'
sec_sta =smf.ols(sec_for,data=card ).fit()
sec_sta.summary()  
# In order to implement IV regression with library, you need to use bracket for your endogenous variable, 
# for this case educ and isntrumenttal variable, nearc4
main_equation='lwage~1+IQ+exper+black+married+fatheduc+motheduc+[educ~nearc4]'
main_results =IV.IV2SLS.from_formula(main_equation,data=card ).fit()
# you can also imlement estimation without defining equation before
#main_results =IV.IV2SLS.from_formula(dependent=card['lwage'], exog=card[['IQ','exper','black','married', 'fatheduc' 'motheduc']], endog=card['educ'], instruments=card['nearc4']).fit()
main_results.summary
# in order to check the exclusion restriction, we can make some placebo test with different variable. 
# But it should be noted that checking exclusion restriction is very difficult to check emprically
placebo_equation='lwage~1+IQ+exper+black+married+fatheduc+motheduc+[educ~nearc2]' # here I used growing up near 2 years college as instrument for the educatio as purpose of place test
placebo_results =IV.IV2SLS.from_formula(placebo_equation,data=card ).fit()
placebo_results.summary