import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

exercise_df = sns.load_dataset('exercise')

print("Original Exercise Dataset: ")
print(exercise_df.head())

running_data = exercise_df.loc[exercise_df["kind"] == 'running']

one_min_data = running_data.loc[running_data['time'] == '1 min',['id','pulse']]

thirty_min_data = running_data.loc[running_data['time']=='30 min',['id','pulse']]

fitness_merge = one_min_data.merge(thirty_min_data,on='id',suffixes=('_1_minute','_30_minutes'))

print("\nMerged Fitness Data: ")
print(fitness_merge)

fitness_merge['pulse_progress'] = (fitness_merge['pulse_30_minutes']-fitness_merge['pulse_1_minute'])

fitness_merge = fitness_merge.sort_values("pulse_progress",ascending=False)

print("\n Sorted Fitness Progress: ")
print(fitness_merge)

participant_names = ["Participant" +str(participant_id) for participant_id in fitness_merge['id']]

fitness_data = {'participant': participant_names,'pulse_1_minute':fitness_merge['pulse_1_minute'].tolist(),'pulse_30_minutes':fitness_merge['pulse_30_minutes'].tolist()}

chart_df = pd.DataFrame(fitness_data)

print("\n Chart Data: ")
print(chart_df)

positions = np.arange(len(chart_df['participant']))

bar_width = 0.35

plt.figure(figsize=(12,7))

one_min_bars = plt.bar(positions - bar_width/2, chart_df['pulse_1_minute'], width=bar_width, label='After 1 minute')

thirty_min_bars = plt.bar(positions + bar_width/2, chart_df['pulse_30_minutes'], width=bar_width, label='After 30 minutes')

plt.title('Running Exercise Pulse Comparison')
plt.xlabel('Participant')
plt.ylabel("Pulse Rate")

plt.xticks(positions,chart_df['participant'],rotation=45)

plt.legend()

for bar in one_min_bars:
    value = bar.get_height()
    plt.annotate(str(value), xy=(bar.get_x() + bar.get_width()/2, value), xytext=(0,3), textcoords='offset points', ha='center', va='bottom')

for bar in thirty_min_bars:
    value = bar.get_height()
    plt.annotate(str(value), xy=(bar.get_x() + bar.get_width()/2, value), xytext=(0,3), textcoords='offset points', ha='center', va='bottom')

plt.tight_layout()
plt.show()