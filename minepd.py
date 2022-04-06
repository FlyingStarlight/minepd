#mine_pd
from msilib.schema import Class
from xml.etree.ElementInclude import include
from mysqlx import Column
import numpy as np
from minepy import MINE
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def get_x_col(df, y_col):
    x_col = df.columns.difference(y_col)
    return list(x_col)

def to_np(df, x_col):
    np_data = {} #{xdata1, xdata2, ...}
    for x in x_col:
        np_data[x] = df[x].to_numpy()
    return np_data

def get_scores(x, y):
    mine = MINE(alpha=0.6, c=15, est="mic_approx")
    mine.compute_score(x, y)
    return get_stats(mine)


def compute_each_col(x_nps, y_nps):
    scores = {}
    for y in y_nps:
        for x in x_nps:
            # todo: return an df object
            scores[(x, y)] = get_scores(x_nps[x], y_nps[y])
    return scores

def get_scores_df(x_nps, y_nps):
    df_list = {}
    for y in y_nps:
        sdf = pd.DataFrame(columns=["mic", "mas", "mev", "mcn", "gmic", "tic"])
        #sdf.style.set_caption(y, inplace = True)    
        for x in x_nps:
            mine_score = get_scores(x_nps[x], y_nps[y])
            #mine_score["factors"] = str(x)
            df_t = pd.DataFrame(mine_score, index=[str(x)])
            sdf = sdf.append(df_t)
        sdf.rename_axis('Factors', inplace=True)
        df_list[y] = sdf
    return df_list

def get_stats(mine): #todo print
    return {"mic": mine.mic(),
            "mas": mine.mas(),
            "mev": mine.mev(),
            "mcn": mine.mcn(),
            "gmic": mine.gmic(),
            "tic": mine.tic()}

def get_mine(df, y_col):
    df = df.copy()
    str_col = df.select_dtypes(include="object").columns
    df[str_col] = df[str_col].astype("string")
    str_col = df.select_dtypes("string").columns.to_list()
    df = pd.get_dummies(df, columns=str_col, drop_first=False)
    x_col = get_x_col(df, y_col)
    x_nps = to_np(df, x_col)
    y_nps = to_np(df, y_col)
    return get_scores_df(x_nps, y_nps)

def get_matrix(df, type):
    df = df.copy()
    #todo get matrix by type

