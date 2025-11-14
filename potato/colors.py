COLORS: dict[str, dict[str, str]] = {
    'BOLD': {
        'BLACK': '\033[1;30m',
        'RED': '\033[1;31m',
        'GREEN': '\033[1;32m',
        'YELLOW': '\033[1;33m',
        'BLUE': '\033[1;34m',
        'PURPLE': '\033[1;35m',
        'CYAN': '\033[1;36m',
        'GRAY': '\033[1;37m',
        'WHITE': '\033[1;38m'
    },
    'NOR': {
        'BLACK': '\033[;30m',
        'RED': '\033[;31m',
        'GREEN': '\033[;32m',
        'YELLOW': '\033[;33m',
        'BLUE': '\033[;34m',
        'PURPLE': '\033[;35m',
        'CYAN': '\033[;36m',
        'GRAY': '\033[;37m',
        'WHITE': '\033[;38m'
    },
    'ITAL': {
        'BLACK': '\033[3;30m',
        'RED': '\033[3;31m',
        'GREEN': '\033[3;32m',
        'YELLOW': '\033[3;33m',
        'BLUE': '\033[3;34m',
        'PURPLE': '\033[3;35m',
        'CYAN': '\033[3;36m',
        'GRAY': '\033[3;37m',
        'WHITE': '\033[3;38m'
    },
    'UND': {
        'BLACK': '\033[4;30m',
        'RED': '\033[4;31m',
        'GREEN': '\033[4;32m',
        'YELLOW': '\033[4;33m',
        'BLUE': '\033[4;34m',
        'PURPLE': '\033[4;35m',
        'CYAN': '\033[4;36m',
        'GRAY': '\033[4;37m',
        'WHITE': '\033[4;38m'
    }
}
MODES: dict[str, str] = {
    'ITAL': '\033[3m',
    'BOLD': '\033[1m',
    'UND': '\033[4m'
}
