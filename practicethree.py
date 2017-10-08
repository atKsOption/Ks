def funcGrade():
    
    grade = input('please input your grade:')

    if(grade > 100):
        return ('error')
    elif(grade >= 90):
        return ('A')
    elif(grade >= 80):
        return ('B')
    elif(grade >= 70):
        return ('C')
    elif(grade >= 60):
        return ('D')
    else:
        return ('E')
