# Quiz 9 question 4
class ScoreIsLessException(Exception):
    def __init__(self, m):
        Exception.__init__(self, m)


score = 79
try:
    if score < 50:
        raise ScoreIsLessException("This score is too low. You failed the exam")
    else:
        raise ScoreIsLessException("You passed the exam. Congratulations.")
except ScoreIsLessException as e:
    print(e.args)
