import pandas as pd

f = pd.read_csv('dailyActivity_merged.csv')
ime = ['Id', 'TotalSteps', 'TotalDistance', 'TrackerDistance', 'LoggedActivitiesDistance', 'VeryActiveDistance', 'ModeratelyActiveDistance',
       'LightActiveDistance', 'SedentaryActiveDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes', 'Calories']

Ts = f['TotalSteps'].tolist()
Ad = f['ActivityDate'].tolist()
Id = f['Id'].tolist()
Td = f['TotalDistance'].tolist()
TDd = f['TrackerDistance'].tolist()
lad = f['LoggedActivitiesDistance'].tolist()
vaa = f['VeryActiveDistance'].tolist()
m = f['ModeratelyActiveDistance'].tolist()
laad = f['LightActiveDistance'].tolist()
sad = f['SedentaryActiveDistance'].tolist()
vad = f['VeryActiveMinutes'].tolist()
fad = f['FairlyActiveMinutes'].tolist()
lam = f['LightlyActiveMinutes'].tolist()
sm = f['SedentaryMinutes'].tolist()
cal = f['Calories'].tolist()

abs_val = f[ime].abs()

max_val = f['TotalSteps'].max()
min_val = f['TotalSteps'].min()
mean_val = f['TotalSteps'].mean()
print(max_val, min_val)
print(abs_val)
print((max_val - mean_val)/mean_val*100)

f['TotalSteps'] = (f['TotalSteps'] - min_val) / (max_val - min_val)
f.to_csv('_normalized.csv', index=False)


cor_mat = f.corr()
max_pos = cor_mat.unstack().sort_values().drop_duplicates().iloc[-3:-1]
max_neg = cor_mat.unstack().sort_values().drop_duplicates().head(2)
print(max_pos, max_neg)
