from fastapi import FastAPI, HTTPException
# from StaffMemberService.app.StaffMember import StaffMember # for IDE Pycharm
from app.StaffMember import StaffMember

staffMembersList: list[StaffMember] = [
    StaffMember("205301", "Harry Potter", "30", "Admin"),
    StaffMember("205302", "Herminoe Granger", "30", "Manager"),
    StaffMember("205303", "Voldemort", "HP", "Assistant"),
    StaffMember("205304", "Albus Dumbledore", "70", "Team Leader"),
    StaffMember("205305", "Severus Rogue", "40", "Admin")
]

app = FastAPI()

@app.get("/v1/staffmembers")
async def getStaffMembersList():
    return staffMembersList

@app.get("/v1/staffmembers/{idStaffMember}")
async def getStaffMemberById(idStaffMember: str):
    choosenStaffMember = [person for person in staffMembersList if person.IdStaffMember == idStaffMember]
    if len(choosenStaffMember) > 0:
        return choosenStaffMember[0]
    raise HTTPException(status_code=404, detail="Staff Member is not founded!")


