ALHE Projekt wstępny

Wiktor Grzesiuk Robert Lichman

Temat 13: Sygnalizacja świetlna

  

Znając dobowe profile natężenia ruchu na każdej z 4 dróg wjeżdżających na dane skrzyżowanie, opracować strategię zmiany sygnalizacji. Celem jest minimalizacja oczekiwanej wartości sumarycznego czasu spędzonego na skrzyżowaniu przez uczestników ruchu.

Opis zagadnienia, założenia

Dane jest jedno skrzyżowanie dwóch dróg. Przyjmujemy że każda z dróg ma osobne pasy do skręcania w prawo i jazdy prosto, skręcania, w lewo i do jazdy prosto jak na załączonym obrazku. Sygnalizacja świetlna nie dopuszcza możliwości wystąpienia kolizji tj. można jechać prosto i w prawo, oraz osoby jadące z naprzeciwka mogą jechać prosto i w prawo lub jeden z czterech kierunków może jechać we wszystkie strony. Skręt w lewo zezwala również na zawracanie, dlatego skręt w prawo z prostopadłej strony jest zabroniony. Cykle zaczyna się od tego, że jeden kierunek ma możliwość jazdy we wszystkie strony. Potem sygnalizator pozwalający na skręt w lewo włącza światło czerwone. Wtedy przeciwny kierunek może jechać prosto i w prawo. Później kierunek od którego zaczynaliśmy ma czerwone na wszystkich pasach, a na przeciwnym jest możliwość jazdy we wszystkich kierunkach. Po czy następuje światło czerwone dla wszystkich i ten sam cykl zaczyna się dla prostopadłego kierunku. Nie uwzględniamy zmiany sygnalizacji dla pieszych. Zakładamy format danych w którym mamy dostępne informacje w jakim momencie dany samochód znalazł się na skrzyżowaniu, w którym kierunku jechał. Zakładamy że czas samochodu potrzebny na ruszenie po zmianie światła jest liniowy względem pozycji na pasie od sygnalizacji. Czas ruszenia pierwszego samochodu jest stały. Dane w naszym zadaniu będą generowane w sposób losowy z rozkładem zwiększającym ilość samochodów w godzinach 7-8 i 16-17. Dodatkowo załóżmy, że szlak do centrum miasta jest uczęszczany rano przez ludzi jadących do pracy. Z kolei w godzinach 16-17 zwiększony jest ruch z centrum miasta.

Zdefiniowanie przestrzeni przeszukiwania

Przestrzeń przeszukiwań zdefiniowana będzie za pomocą 8 ciągów po 48 liczb oznaczających czas światła zielonego dla danego kierunku. Zauważmy, że dwa prawe pasy mają wspólny sygnalizator, oraz czas zielonego światła dla skrętu w lewo &lt;= czas światła zielonego dla pozostałych dwóch pasów. Rozdzielczość czasu: 1s. Maksymalny czas świecenia się zielonego światła na jednym pasie to 2min. Sąsiedztwem będzie zestaw ciągów które różnią się tylko na jednej pozycji czyli zmieniamy długość cyklu jednego sygnalizatora dla danej “pół godziny”

Wstępna propozycja postaci funkcji celu i przykładowe zadanie z obliczoną wartością tej funkcji 

Celem naszego projektu jest znalezienie takiej sekwencji zmian sygnalizacji świetlnej, która da najmniejszy sumaryczny czas oczekiwania dla wszystkich pojazdów. Funkcją celu będzie więc średnia czasów oczekiwania dla pojazdów przejeżdżających przez skrzyżowanie w czasie jednej doby. Przykładowe obliczenie mogłoby wyglądać w następujący sposób:

Mamy dany dobowy profil natężenia ruchu. W ramach tego profilu wiemy ile samochodów chciało w danej godzinie przejechać przez skrzyżowanie. Znając czasy zmian sygnalizacji i przyjmując standardowe wartości czasu potrzebnego na ruszenie ze świateł, wyliczamy czas oczekiwania dla każdego samochodu. Sumę czasów następnie dzielimy przez ilość samochodów, które przejechały przez dobę. 

Funkcja celu nie będzie bezpośrednio bazowała na przepustowości skrzyżowania. Jednak czas potrzebny na ruszenie ze świateł będzie ograniczał przepustowość w cyklu. Im więcej samochodów czeka na skrzyżowaniu, tym mniejsza przepustowość. Im mniej czasu samochód będzie potrzebował na przejazd przez skrzyżowanie, tym przepustowość będzie większa.

 

Przykład:

Załóżmy uproszczoną wersję. Cykle są stałej długości. Jazda na wprost trwa 30s. Jazda w lewo 10s. Pełny cykl trwa 2min. Załóżmy że przez dobę przejechały tylko 4 samochody i wszystkie jechały z południa. Cykl zaczyna się o pełnej godzinie i pierwszym kierunkiem który ma dostępne wszystkie kierunki jest kierunek z południa na północ.

Dane:

10:12:34      1, 2  (1 = z południa,  2= drugi pas)

12:43:55      1, 1  (w lewo)

12:44:00      1, 1 (w lewo)

12:44:20      1, 3 (w prawo lub prosto z prawego pasa)

Pierwszy będzie czekał 86 s na zielone światło + jako że czekał, to trzeba doliczyć 5 s opóźnienia potrzebnego na osiągnięcie prędkości i 5s bo tyle trwa standardowy przejazd. Drugi i trzeci stoją zanim włączy się zielone światło. Nr 2 stoi 5 s, Nr 3 stoi 0s, ale musiał się zatrzymać. Więc czas numeru 2. to 5 s, które czekał + 5s na osiągnięcie prędkości + 5s na przejazd =15s. Nr. 3   5s bo był drugi w kolejce + 5s na osiągnięcie prędkości + 5 na przejazd. Nr 4 nie czeka wcale i nie traci prędkości więc cały czas to czas przejazdu=5s. Wartość funkcji celu dla tych danych wynosi 

F=(96+15+10+5)/4=31.

 

Określenie metody optymalizacji (metaheurystyki), która będzie zastosowana do rozwiązania zadania

Planujemy użyć algorytmu symulowanego wyżarzania. Zmiana temperatury będzie geometryczna. Sąsiedztwo w zbiorze poszukiwań będzie definiowane poprzez różnicę na jednym miejscu w ciągu liczbowym opisującym dane rozwiązanie. Wartość początkowa będzie generowana losowo, jednak z pewnym uwzględnieniem danej instancji problemu tak, aby znalazł się on możliwie blisko ekstremum. Strojenia wymagać będzie temperatura. 

Deklaracja przewidywanych wyników pracy

Wynikiem przeszukiwania będzie optymalna sekwencja zmian sygnalizacji świetlnej, tj. ciąg dający najlepsze wyniki dla wszystkich przeprowadzonych eksperymentów. Zostanie przeprowadzone wiele eksperymentów dla różnych danych.
