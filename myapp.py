from fastapi import FastAPI


app = FastAPI()


students = { 
    'sarwech':{ 
        'name': 'Sarwech Imdad',
        'id':'BSE-22F-138', 
        'Department': 'software engineering', 
        'section':'SE4C'
    },
    'asim':{ 'name':'Asim Hayat',
    'id':'BSE-22F-132', 
    'Department': 'software engineering', 
    'section':'SE4C'
    },
    'abrar':{ 'name':'abrar',
    'id':'BSE-22F-128', 
    'Department': 'software engineering', 
    'section':'SE4C'},
    }
 
@app.get("/api/{student_name}")
def index(student_name:str):
    if student_name in students:
        return {'student': students[student_name]}
        
    else:
        return {'students': students}
