from fastapi import FastAPI

app = FastAPI()

# Sample alumni data
alumni = [
    {"name": "John Doe", "year": 2020, "program": "Computer Science", "email": "john@example.com"},
    {"name": "Jane Smith", "year": 2019, "program": "Electrical Engineering", "email": "jane@example.com"}
]

@app.get("/")
def home():
    return {"message": "Welcome to Alumni Tracker!"}

@app.get("/alumni")
def get_alumni():
    return alumni

@app.get("/alumni/{year}")
def get_alumni_by_year(year: int):
    return [a for a in alumni if a["year"] == year]
