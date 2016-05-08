from google.transit import gtfs_realtime_pb2
import urllib

n = 1
trip_update = 'http://www.rtd-denver.com/google_sync/TripUpdate.pb'
vehicle_position = 'http://www.rtd-denver.com/google_sync/VehiclePosition.pb'

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen(vehicle_position)
feed.ParseFromString(response.read())

first = feed.entity[0]
for entity in feed.entity[:n]:
    if entity.HasField('trip_update'):
        print entity.trip_update
