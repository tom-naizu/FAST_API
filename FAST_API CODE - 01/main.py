from fastapi import FastAPI, Path, Query, HTTPException
import json

app = FastAPI()
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/patients/{patient_id}")
def view_patients(patient_id:str = Path(..., description="Patient ID of patient",example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort by weight or BMI"),
    order: str = Query("asc", description="asc or desc")
):

    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in ["height", "weight", "bmi"]:
        raise HTTPException(status_code=400, detail=f'Invaild sort field select from {valid_fields}')
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail=f'Invaild order select between asc and desc')

    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

@app.get("/about")
def about():
    return {"message": "Tom Naizu is here, Be Aware..."}