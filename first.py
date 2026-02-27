import re

check1=re.compile('[1-9][_][1-9]')
check2=re.compile('[1-9][_][1-2]\d')
check3=re.compile('[1|3|5|7|8][_][3][0-1]')
check4=re.compile('[4|6|9|][_][3][0]')
check5=re.compile('[1][0-2][_][1-9]')
check6=re.compile('[1][0-2][_][1-2]\d')
check7=re.compile('[1][0|2][_][3][0-1]')
check8=re.compile('[1][1][_][3][0]')

db={}

class Todo():
    def __init__(self,date,content):
        self.date=date
        self.content=content

def submit():
    def makeTodo(db,todo):
        db.setdefault(date,[]).append(todo.content)

    while True:
        while True:
            date=input('날짜를 입력하세요. ex)2_27\n')
            if len(date)==3:
                if check1.match(date)!=None:
                    break
                else:
                    print('\n올바른 날짜를 입력하세요.\n')
            elif len(date)==4:
                if check2.match(date)!=None or check3.match(date)!=None or check4.match(date)!=None or check5.match(date)!=None:
                    break
                else:
                    print('\n올바른 날짜를 입력하세요.\n')
            elif len(date)==5:
                if check6.match(date)!=None or check7.match(date)!=None or check8.match(date)!=None:
                    break
                else:
                    print('\n올바른 날짜를 입력하세요.\n')
            else:
                print('\n올바른 2날짜를 입력하세요.\n')

        content=input('할 일을 입력하세요.\n')
        todo=Todo(date,content)
        makeTodo(db,todo)

        while True:
            more=input('할일을 더 등록하시겠습니까? y/n\n')
            if more=='y' or more=='n':
                break
            else:
                print('\n올바른 답변을 입력하세요.\n')
                continue
        if more=='y':
            continue
        else:
            break

    print(db)
    
submit()