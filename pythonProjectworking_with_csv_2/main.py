import pandas as pd
df=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_colored_squirrel=df[df["Primary Fur Color"]=="Gray"]
black_colored_squirrel=df[df["Primary Fur Color"]=="Black"]
cinnamon_colored_squirrel=df[df["Primary Fur Color"]=="Cinnamon"]

#total number of squerrel of each color
grey_colored_squirrel_count=len(grey_colored_squirrel)
black_colored_squirrel_count=len(black_colored_squirrel)
cinnamon_colored_squirrel_count=len(cinnamon_colored_squirrel)

print(grey_colored_squirrel_count)
print(black_colored_squirrel_count)
print(cinnamon_colored_squirrel_count)

#to create a dataframe the best way is to create a dictionary
dictionary_of_squerllel_data={
    "Primary Fur Color":["Gray","Black","Red"],
    "Number Of Squerrel in area":[grey_colored_squirrel_count,black_colored_squirrel_count,cinnamon_colored_squirrel_count]
}

new_dataframe=pd.DataFrame(dictionary_of_squerllel_data)
print(new_dataframe)
new_dataframe.to_csv("new_data_for_each_squerrel")
