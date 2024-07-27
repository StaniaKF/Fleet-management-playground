from common.statements import create_insert_statement_for_link_table
from sqlalchemy import text
from common.models import DBSession, Fleet
from sqlalchemy.exc import IntegrityError
from payloads import payload_1


payload = payload_1
filter_conditions = payload["filter_conditions"]
fleet_id = payload["id"]

fleet_1 = Fleet(
    id=payload["id"],
    filter_conditions=payload["filter_conditions"]
)

insert_statement_for_link_table = create_insert_statement_for_link_table(
    payload["filter_conditions"], payload["id"]
)

with DBSession() as session:
    session.add(fleet_1)
    session.flush()
    session.execute(text(insert_statement_for_link_table))
    
    try:        
        session.commit()
    except IntegrityError as e:
        print(e)
        