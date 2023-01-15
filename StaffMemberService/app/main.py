from fastapi import FastAPI, HTTPException
# from StaffMemberService.app.StaffMember import StaffMember # for IDE Pycharm
from app.StaffMember import StaffMember, CreateStaffMemberModel # for Docker
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

staffMembersList: list[StaffMember] = [
    # StaffMember("205301", "Harry Potter", "30", "Admin"),
    # StaffMember("205302", "Herminoe Granger", "30", "Manager"),
    # StaffMember("205303", "Voldemort", "HP", "Assistant"),
    # StaffMember("205304", "Albus Dumbledore", "70", "Team Leader"),
    # StaffMember("205305", "Severus Rogue", "40", "Admin")
]

def addStaffmember(context: CreateStaffMemberModel):
    IdStaffMember = len(staffMembersList)
    staffMembersList.append(StaffMember(
        IdStaffMember,
        context.NameStaffMember,
        context.AgeStaffMember,
        context.RoleStaffMember))
    return IdStaffMember

app = FastAPI()

# Jaeger
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


resource = Resource(attributes={
    SERVICE_NAME: "staffmembers-service"
})

jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831,
)

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(jaeger_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

FastAPIInstrumentor.instrument_app(app)

#
##########

##########
# Prometheus

from prometheus_fastapi_instrumentator import Instrumentator
@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)

##########
@app.get("/v1/staffmembers")
async def getStaffMembersList():
    return staffMembersList

@app.post("/v1/staffmembers")
async def addStaffMember(content: CreateStaffMemberModel):
    addStaffmember(content)
    return staffMembersList[-1]

@app.get("/v1/staffmembers/{idStaffMember}")
async def getStaffMemberById(idStaffMember: str):
    choosenStaffMember = [person for person in staffMembersList if person.IdStaffMember == idStaffMember]
    if len(choosenStaffMember) > 0:
        return choosenStaffMember[0]
    raise HTTPException(status_code=404, detail="Staff Member is not founded!")

@app.get("/__health")
async def check_service():
    return


