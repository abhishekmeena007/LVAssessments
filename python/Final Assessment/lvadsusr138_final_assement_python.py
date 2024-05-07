# -*- coding: utf-8 -*-
"""LVADSUSR138_Final_Assement_python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-mpPtUCYT-vYH6-OO3jQmZ6TeIH9mMZn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#question 1(a)
df = pd.read_csv('/content/Final Dataset - IPL.csv')
df

#question1(b)
df.info()

print(df.isnull())

#question2(a)
missing_value = df.isnull
print(missing_value)

#filling 0 in missing value
df.fillna(0)

#question2(b)
df.drop_duplicates(inplace=True)
print(len(df))

#question3
mean = df.select_dtypes(include='number').mean()
median = df.select_dtypes(include='number').median()
mode = df.select_dtypes(include='object').mode().iloc[0]
variance = df.select_dtypes(include='number').var()
std = df.select_dtypes(include='number').std()

print("Mean:")
print(mean)
print("\nMedian:")
print(median)
print("\nMode:")
print(mode)
print("\nVariance:")
print(variance)
print("\nStandard Deviation:")
print(std)

#question4
print('Visual Plots :')
plt.figure(figsize=(8, 6))
plt.hist(df['first_ings_score'], bins=12, color='blue')
plt.title('First Innings Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(7, 5))
plt.scatter(df['first_ings_score'], df['second_ings_score'], color='red')
plt.title('First Innings Score vs Second Innings Score')
plt.xlabel('First Innings Score')
plt.ylabel('Second Innings Score')
plt.show()

plt.figure(figsize=(10, 6))
df.boxplot(column='second_ings_score', by='team2')
plt.title('Second Innings Score by Team 2 box plot')
plt.ylabel('Seocnd Innings Score')
plt.xlabel('Team 2')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(8, 6))
team_counts = df['team1'].value_counts()
team_counts.plot(kind='bar', color='pink')
plt.title('Each team total matches')
plt.xlabel('Team')
plt.ylabel('Number of Matches')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(8, 6))
match_winner_counts = df['match_winner'].value_counts()
match_winner_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Match Winners')
plt.ylabel('')
plt.show()

#question5
df['toss_decision'] = df['toss_decision'].map({'Batting': 0, 'Fielding': 1})
ques = ['toss_decision', 'first_ings_score', 'second_ings_score']
ans = df[ques].corr()
print(ans)

plt.figure(figsize=(5, 4))
sns.heatmap(ans)
plt.title('Heatmap showing correlation')
plt.show()

#question6
def rem_out(df, column):
    a = df[column].quantile(0.3)
    b = df[column].quantile(0.7)
    x = b - a
    low = a - 1.5 * x
    upp = b + 1.5 * x
    return df[(df[column] >= low) & (df[column] <= upp)]

col = ['first_ings_score', 'first_ings_wkts', 'second_ings_score', 'second_ings_wkts', 'highscore']

for column in col:
    df = rem_out(df, column)

print("after removing:")
print(df)

plt.figure(figsize=(5, 4))
sns.boxplot(data=df[['first_ings_score', 'second_ings_score']])
plt.title('Box Plot')
plt.ylabel('Score')
plt.xlabel('Innings')
plt.show()

#question7(a)
x1 = df.groupby(['venue', 'team1']).agg({'first_ings_score': 'sum', 'first_ings_wkts': 'sum'}).reset_index()
print(x1)
x1['batting_average'] = x1['first_ings_score'] / x1['team1'].count()
x1['bowling_average'] = x1['first_ings_score'] / x1['first_ings_wkts']

plt.figure(figsize=(10, 6))
sns.barplot(data=x1, x='venue', y='first_ings_score', hue='team1')
plt.title('Runs scored at a Venue vs team for first innings')
plt.xlabel('Venue')
plt.ylabel('Total Runs')
plt.xticks(rotation=90)
plt.show()

#question7(b)
x1 = df.groupby(['venue', 'team2']).agg({'second_ings_score': 'sum', 'second_ings_wkts': 'sum'}).reset_index()
print(x1)
x1['batting_average'] = x1['second_ings_score'] /  x1['team2'].count()
x1['bowling_average'] = x1['second_ings_score'] / x1['second_ings_wkts']

plt.figure(figsize=(10, 6))
sns.barplot(data=x1, x='venue', y='second_ings_score', hue='team2')
plt.title('Runs scored at a Venue vs team for first innings')
plt.xlabel('Venue')
plt.ylabel('Total Runs')
plt.xticks(rotation=90)
plt.show()

#question8(a)
potm = df['player_of_the_match'].value_counts()
winner = potm.idxmax()
max_win = potm.max()

print(f"'Player of the Match' award given for maximum times is: {winner} (Won {max_win} times)")

#question8(b)
# Top Scorers Plot
plt.figure(figsize=(10, 6))
df_top_scorers = df[['top_scorer', 'highscore']].drop_duplicates().nlargest(6, 'highscore')
plt.bar(df_top_scorers['top_scorer'], df_top_scorers['highscore'], color='skyblue')
plt.title('Top Scorers')
plt.xlabel('Player')
plt.ylabel('High Score')
plt.xticks(rotation=90)
plt.show()

# Best Bowlers Plot
plt.figure(figsize=(10, 5))
df_best_bowlers = df[['best_bowling', 'best_bowling_figure']]
plt.bar(df_best_bowlers['best_bowling'], df_best_bowlers['best_bowling_figure'], color = 'red')
plt.title('Best Bowlers')
plt.xlabel('Player')
plt.ylabel('Best Bowling Figure')
plt.xticks(rotation=45)
plt.show()

#question9
print('Summary: ')
print('Mean, median, Mode, variance, standard deviation :')
mean = df.select_dtypes(include='number').mean()
median = df.select_dtypes(include='number').median()
mode = df.select_dtypes(include='object').mode().iloc[0]
variance = df.select_dtypes(include='number').var()
std = df.select_dtypes(include='number').std()

print("Mean:")
print(mean)
print("\nMedian:")
print(median)
print("\nMode:")
print(mode)
print("\nVariance:")
print(variance)
print("\nStandard Deviation:")
print(std)

print('Both teams scores :')

plt.figure(figsize=(8, 6))
plt.hist(df['first_ings_score'], bins=12, color='blue')
plt.title('First Innings Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
df.boxplot(column='second_ings_score', by='team2')
plt.title('Second Innings Score by Team 2 box plot')
plt.ylabel('Seocnd Innings Score')
plt.xlabel('Team 2')
plt.xticks(rotation=90)
plt.show()

potm = df['player_of_the_match'].value_counts()
winner = potm.idxmax()
max_win = potm.max()

print(f"'Player of the Match' award given for maximum times is: {winner} (Won {max_win} times)")

print('Top scorers and Best bowlers overall :')
# Top Scorers Plot
plt.figure(figsize=(10, 6))
df_top_scorers = df[['top_scorer', 'highscore']].drop_duplicates().nlargest(6, 'highscore')
plt.bar(df_top_scorers['top_scorer'], df_top_scorers['highscore'], color='skyblue')
plt.title('Top Scorers')
plt.xlabel('Player')
plt.ylabel('High Score')
plt.xticks(rotation=90)
plt.show()

# Best Bowlers Plot
plt.figure(figsize=(10, 5))
df_best_bowlers = df[['best_bowling', 'best_bowling_figure']]
plt.bar(df_best_bowlers['best_bowling'], df_best_bowlers['best_bowling_figure'], color = 'red')
plt.title('Best Bowlers')
plt.xlabel('Player')
plt.ylabel('Best Bowling Figure')
plt.xticks(rotation=45)
plt.show()