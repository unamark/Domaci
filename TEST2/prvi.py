from pandas import *

f = read_csv('dailyActivity_merged.csv')
ime = ['Id', 'ActivityDate', 'TotalSteps', 'TotalDistance', 'TrackerDistance', 'LoggedActivitiesDistance', 'VeryActiveDistance', 'ModeratelyActiveDistance',
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


max_val = max(Ts)
min_val = min(Ts)
print(max_val, min_val)
print(f[ime].abs)
print(abs(max_val - f['TotalSteps'].abs)*100)
