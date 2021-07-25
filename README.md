# Photos Mirror

Script Python para baixar a biblioteca de fotos do iCloud, incluindo arquivos RAW.

# Configuração

Para usar a aplicação, é necessário adicionar dois arquivos de configução: `.env` e `.secrets.toml`.

## Arquivo `.env`

O `.env` é usado para definir os diretórios que serão utilizados para armazenar os dados, tanto as fotos como os token de login. Exemplo de arquivo:

```
DOWNLOAD_PATH=~/Pictures/iCloud
COOKIE_PATH=~/Pictures/iCloud/cookies
```

## Arquivo `.secrets.toml`

O `secrets.toml` é onde se deve colocar as credenciais usadas no iCloud, conforme exemplo abaixo:

```
[docker.icloud]
user = 'fulano@dominio.com'
password = 'senha'
```

# Execução

Para executar o script, é necessário executar o comando `docker run app` na raiz do projeto. A cada execução, o script fará o download de todas as fotos que ainda não estão baixadas no diretório definido em `DOWNLOAD_PATH`.