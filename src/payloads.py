payload_1 = {
    "id": "947a6f4e-65ef-4ac0-8020-3337d53848a1",
    "filter_conditions" : [
        {   
            "field": "location_id",
            "value": ["location/*"],
            "type": "like"
        },        
        {
            "field": "services_enabled",
            "value": ["service_1", "service_2"],
            "type": "contain"
        },
        {
            "field": "location_id",
            "value": ["location/loc/2"],
            "type": "equal"
        },
        {
            "field": "location_id",
            "value": ["location/loc/*"],
            "type": "like"
        },
        {
            "field": "site_registered_meter_id",
            "value": ["false"],
            "type": "is_null"
        },
   ]
}

payload_1b = {
    "id": "947a6f4e-65ef-4ac0-8020-3337d53848a1",
    "filter_conditions": [
        {
            "field": "integration",
            "value": ["Enode"],
            "type": "equal"
        },
   ]
}

payload_2 = {
    "id": "947a6f4e-65ef-4ac0-8020-3337d53848a2",
    "filter_conditions" : [
        {
            "field": "integration",
            "value": ["Enode"],
            "type": "equal"
        },
   ]
}

payload_3 = {
    "id": "947a6f4e-65ef-4ac0-8020-3337d53848a3",
    "filter_conditions" : [
        {
            "field": "integration",
            "value": ["Enode"],
            "type": "equal"
        },
        {
            "field": "location_id",
            "value": ["loc_1"],
            "type": "equal"
        },
        {
            "field": "site_registered_meter_id",
            "value": ["false"],
            "type": "is_null"
        },
   ]
}