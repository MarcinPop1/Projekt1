"""
Główny moduł aplikacji do wizualizacji grafów.

Ten moduł zawiera główną logikę aplikacji, w tym inicjalizację interfejsu
użytkownika i obsługę interakcji z użytkownikiem.

Example:
    Aby uruchomić aplikację:

        $ python main.py

Attributes:
    DEFAULT_CONFIG (Dict): Domyślna konfiguracja aplikacji.
    WINDOW_SIZE (Tuple[int, int]): Rozmiar okna aplikacji (szerokość, wysokość).
"""

from typing import Dict, Tuple
from json_loader import load_json_file, validate_graph_data
from shortest_path import dijkstra

class GraphVisualizer:
    """
    Klasa odpowiedzialna za wizualizację grafu.

    Attributes:
        graph (Dict): Struktura danych reprezentująca graf.
        window_size (Tuple[int, int]): Rozmiar okna wizualizacji.
    """

    def __init__(self, graph_data: Dict, window_size: Tuple[int, int] = (800, 600)):
        """
        Inicjalizuje obiekt GraphVisualizer.

        Args:
            graph_data (Dict): Dane grafu w formacie JSON.
            window_size (Tuple[int, int], optional): Rozmiar okna. Defaults to (800, 600).

        Raises:
            ValueError: Gdy dane grafu są niepoprawne.
        """
        if not validate_graph_data(graph_data):
            raise ValueError("Niepoprawne dane grafu")
        self.graph = graph_data
        self.window_size = window_size

    def visualize(self) -> None:
        """
        Wyświetla wizualizację grafu.

        Tworzy okno z interaktywną wizualizacją grafu, umożliwiając
        użytkownikowi manipulację widokiem i analizę struktury.
        """
        # implementacja...

def main():
    """
    Główna funkcja aplikacji.

    Wczytuje dane grafu, inicjalizuje wizualizację i uruchamia
    interfejs użytkownika.
    """
    try:
        data = load_json_file("graph.json")
        visualizer = GraphVisualizer(data)
        visualizer.visualize()
    except Exception as e:
        print(f"Błąd: {str(e)}")

if __name__ == "__main__":
    main()
