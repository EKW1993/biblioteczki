Instalacja
a) Sklonuj repozytorium na swój komputer. b) Przejdź do katalogu z aplikacją. c) Zainstaluj zależności, uruchamiając polecenie pip install -r requirements.txt.
Jak używać? a) Uruchom aplikację, wykonując komendę python app.py lub flask run. b) Przejdź do przeglądarki internetowej i wpisz adres http://localhost:5000/book. c) Używaj aplikacji zgodnie z instrukcjami na stronie.
Tematyka aplikacji Jest to aplikacja webowa napisana w języku Python w oparciu o framework Flask. Funkcjonalności aplikacji obejmują: a) tworzenie nowych wpisów - użytkownik może dodać nową książkę do listy przez wypełnienie formularza i kliknięcie przycisku "Go", b) aktualizacja starych wpisów - użytkownik może edytować istniejący wpis, przechodząc do strony szczegółów książki i wprowadzając zmiany w formularzu. c) wyświetlanie listy - na stronie głównej użytkownik może zobaczyć listę wszystkich książek w formie tabeli. Alikacja korzysta z formularzy WTForms do walidacji danych wprowadzanych przez użytkownika. Formularze zawierają pola takie jak tytuł książki, autor i rok wydania.
