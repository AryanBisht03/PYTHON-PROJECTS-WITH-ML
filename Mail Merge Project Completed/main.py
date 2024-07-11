placeholder="[name]"

names_file=open("./Input/Names/invited_names.txt")
names=names_file.readlines()
print(names)
#readlines method returns the file content as a list.

letter_file=open("./Input/Letters/starting_letter.txt")
content=letter_file.read()
print(content)

for name in names:
    stripped_name=name.strip()
    new_letter=content.replace(placeholder,stripped_name)
    # print(new_letter)
    #now writing the new letters and stroing them into a seperate files by their names
    completed_letter=open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w")
    new_content=completed_letter.write(new_letter)