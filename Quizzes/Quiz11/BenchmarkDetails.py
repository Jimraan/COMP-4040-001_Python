# COMP 4040-001 Quiz 11

import pandas as pd

df = pd.read_excel('student_benchmark_test_grades.xlsx')

print(df)

res = pd.DataFrame()  # begin with empty data frame
res["Students"] = df["FirstName"]  # first column: student names

cor_answers = []  # to store number of correct answers (will be converted to df row)
inc_answers = []  # to store number of incorrect answers
oth_answers = []  # to store number of other answers

# 1. get total correct answers
for i, row in df.iterrows():  # i is index (0, 1, ...), row is column name + column data (i.e. FirstName Student_2)

    student_info = {}  # create dictionary for storing later
    correct_answers = 0  # tally variable

    for j, column in row.items():  # j is column name (i.e. 1_01), column is column data (i.e. b)
        student_info[j] = column  # {'FirstName': 'Student_1', 'Section': '6C'...} for each student

        if j != "FirstName" and j != "Section" and j != "Grade":  # these are the only columns we're not concerned with
            if column.isupper() and column.isalpha():  # if the data is a correct answer
                correct_answers += 1

    cor_answers.append(correct_answers)
res["Cor Ans"] = cor_answers


# 2. get total incorrect answers
for i, row in df.iterrows():  # i is index (0, 1, ...), row is column name + column data (i.e. FirstName Student_2)

    student_info = {}  # create dictionary for storing later
    incorrect_answers = 0  # tally variable

    for j, column in row.items():  # j is column name (i.e. 1_01), column is column data (i.e. b)
        student_info[j] = column  # {'FirstName': 'Student_1', 'Section': '6C'...} for each student

        if j != "FirstName" and j != "Section" and j != "Grade":  # these are the only columns we're not concerned with
            if column.islower() and column.isalpha():  # if the data is an incorrect answer
                incorrect_answers += 1

    inc_answers.append(incorrect_answers)
res["Inc Ans"] = inc_answers


# 3. get total other answers
for i, row in df.iterrows():  # i is index (0, 1, ...), row is column name + column data (i.e. FirstName Student_2)

    student_info = {}  # create dictionary for storing later
    other_answers = 0  # tally variable

    for j, column in row.items():  # j is column name (i.e. 1_01), column is column data (i.e. b)
        student_info[j] = column  # {'FirstName': 'Student_1', 'Section': '6C'...} for each student

        if j != "FirstName" and j != "Section" and j != "Grade":  # these are the only columns we're not concerned with
            if not column.isalpha():  # if the data is a non-letter answer
                other_answers += 1

    oth_answers.append(other_answers)
res["Oth Ans"] = oth_answers


# 4. Success rate
res["Suc Rate"] = round(res["Cor Ans"]/29, 2)*100


# 5. Failure rate
res["Fail Rate"] = round((res["Inc Ans"] + res["Oth Ans"])/29, 2)*100
print(res)

# 6. Convert dataframe to csv and output file for submission
res.to_csv("output.csv")
