#CONSTANTES
DAY = 24
MINUTE = 60

#VARIAVEIS
total_time_hour = 0
total_time_minute = 0
initial_hour, initial_minute, final_hour, final_minute = map(int,input().split())

total_time_hour = final_hour - initial_hour
if total_time_hour < 0:
    total_time_hour = 24 + total_time_hour

total_time_minute = final_minute - initial_minute
if total_time_minute < 0:
    total_time_minute = 60 + total_time_minute
    total_time_hour -= 1


if final_minute == initial_minute and final_hour == initial_hour:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

else:
    print("O JOGO DUROU ",total_time_hour," HORA(S) E ",total_time_minute," MINUTO(S)\n")

