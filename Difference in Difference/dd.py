
import pandas as pd
import wooldridge
import statsmodels as sm
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
housing=wooldridge.data('kielmc')
df = wooldridge.data('kielmc', description=True)
housing.head
# Data is used from Kiel and Mcclain(1995) which is used in Wooldrige book 
# We will estimate effect of building a new incinerator on housing prices in North Andover, Massachusetts. 
# The rumor about building a new incinerator began after 1978, construction began in 1981. 
# We will compare difference between before and after the rumor and difference between houses located close to incinerator as treatment and more distant ones as control
house=pd.DataFrame(housing)
y=housing['price']
x= house.loc["age","rooms", "area", "nbh", "nearinc"]
control=house.loc["age","rooms", "area", "nbh"]
lr=LinearRegression()
house['loca']=house.nearinc,map({1:'near', 0:'far'})
#pd.get_dummies(train, columns=["Sex", "Embarked"], drop_first=True)
pd.get_dummies(house.year) #column for each possible answer
pd.get_dummies(house.year).iloc[:,1:] #drop first column first : mean all columns 
pd.get_dummies(house.year, prefix='Post').iloc[:,1:] #add prefix into the name
# pd concat addd row to the variable to the original data frame axis-=1 for columns axis=0 for the rows s

house['year1']=house['year'].replace([1978],'pre')
house['year1']=house['year'].replace([1981],'post')
house.head
xb['nearinc']=xb['nearinc'].replace(['1'],'near to incinerator ')

def post(time, treatment):
    if time>treatment:
        return 1
    if time<=treatment:
        return 0
treatment=1978
year=house['year']
house["year"]=post(year, treatment)
print(year)
print(treatment)
house["po"]=house['nearinc']*house['y81']
results = smf.ols('lrprice ~ y81*nearinc+age+area+rooms+nbh',data=house ).fit()
print(results.summary())
aa=results.fittedvalues
xa=pd.DataFrame(house.groupby(['nearinc', 'year']).agg({'rprice': ['mean']}))

print(xb)
print(xb['rpice'])
xb=xb.rows.droplevel(level=0)
house.columns
hous=house[['year','nearinc','rprice']]
y=hous.groupby(['year','nearinc']).mean()
xb=y.reset_index()

print(xb)
xb.columns
xb['nearinc']=xb['nearinc'].replace([0],'far from incinerator ')
xb['nearinc']=xb['nearinc'].replace([1],'near to incinerator ')
a=pd.DataFrame{(x['rprice'],y['rprice']),index=[1978, 1981]}
xb.plot.line('year rpice)
print(lines)
xb.plot.line()
sns.lineplot(data = xb, x = 'year', y = 'rprice', hue = 'nearinc')
plt.show()
print(xb)
xb.set_index('year', inplace=True)
xb.groupby('nearinc')['rprice'].plot(legend=True)
plt.plot(house.year, house.rprice)
plt.show()

plt.plot(xb.year, xb.rprice)
ax1=fig.add_subplot(11)
near=ax1.plot(xb.rprice)
plt.show()

p_df = pd.DataFrame({"class": classes, "vals": vals})

fig, ax = plt.subplots(figsize=(8,6))
for label, df in xb.groupby('nearinc'):
    xb.rprice.plot(kind="kde", ax=ax, label=label)
plt.show()
print(xb)
plt.figure(figsize = (10, 5))
xb.set_index('year', inplace=True)
plt.axvline(x = 1979, color = 'b', label = 'axvline - full height')
xb.groupby('nearinc')['rprice'].plot(legend=True)
plt.show()
