
# for data cleaning and analysis 
from sre_parse import DIGITS
import pandas as pd 
import numpy as np
# These packages will be used for main econometric analysis 
import statsmodels as sm 
import statsmodels.formula.api as smf
# main data will be called from this package which is also available in R software with same name
# it is very easy accessible from different development environment such as JupiterNote, VScode
import wooldridge
#for visualiazation 
import matplotlib.pyplot as plt
# calling data
housing=wooldridge.data('kielmc')
# #data descriptionn
housing = wooldridge.data('kielmc', description=True)
# save it as data frame using panda
house=pd.DataFrame(housing)
# to see the first few rows of data
house.head
# dummy variable plays important role in DinD estimation, u can create dummy variable same as below. But we don't use it now because 
# we have already pcreated variables in dataset we downloaded from wooldridge package
# it is easy to define estimation equation beforehand. We can just create interaction term with * sign within formula like R
basic ='rprice~y81+nearinc+y81*nearinc'
# I don't want waste time on explaining variables which can be found from result of code in line 15
r_basic = smf.ols(basic,data=house ).fit()
#r_basic = smf.ols(rprice~y81+nearinc+y81*nearinc,data=house ).fit() # you can also do it without formula
r_basic.summary() # we can find exact same result with Wooldridge book
# I hope u can explain the result. otherwise you can find from the Wooldridge book. 
#Adding some controls
basic_control ='rprice~y81+nearinc+y81*nearinc+age+agesq'
# I don't want waste time on explaining variables which can be found from result of code in line 15
r_basic_control = smf.ols(basic_control,data=house ).fit()
r_basic_control.summary()
# Drawing graph showing mean of house price before and after the rumor
hous=house[['year','nearinc','rprice']] #creating subsample to make process easy
y=hous.groupby(['year','nearinc']).mean() #finding mean of subsample using year and nearinc with panda package
plot1=y.reset_index() #formating table index
print(plot1)
#replacing value of the variable nearinc to make graph more understanbale 
plot1['nearinc']=plot1['nearinc'].replace([0],'Far from incinerator ')
plot1['nearinc']=plot1['nearinc'].replace([1],'Near to incinerator ')
# Creating plot with matplotlib
plt.figure(figsize = (10, 5)) #defining size of the plot
plot1.set_index('year', inplace=True) #defining index of the plot or x axis
plt.axvline(x = 1979, color = 'b', label = '') # drawing vertical line
plot1.groupby('nearinc')['rprice'].plot(legend=True)  # main part for the plot assigning main variable that we want to see in the graph
plt.show()
