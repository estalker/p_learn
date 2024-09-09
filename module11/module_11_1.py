import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker as tkr
from datetime import datetime
from datetime import timedelta
from matplotlib import dates


def to_seconds(timestr):
    if timestr == 'nan':
        return 0
    seconds = 0
    for part in timestr.split(':'):
        seconds = seconds * 60 + int(part, 10)
    return seconds


def convert_delta(dlt: timedelta) -> str:
    minutes, seconds = divmod(int(dlt.total_seconds()), 60)
    return f"{minutes}:{seconds:02}"

DATA_URL = "https://runalyze.com/athlete/estalker"
firstOfJuly = pd.to_datetime('2024-07-01')

now = datetime.now()

timestampStart = int(datetime.timestamp(firstOfJuly))
timestampEnd = int(datetime.timestamp(datetime.now()))

getUrl = DATA_URL + f'?start={timestampStart}&end={timestampEnd}'
print(getUrl)

tables_on_page = pd.read_html(getUrl)
df = tables_on_page[3]
df.rename(columns={"Unnamed: 1": "Date"}, inplace=True)

#filtering
basics = df[["Date", "Type", "Distance", "Duration", "Pace"]]
basics = basics[basics['Type'].notnull()]
basics = basics[basics['Date'].notnull()]

#mutaion
basics.insert(5, "Distance (km)", 0)
basics["Distance (km)"] = basics["Distance"].apply(lambda x: str(x).strip("km").strip().replace(",", "."))
basics["Distance (km)"] = basics["Distance (km)"].apply(lambda x: float(x))

basics.insert(6, "Duration (sec)", 0)
basics["Duration (sec)"] = basics["Duration"].apply(lambda x: to_seconds(str(x)))

basics.insert(7, "Pace (sec/km)", 0)
basics["Pace (sec/km)"] = basics["Duration (sec)"] / basics["Distance (km)"]

#output
print(basics)

axs = basics.plot.scatter(x='Type', y="Pace (sec/km)", title="Pace by training type", grid=True)
fmt = tkr.FuncFormatter(lambda x, pos: str(convert_delta(timedelta(seconds=x))))
axs.yaxis.set_major_formatter(fmt)
plt.legend(["ER - Easy run\n" +
            "IT - Interval training\n" +
            "RG - Regeneration\n" +
            "TR - Tempo run\n" +
            "LR - Long run\n" +
            "FL - Fartlek\n" +
            "RC - Race"],
           loc=4)
plt.show()
