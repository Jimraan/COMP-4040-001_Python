import pandas as pd

# Class notes from 19 Apr 2023, copied from pictures of the projected whiteboard

students = {'First Name': pd.Series(['John', 'Mary', 'Joshua', 'Jack', 'Adam', "Robert"]),
            'Last Name': pd.Series(['Doe', 'Jennings', 'Smith', 'Daniel', 'Henry', 'Matthew']),
            'Grade': pd.Series([90, 88, 96, 83]),
            'Section': pd.Series(['A', 'B', 'A', 'C', 'A', 'B'])}
df = pd.DataFrame(students)
print(df)
print()
grouped = df.groupby('Section')
print("grouped by section:")
print(grouped)
print("groups in grouped by section:")
print(grouped.groups)
print()

print("for name, group in grouped:")
for name, group in grouped:
    print(group)
print()

print("for index, row in df.iterrows(), print(:")
for index, row in df.iterrows():
    print("index"+str(index), "row"+str(row))