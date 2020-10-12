# Akcelerometr
 
## Projekt akcelerometru działającego docelowo na Raspberry PI.

### Działanie:
1. Odczytywanie danych z miernika i wysyłanie ich do bazy danych (influx).
2. Korzystanie z serwisu Grafana do wizualizacji danych na 3 osiach.
3. Wtyczka do przeglądarki umorzliwiająca rozpoczęcie i zakończenie pomiaru z poziomu przeglądarki (każdy pomiar jest przechowywany w osobnej tabeli influx'a).
4. Skrypt w bash'u uruchamiający wszystkie elementy - finalnie widoczna jest tylko grafana oraz wtyczka.