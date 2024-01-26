from fastapi import APIRouter
from machines import RegisterMachineValidator, DeleteMachineValidator,ChangeMachineValidator
from database.machine_service import add_new_machine_db,delete_machine_db,change_machine_db

machine_router = APIRouter(tags=['Управление Машинами'],prefix='/machines')


@machine_router.post('/register-machine')
async def register_machine(data: RegisterMachineValidator):

    result = add_new_machine_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'This machine already exists'}

@machine_router.delete('delete-machine')
async def delete_machine(data: DeleteMachineValidator):

    result = delete_machine_db(**data.model_dump())

    if result:
        return {"message": f'Success {result}'}
    else:
        return {'message': 'Machine was not found'}

@machine_router.put('/edit-machine')
async def edit_user(data: ChangeMachineValidator):
    change_data = data.model_dump()

    result = change_machine_db(**change_data)

    return {'message': result}



