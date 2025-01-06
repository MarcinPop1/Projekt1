"""
Moduł odpowiedzialny za ładowanie i przetwarzanie danych JSON dla systemu wizualizacji grafu.

Ten moduł zawiera funkcje do wczytywania danych z plików JSON oraz ich konwersji
do formatu odpowiedniego dla wizualizacji grafu. Obsługuje również walidację
danych wejściowych i zarządzanie błędami.

Attributes:
    DEFAULT_ENCODING (str): Domyślne kodowanie używane do odczytu plików JSON.
"""

import json
from typing import Dict, List, Any

def load_json_file(file_path: str) -> Dict[str, Any]:
    """
    Wczytuje i parsuje plik JSON.

    Args:
        file_path (str): Ścieżka do pliku JSON.

    Returns:
        Dict[str, Any]: Słownik zawierający dane z pliku JSON.

    Raises:
        FileNotFoundError: Gdy plik nie zostanie znaleziony.
        json.JSONDecodeError: Gdy wystąpi błąd podczas parsowania JSON.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Nie znaleziono pliku: {file_path}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Błąd parsowania JSON: {str(e)}", e.doc, e.pos)

def validate_graph_data(data: Dict[str, Any]) -> bool:
    """
    Sprawdza poprawność struktury danych grafu.

    Args:
        data (Dict[str, Any]): Dane grafu do walidacji.

    Returns:
        bool: True jeśli dane są poprawne, False w przeciwnym razie.
    """
    required_keys = ['nodes', 'edges']
    return all(key in data for key in required_keys)

# Reszta implementacji...

