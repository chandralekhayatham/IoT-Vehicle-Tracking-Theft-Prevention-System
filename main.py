from src.gps import get_latitude
from src.gps import get_longitude

from src.geofence import check_geofence
from src.alert import get_alert

from src.dashboard import save_data

print("=" * 60)
print(" IOT VEHICLE TRACKING & THEFT PREVENTION SYSTEM ")
print("=" * 60)

latitude = get_latitude()

longitude = get_longitude()

status = check_geofence(
    latitude,
    longitude
)

alert = get_alert(
    status
)

save_data(
    latitude,
    longitude,
    status,
    alert
)

print("\nLatitude  :", latitude)
print("Longitude :", longitude)

print(
    "\nGoogle Maps :",
    f"https://maps.google.com/?q={latitude},{longitude}"
)

print("\nVehicle Status :", status)

print("\n" + alert)

print("\nLocation Logged Successfully")
print("Thank You for Using Vehicle Tracking System")