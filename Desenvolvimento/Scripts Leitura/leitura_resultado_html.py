import pandas as pd

list_megasenna = pd.read_html("D_MEGA.HTM")

df_megasenna = pd.concat(list_megasenna)
df_megasenna.to_csv("D_MEGA.csv",sep=";", encoding="utf-8")