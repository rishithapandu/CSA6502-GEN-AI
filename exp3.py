import pandas as pd

n = int(input("Enter number of students: "))

name = []
marks = []

for i in range(n):
    name.append(input("Enter student name: "))
    m = input("Enter marks (leave blank for missing): ")
    if m == "":
        marks.append(None)
    else:
        marks.append(float(m))

df = pd.DataFrame({"Name": name, "Marks": marks})

print("\nOriginal Dataset:")
print(df)

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nCleaned Dataset:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Score:", df["Marks"].max())

