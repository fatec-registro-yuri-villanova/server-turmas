# Servidor Flask - Lista de Turmas

Servidor  Flask que retorna na rota `/turmas` uma lista de turmas com propriedades `id`, `name` e `color`:
```json
{
   "turmas":[
      {
         "color":"#FF6B6B",
         "id":"dsm1",
         "name":"DSM 1"
      },
      {
         "color":"#4ECDC4",
         "id":"dsm2",
         "name":"DSM 2"
      },
      {
         "color":"#45B7D1",
         "id":"dsm3",
         "name":"DSM 3"
      },
      {
         "color":"#96CEB4",
         "id":"dsm4",
         "name":"DSM 4"
      },
      {
         "color":"#FFEEAD",
         "id":"dsm5",
         "name":"DSM 5"
      },
      {
         "color":"#D4A5A5",
         "id":"dsm6",
         "name":"DSM 6"
      }
   ]
}
```

## 🛠️ Instalação e Uso

### python
```bash
# Cria a pasta do ambiente virtual
python -m venv venv

# Ativa o ambiente virtual
venv\Scripts\activate.bat

# Instala o Flask
pip install Flask

# Run do servidor
flask run --reload
```