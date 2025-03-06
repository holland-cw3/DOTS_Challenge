from fastapi import FastAPI
# import pandas as pd
# from specialFilter import specialFilter
# from semesterFilter import semesterFilter

# date = '1/3/2023'
# time = '03:00'
# visitorType = 'Student'
# permissions = []

# date = pd.to_datetime(date)


# Read in all the parking lots
# lots = []
# with open('lots.txt', 'r') as file:
#     lines = file.read().splitlines() 
#     lots.extend(lines) 


# lots2 = specialFilter(date, lots)
# lots = semesterFilter(date, lots)


app = FastAPI()



@app.get("/")
def health():
    return {"message": "Hello World"}
