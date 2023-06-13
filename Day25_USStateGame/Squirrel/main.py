import pandas as pd

url = "https://data.cityofnewyork.us/resource/vfnx-vebw.json"

data = pd.read_json(url)
# print(data.columns.tolist())
data.to_csv("dataset.csv")

colors = data["primary_fur_color"].dropna().unique().tolist()
counts = []
for color in colors:
    count = data["primary_fur_color"].eq(color).sum()
    counts.append(count)


df = pd.DataFrame({"color": colors,
                   "count": counts,})

print(df)

df.to_csv("squirrel.csv")