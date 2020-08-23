number1 = input('計算する数字1を入力してください:')
number2 = input('計算する数字2を入力してください:')
print('計算するモードを選択してください')
mode = input('1=足し算 2=引き算 3=掛け算 4=割り算:')
if int(mode) == 1:
    answer = int(number1) + int(number2)
    print(answer)
elif int(mode) == 2:
    answer = int(number1) - int(number2)
    print(answer)
elif int(mode) == 3:
    answer = int(number1) * int(number2)
    print(answer)
elif int(mode) == 4:
    answer = int(number1) / int(number2)
    print(answer)
input('エンターキーを押して終了します')