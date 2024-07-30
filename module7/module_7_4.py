
team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья!"

tasks_total = team1_num + team2_num

print("В команде Мастера кода участников: %d ! " % team2_num)
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))
print("Команда Волшебники данных решила задач: {} !".format(score2))
print(" Волшебники данных решили задачи за {:.1f} с !".format(team2_time))
print(f"Команды решили {score1} и {score2} задач.")
print(f"Результат битвы: {result}")
print(f"Сегодня было решено {team1_num + team2_num} задач, в среднем по {(team1_time + team2_time) / (team1_num + team2_num):.1f} секунды на задачу!.")