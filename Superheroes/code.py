# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
bar = gender_count.hist()

#Code starts here 




# --------------
#Code starts here
alignment = data["Alignment"].value_counts()
pie = alignment.plot.pie()


# --------------
sc_df = data.loc[:,['Strength', 'Combat']]
def covariance(x, y):
  x_mean = x.mean()
  y_mean = y.mean()
  diff_x=[]
  diff_y=[]
  count = 0
  for i in x:
      diff_x.append(i-x_mean)
      count+=1
  for i in y : 
    diff_y.append(i - y_mean) 
  di = [x*y for x,y in zip(diff_x, diff_y)]
  dj = sum(di)/count
  return dj

sc_covariance = 617.49

sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = sc_covariance / (sc_strength * sc_combat)
print(sc_pearson)

ic_df = data.loc[:,['Intelligence', 'Combat']]
ic_covariance = 853.42
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson = ic_covariance / (ic_intelligence * ic_combat)
print(ic_pearson)


# --------------
#Code starts here
total_high = data['Total'].quantile(q=0.99)
supers = data.loc[:, 'Total']
#print(supers)
super_best =[]
for i in supers:
    if i > total_high:
        super_best.append(i)
print(super_best)

supers1= data.loc[:,['Name', 'Total']]
super_best = supers1.loc[(supers1['Total'] > total_high)]
super_best_names = list(super_best.loc[:,'Name'])
print(super_best_names)



# --------------
#Code starts here
ax_1 = plt.subplot2grid((1,3),(0,0))
ax_1.plot(data['Intelligence'])
plt.title('Intelligence')

ax_2 = plt.subplot2grid((1,3),(0,1))
ax_2.plot(data['Speed'])
plt.title('Speed')

ax_3 = plt.subplot2grid((1,3),(0,2))
ax_3.plot(data['Power'])
plt.title('Power')

plt.show()


