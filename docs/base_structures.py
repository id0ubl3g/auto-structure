from typing import Dict, List

Lightweight_API: Dict[str, List[str]] = {
    'src': [
        'modules',  
        'utils/shared',
        'temp',
        'logs',
        'api'
    ],
    'tests': [],
    'config': [],
    'docs': []
}

Extended_API: Dict[str, List[str]]  = {
    'app': [
        'controllers',
        'services',
        'modules',
        'routes',
        'models',
        'views/handlers',
        'utils/shared',
        'temp',
        'logs'
    ],
    'tests': [],
    'config': [],
    'docs': []
}
