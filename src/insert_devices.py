from common.models import DBSession, Device


device_1 = Device(
    id='00000000-0002-4000-8020-000000000001',
    oranisation='octopus-domestic',
    integration='integration_1',
    location_id='location/1',
    services_enabled=['service_1', 'service_2'],
    site_registered_meter_id='a1',
    site_id='octopus-domestic/1'
)

device_2 = Device(
    id='00000000-0002-4000-8020-000000000002',
    oranisation='octopus-domestic',
    integration='integration_1',
    location_id='location/loc/2',
    services_enabled=['service_1', 'service_2', 'service_3'],
    site_registered_meter_id='b2',
    site_id='octopus-domestic/2'
)

device_3 = Device(
    id='00000000-0002-4000-8020-000000000003',
    oranisation='octopus-domestic',
    integration='integration/2',
    location_id='location/1',
    services_enabled=['service_3', 'service_2'],
    site_id='octopus-domestic/3'
)

device_4 = Device(
    id='00000000-0002-4000-8020-000000000004',
    oranisation='octopus-domestic',
    integration='integration/2',
    location_id='location/2',
    services_enabled=[],
    site_id='octopus-domestic/45'
)

device_5 = Device(
    id='00000000-0002-4000-8020-000000000005',
    oranisation='octopus-domestic',
    integration='integration/3',
    location_id='location/3',
    services_enabled=['service_1', 'service_2'],
    site_registered_meter_id='c4',
    site_id='octopus-domestic/45'
)

device_6 = Device(
    id='00000000-0002-4000-8020-000000000006',
    oranisation='octopus-domestic',
    integration='Tesla',
    location_id='loc_1',
    services_enabled=['service_1', 'service_2'],
    site_registered_meter_id='a1',
    site_id='octopus-domestic/1'
)

device_7 = Device(
    id='00000000-0002-4000-8020-000000000007',
    oranisation='octopus-domestic',
    integration='Tesla',
    location_id='loc_1',
    services_enabled=['service_3', 'service_2'],
    site_registered_meter_id='a7',
    site_id='octopus-domestic/7'
)

device_8 = Device(
    id='00000000-0002-4000-8020-000000000008',
    oranisation='octopus-domestic',
    integration='Enode',
    location_id='loc_1',
    services_enabled=['service_3', 'service_2'],
    site_registered_meter_id='a8',
    site_id='octopus-domestic/8'
)

device_9 = Device(
    id='00000000-0002-4000-8020-000000000009',
    oranisation='octopus-domestic',
    integration='Enode',
    location_id='loc_1',
    services_enabled=['service_5', 'service_2'],
    site_registered_meter_id='a9',
    site_id='octopus-domestic/9'
)

with DBSession() as session:
    session.add_all([device_1, device_2, device_3, device_4, device_5, device_6, device_7, device_8, device_9])
    session.commit()