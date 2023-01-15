from pydantic import BaseModel

class CreateStaffMemberModel(BaseModel):
    NameStaffMember: str
    AgeStaffMember: str
    RoleStaffMember: str

class StaffMember:
    def __init__(self, IdStaffMember, NameStaffMember, AgeStaffMember, RoleStaffMember) -> None:
        self.IdStaffMember = IdStaffMember
        self.NameStaffMember = NameStaffMember
        self.AgeStaffMember = AgeStaffMember
        self.RoleStaffMember = RoleStaffMember



