from pydantic import BaseModel

class RegisterMachineValidator(BaseModel):
    machine_name: str
    machine_id: int
    machine_engine: str
    machine_engine_id: int
    machine_photo: str
    machine_cost: int
    machine_color: str
    machine_year: int

class DeleteMachineValidator(BaseModel):
    machine_name: str
    machine_id: int
    machine_engine: str
    machine_color: str
    machine_year: int

class ChangeMachineValidator(BaseModel):
    machine_name: str
    machine_id: int
    machine_engine: str
    changed_machine: str
    machine_color: str
    machine_year: int