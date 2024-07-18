import pandas as pd
#tasks
# pehle input le as a name
# phr us input ko list me change kar
# ek dictionary bana phr uss dictionary se key value match karwa apne name kki,
# then uske corresponding value ki ek list bun jae .
name=input().upper()
stripped_name=name.strip().replace(" ","")
name_letter_list=list(stripped_name)
print(name_letter_list)

#new method i.e list comprehension
# list=[i for i in name if i!=' ']
# print(list)

df=pd.read_csv("nato.csv")
print(df)

dict_of_names={row.letter:row.code for index,row in df.iterrows()}
print(dict_of_names)

list_of_selected_words=[dict_of_names[letter] for letter in name_letter_list]
print(list_of_selected_words)