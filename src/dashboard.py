import pandas as pd
from datetime import datetime

def save_data(
    latitude,
    longitude,
    status,
    alert
):

    data = {
        "Timestamp":[datetime.now()],
        "Latitude":[latitude],
        "Longitude":[longitude],
        "Status":[status],
        "Alert":[alert]
    }

    df = pd.DataFrame(data)

    df.to_csv(
        "data/vehicle_data.csv",
        mode="a",
        index=False,
        header=False
    )