# AGENTS.md - Potato-Lib (batata-lib)

## Project Overview

**Potato-Lib** (`batata-lib`) is a personal Python utility library designed to simplify common development tasks. The
library provides a collection of modules for file management, CLI building, web scraping, API interactions, mathematical
operations, and colorized terminal output.

**Current Version:** 0.1.5  
**Repository:** https://github.com/aaaa560/potato-lib  
**Author:** Decaptado  
**Python Requirements:** >= 3.10

---

## Recent Changes (Last Update: 2025-11-18)

### Major Update: Module Reorganization and API Support

The most recent commit introduced significant structural improvements and new functionality:

#### Renamed Modules

- **`atalhos.py` → `aliases.py`**: Renamed for better English naming consistency. Contains shortcut functions for user
  output (`info`, `warn`, `err`, `out`, `perguntar`).

#### New Module: `apis.py`

Added comprehensive API interaction support:

- **`API` class**: Generic base class for working with any REST API
    - Configurable headers with sensible defaults
    - Support for GET and POST requests
    - Easy endpoint management

- **`PokeAPI` class**: Specialized implementation for Pokémon API
    - Get Pokémon information by name with fuzzy matching
    - Retrieves abilities and other data
    - Uses `difflib.get_close_matches` for name suggestions

- **Standalone functions**:
    - `get(url)`: Simple GET request wrapper
    - `post(url, payload)`: Simple POST request wrapper
    - `find_pokemon(query)`: Find Pokémon names with fuzzy matching

---

## Module Structure

### Core Modules

#### 1. **geral.py** - General Utilities

Core functions for terminal I/O and basic operations:

- `mostra()`: Enhanced print with color/style support
- `get_num()`: Safe numeric input with validation and retry
- `get_inp()`: Styled input prompt
- `par()`: Check if number is even
- `primo()`: Check if number is prime
- `divisivel()`: Check divisibility
- `raiz_qdd()`: Calculate square root

#### 2. **aliases.py** (formerly atalhos.py)

Convenient output shortcuts with automatic formatting:

- `info()`: Display info messages (cyan, bold)
- `warn()`: Display warnings (yellow, bold)
- `err()`: Display errors (red, bold)
- `out()`: Display results (blue, bold)
- `perguntar()`: Styled question prompt

All functions support custom colors and modes.

#### 3. **apis.py** - API Integration (NEW)

REST API interaction utilities:

- `API`: Base class for API clients
- `PokeAPI`: Ready-to-use Pokémon API client
- Helper functions: `get()`, `post()`, `find_pokemon()`

#### 4. **cli.py** - Command Line Interface Builder

Simplified argparse wrapper for building CLI applications:

- **`CLI` class**: Easy-to-use command-line interface builder
    - Automatic version handling
    - Subcommand support with aliases
    - Global arguments and flags
    - Error handling with keyboard interrupt support
    - Auto-passes parsed args to command functions

**Example Usage:**

```python
from batata import CLI

cli = CLI("myapp", "My Application", version="1.0.0")
cli.add_command("start", start_func, help="Start the service")
cli.add_flag("--verbose", "-v", help="Verbose output")
cli.run()
```

#### 5. **files.py** - File Management

Unified file operations for multiple formats:

- **`FileManager` class**: Handle text files
    - Auto-detects file type from extension
    - Create, read, and write operations
    - Automatic file creation on missing files
    - Error handling with user-friendly messages
- **`JSONManager` class**: Handles JSON files
    - Create, read and write operations
    - Automatic file creation on missing files
    - JSON support with configurable indentation
    - Erro handling with user-friendly messages
- **`CSVManager` class**: Handle CSV files
    - CSV support with headers
    - Automatic file creation on missing files
    - Erro handling with user-friendly messages

#### 6. **scraping.py** - Web Scraping

Simple web scraping using BeautifulSoup:

- **`Scraper` class**: Extract data from web pages
    - `scrape()`: Get prettified HTML
    - `get_content(tag)`: Extract all elements by tag
    - `get_title()`: Get page title
    - `get_links()`: Extract all links
    - `get_images()`: Extract all images
    - `get_class(classe)`: Extract by class name
    - `clean_tags(tag)`: Get text content only

#### 7. **colors.py** - Terminal Colors

ANSI color codes and styling:

