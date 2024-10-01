people = {"Arham":"Blue", "Lisa":"Yellow","Vinod":"Purple","Jenny":"Pink"}

print(f"No. of students : {len(people)}")

# changing lisa colour
people["Lisa"] = "Black"
print(people)


# Removing Jenny
people.pop("Jenny")
print(people)

#Shorting dictnary on the bases of Name
sorted_dict = {key: people[key] for key in sorted(people)}
print(sorted_dict)
