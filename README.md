<div align="center">
  <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="python-logo-generic.svg">
</div>

# IP Geolocation

Este é um script Python simples para obter informações de geolocalização com base em um endereço IP.

## Pré-requisitos

Antes de usar este script, certifique-se de ter o Python instalado em seu sistema. Além disso, você precisa instalar a biblioteca `requests` & `beautifulsoup4` se ainda não tiver. Você pode fazer isso executando os seguintes comando:

```bash
pip install requests
```

```bash
pip install beautifulsoup4
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

4. O script solicitará que voce insera um endereço IP manualmente.

5. Você deverá digitar um endereço IP manualmente separado por `.` exemplo `xxx.xxx.xxx.xxx`.

6. O script solicitará à API ipinfo.io as informações de geolocalização do IP e exibirá os resultados na saída do terminal.

## Observações

- A precisão das informações de geolocalização pode variar e nem sempre é 100% precisa.

- Este script foi criado apenas para fins educacionais e de demonstração.

## Autor

Nome: Efy Security

Email: efy.security@proton.me

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
