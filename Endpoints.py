from fastapi import FastAPI
import random
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str

names = ['Santiago', 'Cristiano', 'José', 'Daniela', 'Maria']
sur_names = ['Espinoza','Ronaldo', 'Gonzalez', 'Hernandez','Lopez'] 
data = []
for i in range(100):
    name = random.choice(names)
    sur_name = random.choice(sur_names)

    tmp = {"id":i, "name":name+" "+sur_name}
    d = Employee(id = tmp['id'], name = tmp['name'])
    data.append(d)

@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/item/{parameter}")
def read_item(parameter:int):
    return {"item":parameter}

@app.get("/all")
def get_all():
    return data

@app.post("/employee")
def create_emp(emp:Employee):
    return emp

@app.post("/employee/{emp_id}")
def create_emp(emp_id: int, emp: Employee):
    return {"id":int, **emp.dict()}

@app.get("/emp_id/{emp_id}")
def get_employee(emp_id:int):
    return data[emp_id]