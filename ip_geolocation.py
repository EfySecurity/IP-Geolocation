import requests

def get_ip_geolocation(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data

def display_geolocation_info(geolocation_data):
    print("\nInformações de Geolocalização:")
    print(f"IP: {geolocation_data['ip']}")
    print(f"Hostname: {geolocation_data['hostname']}")
    print(f"Cidade: {geolocation_data['city']}")
    print(f"Região: {geolocation_data['region']}")
    print(f"País: {geolocation_data['country']}")
    print(f"Provedor de Serviços: {geolocation_data['org']}")
    print(f"Latitude/Longitude: {geolocation_data['loc']}")

def main():
    ip_address = input("Digite o endereço IP para obter informações de geolocalização: ")
    
    geolocation_data = get_ip_geolocation(ip_address)
    display_geolocation_info(geolocation_data)

if __name__ == "__main__":
    main()
