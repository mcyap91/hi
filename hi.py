height=input('请输入身高（cm）： ')
weight=input('请输入体重（kg) ： ')
height = int (height)
weight = int (weight)
height = height / 100
bmi = weight / height / height
if bmi <= 18.5:
	print('你的BMI值为', bmi, '属体重过轻')
elif bmi >= 18.5 and bmi < 24:
    print('你的BMI值为', bmi, '属正常范围')
elif bmi >= 24 and bmi < 27:
	print('你的BMI值为', bmi, '稳重')
elif bmi >= 27 and bmi < 30:
	print('你的BMI值为', bmi, '轻度肥胖')
elif bmi >=30 and bmi <35:
	print('你的BMI值为', bmi, '中度肥胖')
else:
	print('你的bmi值为', bmi, '重度肥胖')
