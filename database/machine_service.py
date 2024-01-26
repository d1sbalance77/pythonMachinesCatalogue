from database.models import Machine
from database import get_db


def add_new_machine_db(machine_id, machine_name, machine_engine_id, machine_engine, machine_color, machine_year,
                       machine_cost,
                       machine_photo):
    db = next(get_db())

    checker = db.query(Machine).filter_by(machine_id=machine_id).first()

    if checker:
        return 'This machine was already registered'
    else:
        new_machine = Machine(machine_id=machine_id,
                              machine_name=machine_name,
                              machine_engine=machine_engine,
                              machine_engine_id=machine_engine_id,
                              machine_color=machine_color,
                              machine_year=machine_year,
                              machine_cost=machine_cost,
                              machine_photo=machine_photo)

    db.add(new_machine)
    db.commit()

    return 'Machine was successfully registered'


def delete_machine_db(machine_id,machine_name,machine_engine,machine_color,machine_year):
    db = next(get_db())

    exact_machine = db.query(Machine).filter_by(machine_id=machine_id,
                                                machine_name=machine_name,
                                                machine_engine=machine_engine,
                                                machine_color=machine_color,
                                                machine_year=machine_year).first()

    if exact_machine:
        db.delete(exact_machine)
        db.commit()

        return 'Machine was successfully deleted'
    else:
        return 'This Machine does not exists'


def change_machine_db(machine_id, changed_machine,machine_name,machine_engine,machine_color,machine_year):
    db = next(get_db())

    changed_machine = db.query(Machine).filter_by(machine_id=machine_id,
                                                  changed_machine=changed_machine,
                                                  machine_name=machine_name,
                                                  machine_engine=machine_engine,
                                                  machine_color=machine_color,
                                                  machine_year=machine_year).first()

    if changed_machine:
        changed_machine.Machine = changed_machine
        db.commit()

        return 'Machine was successfully changed'
    else:
        return False

