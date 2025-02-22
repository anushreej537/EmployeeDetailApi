from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine,SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

@app.post('/employees/', response_model = schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session =Depends(get_db)):
    return crud.create_employee(db=db,employee=employee)


@app.get('/employee/{employee_id}/', response_model=schemas.Employee)
def get_employee(employee_id:int ,db : Session = Depends(get_db)):
    db_employee = crud.get_employee(db , employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee not found')
    return db_employee

@app.get('/employees/',response_model=list[schemas.Employee])
def get_employees(skip :int=0 , limit : int=10,db : Session = Depends(get_db)):
    return crud.get_employees(db , skip=skip, limit=limit)


@app.put('/employees/{employee_id}', response_model= schemas.Employee)
def update_employee(employee_id: int , employee:schemas.EmployeeUpdate, db :Session = Depends(get_db)):
    db_employee = crud.update_employee(db , employee_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee not found')
    return db_employee

@app.delete('/employees/{employee_id}', response_model=schemas.Employee)
def delete_employee(employee_id:int, db: Session=Depends(get_db)):
    db_employee = crud.delete_employee(db, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='employee not found')
    return db_employee