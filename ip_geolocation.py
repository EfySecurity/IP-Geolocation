import requests

# Cores para formatar a saída
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'

def get_ip_geolocation(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data

def display_geolocation_info(geolocation_data):
    print(f"\n{Colors.HEADER}Informações de Geolocalização:{Colors.END}")
    print(f"{Colors.BLUE}IP: {geolocation_data['ip']}")
    print(f"Hostname: {geolocation_data['hostname']}")
    print(f"Cidade: {geolocation_data['city']}")
    print(f"Região: {geolocation_data['region']}")
    print(f"País: {geolocation_data['country']}")
    print(f"Provedor de Serviços: {geolocation_data['org']}")
    print(f"Latitude/Longitude: {geolocation_data['loc']}{Colors.END}")

def main():
    ip_address = input(f"{Colors.GREEN}Digite o endereço IP para obter informações de geolocalização: {Colors.END}")
    
    geolocation_data = get_ip_geolocation(ip_address)
    display_geolocation_info(geolocation_data)

if __name__ == "__main__":
    main()
