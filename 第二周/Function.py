from dataclasses import replace


def AddStack(S : list[str],item):
    S.append(item)

def isdigit(num:str) ->bool:
    try:
        float(num)
        return True
    except ValueError:
        return False

def PosFunc(Pos : list[str],Func : list[str]):
    Wait = []
    while Func:
        if  isdigit(Func[0]):
            Pos.append(Func.pop(0))
        elif Func[0] == '(':
            Wait.append(Func.pop(0))
        elif Func[0] == ')':
            while Wait[-1] != '(':
                Pos.append(Wait.pop(-1))
            Wait.pop(-1)
            Func.pop(0)
        elif Func[0] == '*' or Func[0] =='/':
            while Wait and (Wait[-1] != '+' and Wait[-1] != '-' and Wait[-1] != '('):
                Pos.append(Wait.pop(-1))
            Wait.append(Func.pop(0))
        elif Func[0] == '+' or Func[0] =='-':
            while Wait and (Wait[-1] != '('):
                Pos.append(Wait.pop(-1))
            Wait.append(Func.pop(0))
    while Wait:
        Pos.append(Wait.pop(-1))
    return Pos


def Check(Func: list[str]) -> bool:
    yunsuan = '+-*/'
    YS = list(yunsuan)
    flag = 0
    for i,item in enumerate(Func):
        if i+1<len(Func):
            if item in YS:
                if Func[i+1] in YS or Func[i+1] == '.':  #运算符紧跟运算符或小数点
                    flag = 1
        if (i == len(Func)-1 or i == 0)and (item in YS or item == '.'):   #首尾是运算符或小数点
            flag = 1
        if (i == len(Func)-1 and item == '(') or (i == 0 and item == ')'): #尾是(或首是)
            flag = 1
        if i + 1 < len(Func):
            if item == '(' and (Func[i+1] in YS or Func[i+1] == ')' or Func[i+1] == '.'):  #(紧跟.*)/+-
                flag = 1
            if item in YS and Func[i+1] == ')': #运算符紧跟)
                flag = 1
            if item == '.' and Func[i+1] == ')': #.紧跟)
                flag = 1
            if item == ')' and Func[i+1] == '(': # )紧跟(
                flag = 1
            if isdigit(num) and Func[i+1] == '(': #数字后紧跟(
                flag = 1
    if '(' in Func and ')' not in Func:
        flag = 1
    if ')' in Func and '(' not in Func: #只有半边括号
        flag = 1
    if flag == 1:
        return False
    else:
        return True


def Scanf(Func : list[str]):
    while True:
        flag = 0
        function = input('Plz input Func:')
        function = function.replace(' ','') #去掉空格
        Func = list(function)
        for i,item in enumerate(Func):
            if (item <'0' or item > '9') and item != '.' and item != '+' and item != '-' and item != '*' and item != '/' and item != '(' and item != ')' and item != '（' and item != '）':
                flag = 1  #判断有没有非式子可能用到的字符
                break
        if flag == 1 or Check(Func) == False:
            print('Plz check input!')  #再输入一遍
        else:
            break
    for i,item in enumerate(Func):  #将中文括号转英文括号
        if item == '（':
            Func[i] = '('
        if item == '）':
            Func[i] = ')'
        if i+1<len(Func) and item >= '0' and item <= '9':  #合并多位数或小数
            if Func[i + 1] >= '0' and Func[i + 1] <= '9':
                Func[i] += Func[i+1]
                Func.pop(i+1)
            elif Func[i + 1] == '.':
                Func[i] += (Func[i + 1] + Func[i + 2])
                Func.pop(i + 1)
                Func.pop(i + 1)
    return Func


def Calc(Pos : list[str]):
    Sum = '0'
    a = 0
    b = 0
    Wait = []
    while Pos:
        if isdigit(Pos[0]):
            Wait.append(Pos.pop(0))
        elif Pos[0] == '+':
            Pos.pop(0)
            b = float(Wait.pop(-1))
            a = float(Wait.pop(-1))
            Wait.append(str(a+b))
        elif Pos[0] == '-':
            Pos.pop(0)
            b = float(Wait.pop(-1))
            a = float(Wait.pop(-1))
            Wait.append(str(a-b))
        elif Pos[0] == '*':
            Pos.pop(0)
            b = float(Wait.pop(-1))
            a = float(Wait.pop(-1))
            Wait.append(str(a*b))
        elif Pos[0] == '/':
            Pos.pop(0)
            b = float(Wait.pop(-1))
            a = float(Wait.pop(-1))
            Wait.append(str(a/b))
    sum = Wait.pop()
    return sum



Pos = []
Func = []
Func = Scanf(Func)
Pos = PosFunc(Pos,Func)
print(Pos)
sum = Calc(Pos)
print(sum)




