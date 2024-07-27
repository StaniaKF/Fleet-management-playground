# PUT - so the entire condition filters get updated
# 1) update the filter_conditions field in the fleet table
# 2) delete all rows for that fleet in the device_to_fleet table
# 3) from the filter_conditions create a query to select all devices that match the filter conditions + insert rows into the device_to_fleet table

from sqlalchemy import delete, text, update
from common.statements import create_insert_statement_for_link_table
from common.models import DBSession, DeviceToFleet, Fleet
from payloads import payload_2
from sqlalchemy.exc import IntegrityError

payload = payload_2

fleet_id = payload["id"]
fleet_filter_conditions = payload["filter_conditions"]


with DBSession() as session:
    session.execute(
        update(Fleet)
        .where(Fleet.id == fleet_id)
        .values(
            filter_conditions=fleet_filter_conditions
        )
    )
    session.execute(
        delete(DeviceToFleet)
        .where(DeviceToFleet.fleet_id == fleet_id)
    )

    insert_statement_for_link_table = create_insert_statement_for_link_table(
        fleet_filter_conditions, fleet_id
    )
    session.execute(text(insert_statement_for_link_table))

    try:        
        session.commit()
    except IntegrityError as e:
        print(e)