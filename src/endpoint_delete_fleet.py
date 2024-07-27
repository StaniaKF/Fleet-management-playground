"""Uses on delete cascase to delete all rows from the link table that are linked to the fleet"""

from sqlalchemy import delete
from common.models import DBSession
from common.models import Fleet
from sqlalchemy.exc import IntegrityError


fleet_id = "947a6f4e-65ef-4ac0-8020-3337d53848a1"

with DBSession() as session:
    session.execute(delete(Fleet).where(Fleet.id == fleet_id))
    try:        
        session.commit()
    except IntegrityError as e:
        print(e)