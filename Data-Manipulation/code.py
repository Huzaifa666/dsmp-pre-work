# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = df[df['fico'].astype(float) > 700].shape[0]/df.shape[0]
print(p_a)
p_b = df[df['purpose'] == 'debt_consolidation'].shape[0]/df.shape[0]
df1 = df[df['purpose'] == 'debt_consolidation']
p_a_b = df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]

result = p_a_b == p_a
# code ends here


# --------------
# code starts here
prob_lp = df[df['paid.back.loan'] == 'Yes']
length = len(prob_lp)
prob_lp = length / len(df)

prob_cs = df[df['credit.policy'] == 'Yes']
length = len(prob_cs)
prob_cs = length / len(df)


new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0]/new_df.shape[0]
bayes = prob_pd_cs* prob_lp / prob_cs
print(bayes)


# code ends here


# --------------
# code starts here
import seaborn as sns

sns.catplot(x="purpose", kind="count", palette="ch:.25", data=df);
df1 = df[df['paid.back.loan'] == 'No']
print(df1)

sns.catplot(x="purpose", kind='count', palette='ch:.25',data = df1)
# code ends here


# --------------
# code starts here
me = df['installment']
inst_mean = np.mean(me)
print(inst_mean)

inst_median = np.median(me)
print(inst_median)

print(df['installment'].hist())
print(df['log.annual.inc'])
# code ends here