- **Predefined colors**: BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, GRAY, WHITE
- **Modes**: BOLD, NORMAL, ITALIC, UNDERLINE
- **`Color` class**: Programmatic color/mode creation

#### 8. **math.py** - Mathematical Operations

Common math utilities:

- `produto()`: Multiply all values
- `fat()`: Calculate factorial (with verbose option)
- `soma()`: Sum all numbers
- `area()`: Calculate area of geometric shapes

#### 9. **formas.py** - Geometric Shapes

Classes for geometric calculations:

- **Base**: `FormaQualquer` (abstract)
- **Shapes**: `Retangulo`, `Circulo`, `Triangulo`, `Quadrado`, `Trapezio`, `Losangulo`
- Each shape implements `area()` method
- Type alias: `FormaGeometrica` for all shapes

#### 10. **errors.py** - Custom Exceptions

Specialized error classes:

- **`ErroGenerico`**: Base exception with message and code
- **`ParamError`**: Parameter validation errors
- **`ScrapingError`**: Web scraping operation errors

---

## Key Features

### 🎨 Colorized Output

All output functions support customizable colors and styles using ANSI codes.

### 🔧 Type Safety

Modern Python type hints throughout the codebase (compatible with Python 3.10+).

### 📁 Multi-format File Support

Single `FileManager` class handles JSON, CSV, and text files automatically.

### 🌐 API-Ready

Built-in support for REST APIs with a clean, extensible architecture.

### 🛠️ CLI Building Made Easy

Create professional command-line tools with minimal boilerplate.

### 🔍 Web Scraping

Extract data from websites with simple, intuitive methods.

---

## Dependencies

**Required:**

- `requests >= 2.0`
- `beautifulsoup4 >= 4.0.0`

**Development:**

- `pytest >= 7.0`
- `pytest-cov >= 4.0`

---

## Installation

```bash
pip install batata-lib
```

---

## Usage Examples

### Using Aliases for Output

```python
from batata import info, warn, err, out

info("Application started")
warn("Low memory")
err("Connection failed")
out("Result: 42")
```

### Building a CLI Application

```python
from batata import CLI


def start(args):
    print(f"Starting with verbose={args.verbose}")


cli = CLI("myapp", "My Application")
cli.add_flag("--verbose", "-v")
cli.add_command("start", start, help="Start service")
cli.run()
```

### Working with APIs

```python
from batata import PokeAPI

api = PokeAPI()
pokemon_data = api.get_pokemon_info("pikachu")
print(pokemon_data)
```

### Managing Files

```python
from batata import FileManager

# JSON file
fm = FileManager(".", "data.json")
fm.write_json({"name": "test", "value": 123})
data = fm.read_json()

# CSV file
csv_fm = FileManager(".", "data.csv")
csv_fm.creat_csv(header=["name", "age"])
csv_fm.write_csv(["Alice", "30"])
```

### Web Scraping

```python
from batata import Scraper

scraper = Scraper("https://example.com")
title = scraper.get_title()
links = scraper.get_links()
content = scraper.get_content("p")
```

---

## Development Status

**Status:** Alpha (Development Status :: 3 - Alpha)

The library is actively developed and primarily maintained for personal use. While functional, breaking changes may
occur between versions.

---

## Notes for AI Agents

When working with this codebase:

1. **Naming Convention**: The project uses Portuguese names internally (`batata` = potato, `mostra` = show, etc.) but is
   moving toward English for public-facing APIs (e.g., `aliases.py` instead of `atalhos.py`).

2. **Error Handling**: Custom exceptions (`ParamError`, `ScrapingError`) should be used for domain-specific errors. They
   support error codes and detailed messages.

3. **Type Hints**: All new code should include proper type hints. The codebase uses Python 3.10+ features like union
   types (`|`).

4. **Color Support**: When adding output functions, consider integrating with the existing color system via `colors.py`
   or `aliases.py`.

5. **File Operations**: Use `FileManager` for file I/O instead of raw file operations for consistency.

6. **API Extensions**: New API clients should inherit from the `API` base class in `apis.py`.

7. **Testing**: While pytest is listed in dev dependencies, test coverage should be expanded.

---

## Future Considerations

- Add more API integrations beyond PokeAPI
- Expand geometric shapes (3D shapes, etc.)
- Add comprehensive test coverage
- Improve documentation with more examples
- Consider internationalization (i18n) for output messages
- Add async support for API operations
- Enhance CLI with progress bars and interactive prompts
