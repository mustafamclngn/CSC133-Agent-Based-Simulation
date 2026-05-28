import xml.etree.ElementTree as ET
import pandas as pd

# trip information (summary)
def parse_tripinfo(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    data = []
    for trip in root.findall('tripinfo'):
        data.append({
            'vehicle_id': trip.get('id'),
            'depart_time': float(trip.get('depart')),
            'duration_sec': float(trip.get('duration')), # travel time
            'waiting_time_sec': float(trip.get('waitingTime')) # waiting time
        })
    
    return pd.DataFrame(data)

# parse queue length detectors
def parse_queues(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    data = []
    # queue length tracked in interval (every 60 seconds)
    for interval in root.findall('interval'):
        data.append({
            'detector_id': interval.get('id'),
            'begin_time': float(interval.get('begin')),
            'end_time': float(interval.get('end')),
            'max_queue_meters': float(interval.get('maxJamLengthInMeters')), # queue length
            'max_queue_vehicles': int(interval.get('maxJamLengthInVehicles'))
        })
        
    return pd.DataFrame(data)

# parse speed and density
def parse_edgedata(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    data = []
    # edge_data (speend and density) tracked in interval (every 60 seconds)
    for interval in root.findall('interval'):
        for edge in interval.findall('edge'):
            data.append({
                'edge_id': edge.get('id'),
                'density_veh_km': float(edge.get('density')), # congestion density
                'speed_m_s': float(edge.get('speed'))         # average speed
            })
            
    return pd.DataFrame(data)

# output data files
trip_df = parse_tripinfo('tripinfo.xml')
queue_df = parse_queues('queues.xml')
edge_df = parse_edgedata('edge_data.xml')
print("--- Trip Information ---")
print(trip_df.head())
print("\n" + "="*50)
print("INTERSECTION PERFORMANCE REPORT (MIDDAY BASELINE)")
print("="*50)

# 1. travel time (individual trips)
avg_travel_time = trip_df['duration_sec'].mean()
max_travel_time = trip_df['duration_sec'].max()

print("\n1. TRAVEL TIME:")
print(f"   - Average Travel Time: {avg_travel_time:.2f} seconds")
print(f"   - Maximum Travel Time: {max_travel_time:.2f} seconds")

# 2. average speed (each road segment)
print("\n2. AVERAGE SPEED PER ROAD SEGMENT:")
avg_speed = edge_df.groupby('edge_id')['speed_m_s'].mean().reset_index()
for index, row in avg_speed.iterrows():
    print(f"   - {row['edge_id']}: {row['speed_m_s']:.2f} m/s")

# 3. queue length (recorded by the detectors)
print("\n3. MAXIMUM QUEUE LENGTH PER APPROACH:")
max_queue = queue_df.groupby('detector_id')['max_queue_meters'].max().reset_index()
for index, row in max_queue.iterrows():
    print(f"   - {row['detector_id']}: {row['max_queue_meters']:.2f} meters")

# 4. congestion density (each road segment)
print("\n4. AVERAGE CONGESTION DENSITY:")
avg_density = edge_df.groupby('edge_id')['density_veh_km'].mean().reset_index()
for index, row in avg_density.iterrows():
    print(f"   - {row['edge_id']}: {row['density_veh_km']:.2f} vehicles per km")

print("\n" + "="*50)