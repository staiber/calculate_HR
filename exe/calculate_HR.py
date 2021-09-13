# Эта программа рассчитывает зоны физических нагрузок по формуле Карвонена.


# Формула Карвонена:
# _______________________________________________________________________________
# (ЧССмакс — ЧССпокой) х интенсивность + ЧССпокой = ЧСС (необходимый для зоны)
# _______________________________________________________________________________


#                     Зоны физических нагрузок:            Интенсивность:

# Максимальная нагрузка             90% - 100%                 0.9 - 1

# Анаэробная зона                   80% - 90%                  0.8 - 0.9

# Аэробная зона                     70% - 80%                  0.7 - 0.8

# Начало жиросжигающей зоны	        60% - 70%                  0.6 - 0.7

# Зона легкой активности		    40 - 60 %                  0.4 - 0.6


# Получаем возраст
age = input("Введите ваш возраст: ")

print("\n")

# Получаем пульс в состоянии покоя
heartRate_rest = float(input("Введите ваш пульс в состоянии покоя: "))

# Рассчитываем максимальный пульс по формуле
heartRate_max = 205.8 - (0.685 * float(age))

# Рассчитываем тренировочные зоны по формуле: (ЧССмакс — ЧССпокой) х интенсивность + ЧССпокой = ЧССтрен
heartRate_exercise_04 = (heartRate_max - heartRate_rest) * 0.4 + heartRate_rest
heartRate_exercise_06 = (heartRate_max - heartRate_rest) * 0.6 + heartRate_rest
heartRate_exercise_07 = (heartRate_max - heartRate_rest) * 0.7 + heartRate_rest
heartRate_exercise_08 = (heartRate_max - heartRate_rest) * 0.8 + heartRate_rest
heartRate_exercise_09 = (heartRate_max - heartRate_rest) * 0.9 + heartRate_rest

# Выводим результат программы на экран
print("\n")

print("Ваш максимальный пульс: ", int(heartRate_max))

print("\n")

print("Ваши тренировочные зоны находятся в следующих пределах:")

print("\n\n")

print("\n")

print("Зона легкой активности:    ", int(heartRate_exercise_04), " - ", int(heartRate_exercise_06), " Уд/мин")

print("\n")

print("Начало жиросжигающей зоны: ", int(heartRate_exercise_06), " - ", int(heartRate_exercise_07), " Уд/мин")

print("\n")

print("Аэробная зона:             ", int(heartRate_exercise_07), " - ", int(heartRate_exercise_08), " Уд/мин")

print("\n")

print("Анаэробная зона:           ", int(heartRate_exercise_08), " - ", int(heartRate_exercise_09), " Уд/мин")

print("\n")

print("Максимальная нагрузка:     ", int(heartRate_exercise_09), " - ", int(heartRate_max), " Уд/мин")

print("\n\n")

input("Нажмите \"Enter\" для закрытия программы.")
