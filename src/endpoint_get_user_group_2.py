# User group 2
# Fleet explorer

from sqlalchemy import text
from common.statements import create_get_statement_for_link_table
from common.models import DBSession


query_param_a = {"type": "equal", "field": "integration", "value": ["Enode"]}

with DBSession() as session: 
    list_of_fleets = session.execute(text(create_get_statement_for_link_table([query_param_a]))).scalars().all()
    print(list_of_fleets)