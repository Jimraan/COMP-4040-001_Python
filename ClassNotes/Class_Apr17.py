# Python Pandas DataFrames are two-dimensional data structures

import pandas as pd

# *Example 1*
# numbers = [10, 20, 30, 40, 50]  # results in a single column
# numbers = [[10], [20], [30], [40], [50]]  # results in a single column
# numbers = [[10, 20, 30, 40, 50]]  # results in a single row
# numbers = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100],
#            [120, 140, 160, 180, 200], [220, 240, 260, 280, 300]]
# df = pd.DataFrame(numbers)
# print(df)


# *Example 2*
# students = [['John', 'Doe', 90], ['Mary', 'Jennings', 88], ['Joshua', 'Smith', 96], ['Jack', 'Daniel', 83]]
# df = pd.DataFrame(students)
# print(type(df))
# print(df)

# *Example 3*
# students = [['John', 'Doe', 90], ['Mary', 'Jennings', 88], ['Joshua', 'Smith', 96], ['Jack', 'Daniel', 83]]
# df = pd.DataFrame(students, columns=['First Name', 'Last Name', 'Grade'])  # data frame
# print(df)
# print()
# print(df['First Name'])  # series
# print()
# print(df['Grade'])
# print()
# df = pd.DataFrame(students, index=['Student 1', 'Student 2', 'Student 3', 'Student 4'])  # data frame
# print(df)
#print(df['Grade']==83)  # hmmm interesting, gives true/fales for each value in the series


# *Example 4* Generating a DataFrame from a Dictionary of Lists. Produces the same output as above
# students = {'First Name': ['John', 'Mary', 'Joshua', 'Jack'],
#             'Last Name': ['Doe', 'Jennings', 'Smith', 'Daniel'],
#             'Grade': [90, 88, 96, 83]}
# df = pd.DataFrame(students)
# print(df)


# # *Example 5* Generating a DataFrame from a List of Dictionaries. Produces the same output as above
# students = [{'First Name': 'John', 'Last Name': 'Doe', 'Grade': 90},
#             {'First Name': 'Mary', 'Last Name': 'Jennings', 'Grade': 88},
#             {'First Name': 'Joshua', 'Last Name': 'Smith', 'Grade': 96},
#             {'First Name': 'Jack', 'Last Name': 'Daniel', 'Grade': 83}]  # each dictionary represents a row
# df = pd.DataFrame(students)
# print(df)


# *Example 6*
# my_data = [{'x': 10, 'y': 20}, {'x': 55, 'y': 33, 'z': 22}]
# # df = pd.DataFrame(my_data, index=['row_1', 'row_2'])
# df = pd.DataFrame(my_data, columns=['x', 'y', 't'])  # there's no column t, so this column ends up all null
#
# print(df)


# *Example 7*
students = {'First Name': pd.Series(['John', 'Mary', 'Joshua', 'Jack', 'Mike', "James"]),
            'Last Name': pd.Series(['Doe', 'Jennings', 'Smith', 'Daniel', 'Henry', 'Johnson']),
            'Grade': pd.Series([90, 88, 96, 83])}
df = pd.DataFrame(students)
print(df)
cols = df.columns
cols_total = len(cols)
print("number of columns:", cols_total)
print("type of columns:", type(cols))
print()
print(type(df['First Name']))  # series
print(type(df[['First Name', 'Last Name']]))  # dataframe; a subset dataframe of the larger dataframe
print()
print("Adding a new column by passing as Series")
df["Grade 2"] = pd.Series([68, 81, 100, 92])  # adds a new value for each row
# df["Grade"] = pd.Series([68, 81, 100, 92])  # this would overwrite the first grade column
# df["Grade 3"] = pd.Series([56, 93, 98, 84])  # adds a new value for each row
print(df)
print()

# df["Total Grade"] = df['Grade'] + df["Grade 2"] + df['Grade 3']  # create a new column; sum of all grade columns
# df["Total Grade"] = (df['Grade'] + df["Grade 2"] + df['Grade 3'])/3  # this gives the average grade
#
# print(df)
# print()

# *Example 8*
df.fillna(0, inplace=True)

df["Grade 3"] = pd.Series([56, 93, 98, None])  # adds a new value for each row
df["Total Grade"] = df['Grade'] + df["Grade 2"] + df['Grade 3']  # create a new column; sum of all grade columns
print(df)
print()

del df['Total Grade']
print(df)
print()

grade3_df = df.pop('Grade 3')
print(grade3_df)
