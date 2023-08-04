from sqlalchemy import func
from database.db import session
from database.create_tables import Student, Mark

def select_1():
    top_students = (
    session.query(Student.name, func.avg(Mark.mark).label('average_mark'))
    .join(Mark, Student.id == Mark.student_id)
    .group_by(Student.id)
    .order_by(func.avg(Mark.mark).desc())
    .limit(5)
    .all()
    )
    for student_name, average_mark in top_students:
        print(f'Student: {student_name}, Average Mark: {average_mark}')
    
def select_2():
    print(2)
    
def select_3():
    print(3)
    
def select_4():
    print(4)
    
def select_5():
    print(5)
    
def select_6():
    print(6)
    
def select_7():
    print(7)
    
def select_8():
    print(8)
    
def select_9():
    print(9)
    
def select_10():
    print(10)
    
all_selections = [select_1, select_2, select_3, 
                  select_4, select_5, select_6, 
                  select_7, select_8, select_9, 
                  select_10]
