#People in younger age groups are more stressed than others.
data.groupby(['hS3_age_group'])['Q1ra_is_stressed'].mean().plot()




import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

dinner_list = ['Plated_entrée','Pasta','Pizza','Salad','Sandwich','Grilled_Products','Meatloafs_Roasts']



#How and what People eat?
x, y, hue = "dinner_with","prop","last_remmbered_dinner"
from matplotlib.pyplot import show

f, axes = plt.subplots(ncols=1, nrows=2,sharey=True,figsize=(30,30))

prop_df = (data[hue]
.groupby(data[x])
.value_counts(normalize=True)
.rename(y)
.reset_index())

sns.barplot(x=x, y=y, hue=hue, data=prop_df[prop_df['last_remmbered_dinner'].isin(dinner_list)], ax=axes[1])


data['last_remmbered_dinner'].value_counts(normalize=True)
data[data['dinner_with'] == 'Children_aged_5_12']['last_remmbered_dinner'].value_counts(normalize=True)
data[data['dinner_with'] == 'ate_alone']['last_remmbered_dinner'].value_counts(normalize=True)
data[(data['hS3_age_group'].isin(['18-24','35-39'])) & (data['dinner_with'] == 'ate_alone') ]['last_remmbered_dinner'].value_counts(normalize=True)


# Average cooking time
print('Avg Cooking time overall :' ,data['total_time_spent_cooking_int'].mean())
print('Avg Cooking time for people who had dine with family with children:',data[data['dinner_with'] == 'Significant_other_and_children']['total_time_spent_cooking_int'].mean())
print('Avg Cooking time for people who had dine with family without children:',data[data['dinner_with'] == 'Significant_other']['total_time_spent_cooking_int'].mean())


#Does price sensitivity vary between genders?
x, y, hue = "Gender","percentage","Price_Sense"
from matplotlib.pyplot import show

f, axes = plt.subplots(ncols=1, nrows=2,sharey=True,figsize=(15,15))

prop_df = (data[hue]
.groupby(data[x])
.value_counts(normalize=True)
.rename(y)
.reset_index())

sns.barplot(x=x, y=y, hue=hue, data=prop_df, ax=axes[1])


#Are married and single people more price sensitive? 
x, y, hue = "Married","percentage","Price_Sense"
from matplotlib.pyplot import show

f, axes = plt.subplots(ncols=1, nrows=2,sharey=True,figsize=(15,15))

prop_df = (data[hue]
.groupby(data[x])
.value_counts(normalize=True)
.rename(y)
.reset_index())

sns.barplot(x=x, y=y, hue=hue, data=prop_df, ax=axes[1])


#Does price sensitivity vary among people of different educational backgrounds?
x, y, hue = "Education","percentage","Price_Sense"
from matplotlib.pyplot import show

f, axes = plt.subplots(ncols=1, nrows=2,sharey=True,figsize=(30,30))

prop_df = (data[hue]
.groupby(data[x])
.value_counts(normalize=True)
.rename(y)
.reset_index())

#Does price sensitivity vary among people of different work status?

sns.barplot(x=x, y=y, hue=hue, data=prop_df, ax=axes[1])

x, y, hue = "Work","percentage","Price_Sense"
from matplotlib.pyplot import show

f, axes = plt.subplots(ncols=1, nrows=2,sharey=True,figsize=(30,30))

prop_df = (data[hue]
.groupby(data[x])
.value_counts(normalize=True)
.rename(y)
.reset_index())

sns.barplot(x=x, y=y, hue=hue, data=prop_df, ax=axes[1])

/*Price Sensitivity by State*/
data.groupby(['D11'])['Q30rbc'].apply(lambda x: 100*(x[(x == 'Strongly agree') | (x == 'Agree somewhat')].count())/x.count()).reset_index(name='count')