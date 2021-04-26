#%%
import pandas as pd 
df = pd.read_csv("csgo_round_snapshots_less_col.csv")
#%%
print(set(df["map"]))

df = pd.get_dummies(df, columns=["map"])
df.head()
# %%
df["round_winner"].replace(
    to_replace=['CT', 'T'],
    value=[0, 1],
    inplace=True
)

df["Terrorists_win"] = df["round_winner"]
df.drop(["round_winner"], axis=1, inplace=True)
# %%
df.head()
# %%
df.to_csv("cleaned_csgo.csv")
# %%
# one hot encode maps