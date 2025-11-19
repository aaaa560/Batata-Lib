# Batata-Lib API Examples

Este diretório contém exemplos práticos de uso das APIs disponíveis no batata-lib.

## Arquivo: `api_examples.py`

Demonstra o uso de todas as APIs integradas:

### 1. **GitHubAPI** 
Interaja com a API do GitHub para:
- Buscar informações de usuários
- Listar repositórios
- Pesquisar repositórios por query
- Obter commits de um repositório

**Não requer chave de API** (mas tem rate limit menor)

### 2. **WeatherAPI** 
Consulte informações de clima usando OpenWeatherMap:
- Clima atual por cidade
- Previsão do tempo
- Clima por coordenadas geográficas

**Requer chave de API gratuita**: https://openweathermap.org/api

### 3. **CurrencyAPI** 
Conversão de moedas e taxas de câmbio:
- Obter taxas de câmbio atuais
- Converter valores entre moedas
- Listar moedas suportadas

**Não requer chave de API** (mas funcionalidade limitada)

### 4. **PokeAPI** 
Busque informações sobre Pokémon:
- Informações detalhadas de Pokémon
- Fuzzy matching para nomes (aceita erros de digitação)
- Habilidades e características

**Não requer chave de API**

## Como Usar

### Instalação
```bash
pip install batata-lib
```

### Executar Exemplos
```bash
python examples/api_examples.py
```

### Configuração de API Keys

#### WeatherAPI
1. Crie uma conta gratuita em https://openweathermap.org/api
2. Obtenha sua chave de API
3. Substitua `SUA_CHAVE_AQUI` no exemplo

```python
weather = WeatherAPI(api_key="sua_chave_real")
```

#### GitHubAPI (Opcional)
Para maior rate limit, use um token pessoal:
1. Acesse: https://github.com/settings/tokens
2. Crie um token com permissões de leitura
3. Use no código:

```python
github = GitHubAPI(token="seu_token_aqui")
```

#### CurrencyAPI (Opcional)
Para funcionalidades avançadas:
1. Obtenha chave gratuita em https://www.exchangerate-api.com/
2. Use no código:

```python
currency = CurrencyAPI(api_key="sua_chave_aqui")
```

## Exemplos Rápidos

### GitHub
```python
from batata import GitHubAPI

github = GitHubAPI()
user = github.get_user("torvalds")
print(f"Nome: {user['name']}")

repos = github.search_repos("python", sort="stars", per_page=5)
print(f"Encontrados: {repos['total_count']} repositórios")
```

### Weather
```python
from batata import WeatherAPI

weather = WeatherAPI(api_key="sua_chave")
clima = weather.get_current_weather("São Paulo", units="metric")
print(f"Temperatura: {clima['main']['temp']}°C")
```

### Currency
```python
from batata import CurrencyAPI

currency = CurrencyAPI()
resultado = currency.convert(100, "USD", "BRL")
print(f"100 USD = {resultado['result']:.2f} BRL")
```

### Pokemon
```python
from batata import PokeAPI

poke = PokeAPI()
data = poke.get_pokemon_info("pikachu")
print(data)
```

## Tratamento de Erros

Todas as APIs podem lançar exceções. Use try/except:

```python
try:
    weather = WeatherAPI(api_key="chave_invalida")
    clima = weather.get_current_weather("São Paulo")
except Exception as e:
    print(f"Erro: {e}")
```

## Rate Limits

- **GitHub**: 60 requisições/hora (sem autenticação), 5000/hora (com token)
- **Weather**: Varia por plano (gratuito: 1000 chamadas/dia)
- **Currency**: Sem limite na versão gratuita básica
- **Pokemon**: Sem limite oficial, mas use com moderação

## Contribuindo

Encontrou um bug ou tem sugestão de melhoria? Abra uma issue no repositório!
