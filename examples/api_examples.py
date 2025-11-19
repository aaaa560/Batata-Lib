"""
Exemplos de uso das APIs do batata-lib
"""

from batata import GitHubAPI, WeatherAPI, CurrencyAPI, PokeAPI


# ====================
# GitHub API Examples
# ====================

def github_examples():
    """Exemplos de uso da GitHub API"""
    print("\n=== GitHub API Examples ===\n")
    
    # Inicializar (sem token para acesso público)
    github = GitHubAPI()
    
    # Com token para maior rate limit
    # github = GitHubAPI(token="seu_token_aqui")
    
    # 1. Buscar informações de um usuário
    print("1. Buscando usuário...")
    user = github.get_user("torvalds")
    print(f"Nome: {user.get('name')}")
    print(f"Bio: {user.get('bio')}")
    print(f"Repositórios públicos: {user.get('public_repos')}")
    
    # 2. Listar repositórios
    print("\n2. Listando repositórios...")
    repos = github.get_repos("torvalds", per_page=5)
    for repo in repos[:3]:
        print(f"- {repo['name']}: {repo['description']}")
    
    # 3. Buscar repositório específico
    print("\n3. Buscando repositório específico...")
    repo = github.get_repo("python", "cpython")
    print(f"Repo: {repo['full_name']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Linguagem: {repo['language']}")
    
    # 4. Pesquisar repositórios
    print("\n4. Pesquisando repositórios...")
    results = github.search_repos("machine learning", sort="stars", per_page=3)
    print(f"Total encontrado: {results['total_count']}")
    for repo in results['items']:
        print(f"- {repo['full_name']} ({repo['stargazers_count']} stars)")
    
    # 5. Listar commits
    print("\n5. Últimos commits...")
    commits = github.get_repo_commits("python", "cpython", per_page=3)
    for commit in commits:
        print(f"- {commit['commit']['message'][:50]}... por {commit['commit']['author']['name']}")


# ====================
# Weather API Examples
# ====================

def weather_examples():
    """Exemplos de uso da Weather API"""
    print("\n=== Weather API Examples ===\n")
    
    # IMPORTANTE: Você precisa de uma chave de API gratuita
    # Obtenha em: https://openweathermap.org/api
    api_key = "SUA_CHAVE_AQUI"  # Substitua pela sua chave
    
    weather = WeatherAPI(api_key)
    
    # 1. Clima atual
    print("1. Clima atual em São Paulo...")
    try:
        current = weather.get_current_weather("São Paulo", units="metric")
        print(f"Temperatura: {current['main']['temp']}°C")
        print(f"Sensação térmica: {current['main']['feels_like']}°C")
        print(f"Descrição: {current['weather'][0]['description']}")
        print(f"Umidade: {current['main']['humidity']}%")
    except Exception as e:
        print(f"Erro (verifique sua API key): {e}")
    
    # 2. Previsão do tempo
    print("\n2. Previsão para os próximos dias...")
    try:
        forecast = weather.get_forecast("Rio de Janeiro", units="metric", cnt=3)
        for item in forecast['list']:
            print(f"- {item['dt_txt']}: {item['main']['temp']}°C - {item['weather'][0]['description']}")
    except Exception as e:
        print(f"Erro (verifique sua API key): {e}")
    
    # 3. Clima por coordenadas
    print("\n3. Clima por coordenadas (Brasília)...")
    try:
        coords_weather = weather.get_weather_by_coords(-15.7801, -47.9292, units="metric")
        print(f"Local: {coords_weather['name']}")
        print(f"Temperatura: {coords_weather['main']['temp']}°C")
    except Exception as e:
        print(f"Erro (verifique sua API key): {e}")


# ====================
# Currency API Examples
# ====================

def currency_examples():
    """Exemplos de uso da Currency API"""
    print("\n=== Currency API Examples ===\n")
    
    # Inicializar (sem chave usa versão gratuita limitada)
    currency = CurrencyAPI()
    
    # Com chave de API (opcional, para mais recursos)
    # currency = CurrencyAPI(api_key="sua_chave_aqui")
    
    # 1. Obter taxas de câmbio
    print("1. Taxas de câmbio para USD...")
    rates = currency.get_rates("USD")
    if 'rates' in rates:
        print(f"USD -> BRL: {rates['rates'].get('BRL', 'N/A')}")
        print(f"USD -> EUR: {rates['rates'].get('EUR', 'N/A')}")
        print(f"USD -> JPY: {rates['rates'].get('JPY', 'N/A')}")
    
    # 2. Converter moedas
    print("\n2. Convertendo 100 USD para BRL...")
    conversion = currency.convert(100, "USD", "BRL")
    if 'result' in conversion:
        print(f"100 {conversion['base']} = {conversion['result']:.2f} {conversion['target']}")
        print(f"Taxa de câmbio: {conversion['rate']}")
    
    # 3. Outras conversões
    print("\n3. Outras conversões...")
    conversions = [
        (50, "EUR", "USD"),
        (1000, "BRL", "USD"),
        (100, "GBP", "EUR")
    ]
    
    for amount, from_curr, to_curr in conversions:
        result = currency.convert(amount, from_curr, to_curr)
        if 'result' in result:
            print(f"{amount} {from_curr} = {result['result']:.2f} {to_curr}")
    
    # 4. Listar moedas suportadas
    print("\n4. Moedas suportadas (primeiras 10)...")
    supported = currency.get_supported_currencies()
    if 'supported_codes' in supported:
        codes = supported['supported_codes'][:10]
        print(f"Total: {len(supported['supported_codes'])} moedas")
        print(f"Exemplos: {', '.join(codes)}")


# ====================
# Pokemon API Examples
# ====================

def pokemon_examples():
    """Exemplos de uso da Pokemon API"""
    print("\n=== Pokemon API Examples ===\n")
    
    poke = PokeAPI()
    
    # 1. Buscar informações de um Pokémon
    print("1. Buscando informações de Pikachu...")
    pokemon_data = poke.get_pokemon_info("pikachu")
    for name, data in pokemon_data.items():
        print(f"\nPokémon: {name.capitalize()}")
        print("Habilidades:")
        for ability in data['abilidades']:
            print(f"  - {ability['name']}")
    
    # 2. Busca com fuzzy matching
    print("\n2. Busca com fuzzy matching (erro de digitação)...")
    pokemon_data = poke.get_pokemon_info("charizar")  # Digitado errado propositalmente
    for name in pokemon_data.keys():
        print(f"Encontrado: {name}")


# ====================
# Main
# ====================

if __name__ == "__main__":
    print("╔════════════════════════════════════════╗")
    print("║  Exemplos de APIs - Batata-Lib        ║")
    print("╚════════════════════════════════════════╝")
    
    # Executar exemplos
    # Descomente as funções que deseja testar
    
    github_examples()
    
    # NOTA: Precisa de chave de API
    # weather_examples()
    
    currency_examples()
    
    pokemon_examples()
    
    print("\n" + "="*50)
    print("Exemplos concluídos!")
    print("="*50)
