import requests
import socket

def get_external_ip():
    try:
        # Conexão com um servidor externo para determinar o IP público
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        print("Não foi possível obter o endereço IP externo:", e)
        return None

def get_ip_geolocation(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    option = input("Escolha uma opção:\n1 - Usar meu IP público\n2 - Inserir manualmente um endereço IP\nDigite o número da opção: ")

    if option == "1":
        ip_address = get_external_ip()
        if ip_address is None:
            print("Não foi possível obter o seu IP externo.")
            return
    elif option == "2":
        ip_address = input("Digite o endereço IP para obter informações de geolocalização: ")
    else:
        print("Opção inválida.")
        return
    
    geolocation_data = get_ip_geolocation(ip_address)
    
    print("\nInformações de Geolocalização:")
    print(f"IP: {geolocation_data['ip']}")
    print(f"Hostname: {geolocation_data['hostname']}")
    print(f"Cidade: {geolocation_data['city']}")
    print(f"Região: {geolocation_data['region']}")
    print(f"País: {geolocation_data['country']}")
    print(f"Provedor de Serviços: {geolocation_data['org']}")
    print(f"Latitude/Longitude: {geolocation_data['loc']}")

if __name__ == "__main__":
    main()
