'''
Napisz program, który poinformuje użytkownika o aktualnej godzinie za pomocą głosu po wpisaniu przez Ciebie odpowiedniego ciągu znaków.
Nie powinno mieć znaczenia to czy używasz małych, czy dużych liter.
Uruchomienie powinno odbyć się poprzez linię komend (funkcja input()).
PRZYKŁAD:
- input: 'What time is it?'
- SPEAKING: 'The time is 12:00'
Do zrealizowania zadania potrzebne będą biblioteki pyttsx3 i datetime

Kroki, które należy podjąć:
1) za pomocą biblioteki pyttsx3 należy zainicjować silnik, który będzie odpowiedzialny za zamianę tekstu na mowę.
2) wczytać tekst przy użyciu funkcji input()
3) uruchomić silnik i sprawić, by program mówił (łącznie w tym kroku wykorzystuje się dwie metody obiektu engine)
4) pobrać aktualną datę przy użyciu metody modułu datetime i dodaniu jej do outputu

'''


from datetime import datetime
import pyttsx3

if __name__ == '__main__':
    pass
