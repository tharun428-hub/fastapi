from sqlalchemy.orm import Session
from models import Student
from schemas import StudentCreate, StudentUpdate

def create_student(db: Session, student: StudentCreate):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(Student).all()

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def update_student(db: Session, student_id: int, student: StudentUpdate):
    db_student = get_student(db, student_id)
    if db_student:
        # Update only the fields that are provided (not None)
        if student.name is not None:
            db_student.name = student.name
        if student.age is not None:
            db_student.age = student.age
        if student.email is not None:
            db_student.email = student.email
        if student.course is not None:
            db_student.course = student.course
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student
