# PDF Emissor

Emissão de recibos Escuteiros - Sistema para geração de recibos em PDF.

## Estrutura do Projeto

```
pdf-emissor/
│
├── src/
│   ├── pdf_emissor.py      # Geração de PDFs
│   ├── airtable_client.py  # Cliente para Airtable API
│   ├── supabase_client.py  # Cliente para Supabase
│   └── main.py             # Ponto de entrada principal
│
├── app.py                  # Aplicação web
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação
└── .env.example            # Exemplo de variáveis de ambiente
```

## Instalação

1. Clone o repositório:
```bash
git clone <repository-url>
cd pdf-emissor
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas credenciais
```

## Configuração

Copie o arquivo `.env.example` para `.env` e preencha as variáveis:

- `AIRTABLE_API_KEY`: Chave de API do Airtable
- `AIRTABLE_BASE_ID`: ID da base do Airtable
- `SUPABASE_URL`: URL do projeto Supabase
- `SUPABASE_KEY`: Chave de API do Supabase

## Uso

### Execução via linha de comando:
```bash
python src/main.py
```

### Execução da aplicação web:
```bash
python app.py
```

## Módulos

### pdf_emissor.py
Responsável pela geração dos recibos em formato PDF.

### airtable_client.py
Cliente para comunicação com a API do Airtable para busca e atualização de dados.

### supabase_client.py
Cliente para comunicação com o Supabase para armazenamento de arquivos.

## Licença

Este projeto é para uso interno do Grupo de Escuteiros.
