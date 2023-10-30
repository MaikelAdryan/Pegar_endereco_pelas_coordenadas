from geopy.geocoders import Nominatim
import pandas as pd

geolocator = Nominatim(user_agent="Adryan")
data = pd.read_excel('coord.xlsx')
# print(data.head(0))
latitude = data['LAT']
longitude = data['LONG']
count = 0
addresss = []
for la, lo in zip(latitude, longitude):
  count += 1
  location = geolocator.reverse(f"{la}, {lo}")
  address = location.address if location else print("Verifique as coordenadas.")
  print(f"{count} = {address.split(', Porto Alegre,')[0]}")
  addresss.append(f"{address.split(', Porto Alegre,')[0]}")

data['Local'] = addresss
print(data.head())
name = 'dados.xlsx'
sheet_name = 'Planilha1'
data.to_excel(name, sheet_name=sheet_name, index=False)
