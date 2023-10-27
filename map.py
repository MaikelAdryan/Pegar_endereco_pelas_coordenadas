from geopy.geocoders import Nominatim
import pandas as pd

def get_address_from_latlng(latitude, longitude):
  pass
  # Inicialize o objeto geocoder com o serviço Nominatim
  geolocator = Nominatim(user_agent="geoapiExercises")

  # Crie uma string de coordenadas no formato "latitude, longitude"
  location = geolocator.reverse(f"{latitude}, {longitude}")

  if location:
    return location.address
  else:
    print("Não foi possível obter o endereço. Verifique as coordenadas.")


if __name__ == "__main__":
  data = pd.read_excel('coord.xlsx')
  
  latitude = data['Lat']  # Substitua pela sua latitude
  longitude = data['Lon']  # Substitua pela sua longitude
  
  for la, lo in zip(latitude, longitude):
    address = get_address_from_latlng(la, lo)
    print(f"{la} {lo} = {address}")
    data['Local'] = f"{address}"
    
  print(data.head())
  nome_do_arquivo = 'dados.xlsx'
  sheet_name = 'Planilha1'

  data.to_excel(nome_do_arquivo, sheet_name=sheet_name, index=False)