#Code for Difference and Difference approach and You will find information about context of the data and methodology from README file 
# for data cleaning and analysis 
import pandas as pd 
import numpy as np
# These libraries will be used for main econometric analysis 
import statsmodels as sm 
import statsmodels.formula.api as smf
# main data will be called from this library which is also available in R software with same name
# this data is very easy to implement DinD approach without data cleaning
import wooldridge
#for visualiazation of the data
import matplotlib.pyplot as plt
# #data descriptionn
housing = wooldridge.data('kielmc', description=True)
# calling data
# Information about  DATA and METHODOLOGY are found from README file
housing=wooldridge.data('kielmc')
# save it as data frame using panda
house=pd.DataFrame(housing)
# to see the first few rows of data to inspect it
house.head
# dummy variable plays an important role in DinD estimation, u can create dummy variable same as below. But we don't use it now because 
# we have already pre-built variables in dataset we downloaded from wooldridge library
# pd.get_dummies(house.year)
# it is easy to define estimation equation beforehand. We can just create interaction term with * sign within formula like R
basic ='rprice~y81+nearinc+y81*nearinc'
# I don't want waste time on explaining variables which can be found from result of code in line 15 or from the original paper
r_basic = smf.ols(basic,data=house ).fit()
#r_basic = smf.ols(rprice~y81+nearinc+y81*nearinc,data=house ).fit() # you can also do it without formula
r_basic.summary() # we can find exact same result with Wooldridge book
# I hope u can explain the result. otherwise you can find from the Wooldridge book or the original paper 
#Adding some controls
basic_control ='rprice~y81+nearinc+y81*nearinc+age+agesq'
# I don't want waste time on explaining variables which can be found from result of code in line 15
r_basic_control = smf.ols(basic_control,data=house ).fit()
r_basic_control.summary()
# Drawing graph showing the mean of house price before and after the rumor
hous=house[['year','nearinc','rprice']] #creating subsample to make process easy
y=hous.groupby(['year','nearinc']).mean() #finding mean of subsample using year and nearinc with panda library
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
# You can also conduct some placebo estimations as a robustness check
# here I implemented place test using score of neighborhood. Conceptually, rumor about a new garbage incinerator doesn't have to effect score of neighborhood
placebo =' nbh~y81+nearinc+y81*nearinc'
r_placebo = smf.ols(placebo,data=house ).fit()
r_placebo.summary()