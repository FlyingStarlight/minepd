# minepd
Maximal Information Coefficient(MIC) is a tool that can measure the relationship of a series of data, which provided in the Maximal Information-based Nonparametric Exploration (MINE) library

However, the original minepy is a bit mess because it aims to the core function, especially for only np support and print the result for a series of data.

Therefore, this project try to wrap Pandas and Plotly to ... eh ... Make MINE Great Again?(LOL) 

To be honest, this project target is to make MINE more easy to be used by myself, but I think someone will also like to try it.

## How
import minepd as mpd

mpd.get_mine(df, y_col)

df is the dataframe contains all data you want to evaluate

y_col is the targets or futures list, like ["heart_disease", "brain_disease"]

## Todo

requirement.txt

plot matrix function for the whole sets.

return the set of figure which are required, like mic > 0.1
