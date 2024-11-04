# Gra_w_zgadywanie_flask

Ten projekt aplikacja webowa w Flasku, która implementuje grę „Zgadnij liczbę”, gdzie komputer zgaduje liczbę wybraną przez użytkownika z przedziału od 0 do 1000. Użytkownik informuje komputer, czy jego zgadywana liczba jest „Za duża”, „Za mała” czy „Trafiona”. Gra trwa maksymalnie 10 ruchów, a zakres zgadywania zawęża się przy każdej odpowiedzi użytkownika.

# Struktura kodu
HTML: Aplikacja zawiera trzy szablony HTML zapisane w formie tekstu w kodzie Python:

### HTML
Strona początkowa z formularzem do rozpoczęcia gry.
### HTML_GUESS 
Strona wyświetlająca propozycję liczby komputera oraz przyciski do odpowiedzi użytkownika („Too big”, „Too small”, „You win”).
### HTML_WIN
Strona wyświetlająca komunikat wygranej, gdy komputer zgadnie poprawną liczbę.
### Funkcja guess()
Jedyna funkcja główna aplikacji Flask, uruchamiana na adresie /. Odpowiada za obsługę żądania typu GET oraz POST.

 GET: Ustawia początkowy zakres 0-1000 i generuje stronę początkową.
 POST: Odczytuje odpowiedzi użytkownika i odpowiednio aktualizuje zakres, by komputer zawęził swoje zgadywanie. Obsługuje trzy możliwe odpowiedzi użytkownika:
 „Too big” – zmienia górny zakres (max_number) na aktualnie zgadywaną liczbę.
 „Too small” – zmienia dolny zakres (min_number) na aktualnie zgadywaną liczbę.
 „You win” – zwraca stronę wygranej.
 Przesyłanie zmiennych min i max: Pola hidden w formularzu przesyłają aktualny zakres (minimalną i maksymalną liczbę) z powrotem na serwer, by każda kolejna propozycja zgadywania była dokładniejsza.
