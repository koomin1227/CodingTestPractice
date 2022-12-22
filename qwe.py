def check_score(score):
    if score>=90:
        grade='A'
    elif score >=80:
        grade='B'
    elif score >= 70:
        grade='C'
    elif score >=60:
        grade='D'
    else:
        grade='F'
    return grade
grade=check_score(30)
print(grade)
