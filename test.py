import pickle
import re

check1=re.compile('[1-9][_][1-9]')
check2=re.compile('[1-9][_][1-2]\d')
check3=re.compile('[1|3|5|7|8][_][3][0-1]')
check4=re.compile('[4|6|9|][_][3][0]')
check5=re.compile('[1][0-2][_][1-9]')
check6=re.compile('[1][0-2][_][1-2]\d')
check7=re.compile('[1][0|2][_][3][0-1]')
check8=re.compile('[1][1][_][3][0]')

TODO_DB_PATH = "test.obj"

#Todo 클래스 {"date" : ["content1", "content2"]} 구조
class Todo():
    def __init__(self, date, content): 
        self.date = date
        self.content = content

#test.obj 파일 열어서 반환하는 함수
#print(loadDB()) -> 파일 내용 전부 출력
def loadDB():
    try:
        with open(TODO_DB_PATH, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}
    except EOFError:
        return {}

#test.obj 파일에 기존 데이터 무시하고 덮어씌우는 함수
def saveDB(db):
    with open(TODO_DB_PATH, "wb") as f:
        pickle.dump(db, f)

def deleteDB(db, key):
    if key in db:
        del db[key]

def main():
    while True:
        print("1. 회원가입\t2. 로그인")
        userinput = input("어디로 이동할까요?: ")
        if (userinput == "1"):
            print("회원가입 진행")
        elif (userinput == "2"):
            print("로그인 진행")
            todoMain()
            break
        else:
            print("올바른 숫자를 입력해주세요!")

def todoMain():
    while True:
        print("1. 할 일 목록\t2. 할 일 추가\t3. 할 일 수정\t4. 할 일 삭제\t5. 종료")
        userinput = input("어디로 이동할까요?: ")
        if(userinput == "1"):
            print("할 일 목록 출력")
            print(loadDB())
        elif(userinput == "2"):
            print("할 일 추가")
            makeTodo()
        elif(userinput == "3"):
            print(list(loadDB().keys()))
            date = input("어느 날짜의 할 일을 선택하시겠습니까?: ")
            todoUpdate(date)
            break
        elif(userinput == "4"):
            print("할 일 삭제")
        elif(userinput == "5"):
            print("종료")
            break
        else:
            print("올바른 숫자를 입력해주세요!")


def addTodo(todo):
    db = loadDB()
    db.setdefault(todo.date,[]).append(todo.content)
    saveDB(db)

def makeTodo():
    while True:
        while True:
            date=input('날짜를 입력하세요. ex)2_27\n')
            if len(date) == 3:
                if check1.match(date) != None:
                    break
                else:
                    print('\n올바른 날짜를 입력하세요.\n')
            elif len(date) == 4:
                if check2.match(date) != None or check3.match(date) != None or check4.match(date) != None or check5.match(date) != None:
                    break
                else:
                    print('\n올바른 날짜를 입력하세요.\n')
            elif len(date) == 5:
                if check6.match(date) != None or check7.match(date) != None or check8.match(date) != None:
                    break
                else:
                    print('\n올바른 날짜를 입력하세요.\n')
            else:
                print('\n올바른 2날짜를 입력하세요.\n')

        content = input('할 일을 입력하세요.\n')
        todo = Todo(date,content)
        addTodo(todo)

        while True:
            more = input('할일을 더 등록하시겠습니까? y/n\n')
            if more == 'y' or more == 'n':
                break
            else:
                print('\n올바른 답변을 입력하세요.\n')
                continue
        if more == 'y':
            continue
        else:
            break
    
def todoUpdate(key):
    print(key)
    while True:
        print(loadDB()[key])
        idx = int(input("어느 항목을 수정하시겠습니까?: "))
        print(loadDB()[key][idx-1])
        todoMain()
        break

main()
