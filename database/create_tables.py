from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from .db import engine

Base = declarative_base()

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(10))
    
    
class Student(Base):
    __tablename__ = "stidents"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(120), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"))
    
    
class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(120))


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(120))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    
    
class Mark(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    student_id = Column(Integer, ForeignKey("stidents.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    mark = Column(Integer)
    date = Column(String) # Date


Base.metadata.create_all(engine)
Base.metadata.bind = engine