from geopy.geocoders import Nominatim
import pandas as pd

geolocator = Nominatim(user_agent="geoapiExercises")
data = pd.read_excel('coord2.xlsx')
latitude = data['Lat']
longitude = data['Lon']
count = 0
addresss = []

for la, lo in zip(latitude, longitude):
  count = count + 1
  location = geolocator.reverse(f"{la}, {lo}")
  if location:
    address = location.address
  else:
    print("Não foi possível obter o endereço. Verifique as coordenadas.")
  print(f"{count} = {address}")
  addresss.append(f"{address}")
  
data['Local'] = addresss

print(data.head())

name = 'dados.xlsx'
sheet_name = 'Planilha1'
data.to_excel(name, sheet_name=sheet_name, index=False)
