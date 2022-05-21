'''
Napisz program, który poinformuje użytkownika o aktualnej godzinie za pomocą głosu.
Uruchomienie powinno odbyć się poprzez linię komend (funkcja input())
PRZYKŁAD:
- input: 'What time is it?'
- SPEAKING: 'The time is 12:00'
Do zrealizowania zadania potrzebne będą biblioteki pyttsx3 i datetime

Kroki, które należy podjąć:
1) za pomocą biblioteki pyttsx3 należy zainicjować silnik, który będzie odpowiedzialny za zamianę tekstu na mowę.
2) wczytać tekst przy użyciu funkcji input()
3) uruchomić silnik i sprawić, by program mówił (łącznie w tym kroku wykorzystuje się dwie komendy obiektu engine)
4) pobrać aktualną datę przy użyciu metody modułu datetime i dodaniu jej do outputu

# PRZYDATNE ŹRÓDŁA:
https://pypi.org/project/pyttsx3/ (zajrzyj do Usage)
https://stackoverflow.com/questions/44858120/how-to-change-the-voice-in-pyttsx3
https://techtutorialsx.com/2017/05/06/python-pyttsx-changing-speech-rate-and-volume/

'''



