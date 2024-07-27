# User group 1
# querying done by exact match or filter conditionts

# how will the query parameters look like? who is going to be a user? internal only?

from sqlalchemy import String, cast, select

from common.models import Fleet, DBSession


query_param_1 = {"type": "equal", "field": "integration", "value": ["Enode"]}
query_param_2 = {"type": "equal", "field": "location_id", "value": ["loc_1"]}

with DBSession() as session:    
    fleets = session.execute(
        select(Fleet.id).where(
            Fleet.filter_conditions.contains([query_param_1, query_param_2])
        )
    ).scalars().all()
    print("fleets", fleets)
