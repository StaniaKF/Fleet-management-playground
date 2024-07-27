from common.filter_clauses import type_to_clause_map

def create_select_statement_for_device_table(filter_conditions: list, base_query: str):
    clauses_dict = {}

    for condition in filter_conditions:
        type = condition["type"]
        field = condition["field"]
        value = condition["value"]   

        clause_class = type_to_clause_map[type]
        clause_instance = clause_class(field, value)

        if field not in clauses_dict.keys():
            clauses_dict[field] = [clause_instance]
        else:
            clauses_dict[field].append(clause_instance)

    # flatten array and transform clauses into a query
    sql_statements_array = []
    for field, clauses in clauses_dict.items():
        if len(clauses) > 1:
            joined_clauses = " OR ".join([clause.generate_sql() for clause in clauses])
            statement = "(" + joined_clauses + ")"
        else:
            statement = clauses[0].generate_sql()
        sql_statements_array.append(statement)

    query = base_query + " AND ".join(sql_statements_array) 
    return query


def create_insert_statement_for_link_table(filter_conditions: list, fleet_id: str):   

    base_query = "SELECT id, site_id, site_registered_meter_id FROM device WHERE "
    query = create_select_statement_for_device_table(filter_conditions, base_query)

    # result = DBSession.execute(text(query)).fetchall() 

    insert_query = (
        "INSERT INTO device_to_fleet (device_id, site_id, site_registered_meter_id, fleet_id)" +
        f"WITH devices_cte AS ({query})"+
        f"SELECT id, site_id, site_registered_meter_id, '{fleet_id}' FROM devices_cte"
    )

    return insert_query


def create_get_statement_for_link_table(filter_conditions: list):   

    base_query = "SELECT id FROM device WHERE "
    query = create_select_statement_for_device_table(filter_conditions, base_query)

    get_query = (
        f"WITH devices_cte AS ({query})"+
        f"SELECT DISTINCT fleet_id FROM device_to_fleet JOIN devices_cte ON device_to_fleet.device_id = devices_cte.id"
    )

    return get_query