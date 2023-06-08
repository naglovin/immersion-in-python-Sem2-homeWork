# Напишите программу банкомат.
# ✔Начальная сумма равна нулю
# ✔Допустимые действия: пополнить, снять, выйти
# ✔Сумма пополнения и снятия кратны 50 у.е.
# ✔Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔Нельзя снять больше, чем на счёте
# ✔При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔Любое действие выводит сумму денег

sum_money = 0
count = 0

while True:
    print(count)
    print("Введите команду: 1 - если хотите пополнить счет, 2 - если хотите снять, 3 - выход.")
    action = int(input())
    if action == 1:
        print(f"Сумма пополнения должна быть кратна 50$ \nДоступный баланс {sum_money}")
        deposit = int(input("Введите сумму пополнения: "))
        if deposit % 50 == 0:
            sum_money = deposit + sum_money
            print(f'Баланс пополнен! на балансе {sum_money}')
            if sum_money > 5000000:
                sum_money = (sum_money * 10) / 100
                print(f'С вас вычли налог на богатство) баланс стал {sum_money}')
            count += 1
            if count % 3 == 0:
                sum_money = (sum_money * 3) / 100
                print(f"За операции была вычтена коммиссия в размере 3%. Ваш баланс состовляет {sum_money} ")
            else:
                print(f'Количество операций {count}')
        else:
            print("Сумма пополнения должна быть кратной 50!")



    elif action == 2:
        print(f"Сумма снятия должна быть кратна 50$ \nДоступный баланс {sum_money}")
        deposit = int(input("Введите сумму снятия: "))
        if deposit % 50 == 0:
            percent = (deposit * 1.5) / 100
            if percent < 30:
                deposit = deposit + 30
                if sum_money < deposit:
                    print("Минимальная комиссия составляет 30$")
                    print(f"Вы не можете снять {deposit - 30} т.к будет вычтена комиссия в размере 30$")
                    continue
                else:
                    sum_money = sum_money - deposit
                    print(f'Вы сняли {deposit - 30}! остаток на балансе {sum_money}')
                    print(f'Процент за снятие составил 30$')
            elif percent > 600:
                deposit = deposit + 600
                if sum_money < deposit:
                    print("Максимальная комиссия составляет 600$")
                    print(f"Вы не можете снять {deposit-600} т.к будет вычтена комиссия в размере 600$")
                    continue
                else:
                    sum_money = sum_money - deposit
                    print(f'Вы сняли {deposit - percent}! остаток на балансе {sum_money}')
                    print(f'Процент за снятие составил 600$')

            else:
                deposit = deposit + percent
                if sum_money < deposit:
                    print(f"Вы не можете снять {deposit-percent} т.к будет вычтена комиссия в размере {percent}")
                    continue

                else:
                    sum_money = sum_money - deposit
                    print(f'Вы сняли {deposit - percent}! остаток на балансе {sum_money}')
                    print(f'Процент за снятие составил {percent}')

            print(f'Баланс снизился на  {deposit}! остаток на балансе {sum_money}')
            count += 1
            if count % 3 == 0:
                sum_money = (sum_money * 3) / 100
                print(f"За операции была вычтена коммиссия в размере 3%. Ваш баланс состовляет {sum_money} ")
            else:
                print(f'Количество операций {count}')
        else:
            print("Сумма пополнения должна быть кратной 50!")


    elif action == 3:
        print(f'Спасибо что воспользовались нашим банкоматом! Ваш баланс {sum_money}')
        break

    else:
        print("НУЖНО ВЫБРАТЬ ПРАВИЛЬНУЮ КОМАНДУ: 1 - пополнить, 2 - снять или 3 - выйти. ")
        print(f'Доступный баланс {sum_money}')
