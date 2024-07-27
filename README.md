# Fleet-management-playground
Playground for fleet management code without lambdas.
This is just a simple exapmle to demostrate how the queries for fleet management endpoints could be implemented.

## Set up

### Create virtual environment venv

```bash
python -m venv venv
```

### Activate venv

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create tables
1. Initialise postgreSQL server
2. Run
```bash
python src/common.py/models.py
```

### To insert some devices into device table
```bash
python src/insert_devices.py
```

### To insert a fleet into fleet table and the device_to_fleet table
Choose a payload in payloads.py or add a new payload to it
Update the payload in endpoint_create_fleet.py
Run:
```bash
python src/endpoint_create_fleet.py
```

### To update a fleet 
Choose a payload in payloads.py or add a new payload to it
Update the payload in endpoint_update_fleet.py
Run:
```bash
python src/endpoint_update_fleet.py
```

### To delete a fleet
Modify fleet_id in endpoint_delete_fleet.py to your fleet_id
Run:
```bash
python src/endpoint_delete_fleet.py
```

### To explore fleets with specific characteristics
To explore fleets by the fleet definitions run:
```bash
python src/endpoint_get_user_group_1.py
```
To explore fleets by their composition at an aggregate view run:
```bash
python src/endpoint_get_user_group_2.py
```