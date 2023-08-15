# IP-Geolocation

# IP Geolocation

Este é um script Python simples que utiliza a API de geolocalização de IP do site ipinfo.io para obter informações de geolocalização com base em um endereço IP.

## Pré-requisitos

Antes de usar este script, certifique-se de ter o Python instalado em seu sistema. Além disso, você precisa instalar a biblioteca `requests` se ainda não a tiver. Você pode fazer isso executando o seguinte comando:

```bash
pip install requests
```

## Como usar

1. Clone ou baixe este repositório no seu terminal.

```bash
git clone https://github.com/EfySecurity/IP-Geolocation
```

2. Navegue até o diretório onde o script `ip_geolocation.py` está localizado.

```bash
cd IP-Geolocation
```

3. Execute o script usando o seguinte comando:

```bash
python ip_geolocation.py
```

4. O script solicitará se você deseja usar seu próprio endereço IP ou inserir um endereço IP manualmente. Digite 's' para usar o seu próprio IP ou 'n' para inserir um IP manualmente.

5. Se você escolher usar seu próprio IP, o script detectará seu endereço IP público. Caso contrário, você deverá digitar um endereço IP manualmente.

6. O script solicitará à API ipinfo.io as informações de geolocalização do IP e exibirá os resultados na saída do terminal.

## Observações

- A precisão das informações de geolocalização pode variar e nem sempre é 100% precisa.

- Certos serviços de geolocalização podem ter limites de uso ou exigir uma chave de API para acesso. Certifique-se de verificar a documentação do serviço que você está utilizando.

- Este script foi criado apenas para fins educacionais e de demonstração.

## Autor

Efy Security
