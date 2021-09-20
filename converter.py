#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# # Read Input xlsx files

# In[9]:


df_conversation = pd.read_excel("./data/japanese_persona_chat.xlsx", sheet_name="対話")
df_conversation


# In[5]:


df_persona = pd.read_excel("./data/japanese_persona_chat.xlsx", sheet_name="ペルソナリスト")
df_persona


# In[89]:


df_user[0:1]["発話"].values[0]


# In[112]:


df_groupby = df_conversation.groupby(["No","ペルソナID"])
df_outputA = pd.DataFrame(columns=["ペルソナID","A1","B1","A2"])
for i in range(1, df_conversation["No"].max()+1):
    df_user = df_groupby.get_group((i,f"PP{i}"))
    for j in range(0,len(df_user)-2,2):
        df_outputA = df_outputA.append(
            {
                "ペルソナID":f"PP{i}",
                "A1":df_user[j:j+1]["発話"].values[0],
                "B1":df_user[j+1:j+2]["発話"].values[0],
                "A2":df_user[j+2:j+3]["発話"].values[0]
            },
            ignore_index=True
        )
df_outputA


# In[117]:


df_groupby = df_conversation.groupby(["No","ペルソナID"])
df_outputB = pd.DataFrame(columns=["ペルソナID","A1","B1","A2"])
for i in range(1, df_conversation["No"].max()+1):
    df_user = df_groupby.get_group((i,f"PP{i}"))
    for j in range(0,len(df_user)-3,2):
        df_outputB = df_outputB.append(
            {
                "ペルソナID":f"PP{i}",
                "B1":df_user[j+1:j+2]["発話"].values[0],
                "A1":df_user[j+2:j+3]["発話"].values[0],
                "B2":df_user[j+3:j+4]["発話"].values[0]
            },
            ignore_index=True
        )
df_outputB


# # Output to text file

# In[ ]:


with open("./j_perchat.txt", mode="w", encoding="utf-8") as f:
    for pid in df_persona["ペルソナID"].unique().tolist():
        i = 1
        # ペルソナの書き出し
        for persona in df_persona[df_persona["ペルソナID"]==pid]["A"].values[0].split("\n"):
            f.write(f"{i} your persona: {persona}\n")
            i+=1
        # 対話ペアの書き出し
        for index, row in df_outputA[df_outputA["ペルソナID"]==pid].iterrows():
            f.write(f'{i} {row["A1"]}\t{row["B1"]}\t{row["A2"]}\n')
            i+=1
        i = 1
        # ペルソナの書き出し
        for persona in df_persona[df_persona["ペルソナID"]==pid]["B"].values[0].split("\n"):
            f.write(f"{i} your persona: {persona}\n")
            i+=1
        # 対話ペアの書き出し
        for index, row in df_outputB[df_outputB["ペルソナID"]==pid].iterrows():
            f.write(f'{i} {row["B1"]}\t{row["A1"]}\t{row["B2"]}\n')
            i+=1         
    


# # Convert .ipynb to .py

# In[ ]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'script', '*.ipynb'])

