import pickle

TODO_DB_PATH = "test.obj"

class Todo():
    def __init__(self, date, content): 
        self.date = date
        self.content = content

def loadDB():
    try:
        with open(TODO_DB_PATH, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}
    except EOFError:
        return {}

def saveDB(dictDB):
    with open(TODO_DB_PATH, "wb") as f:
        pickle.dump(dictDB, f)

def deleteDB(dictDB, key):
    if key in dictDB:
        del dictDB[key]

def updateTodo(db, key):
    if key in db:
        print(db)
        print(db[key])

db = loadDB()
def makeTodo(db, todo):
    db.setdefault(date, []).append(todo.content)

date = input("날짜를 입력하세요: ")
content = input("할 일을 입력하세요: ")
todo = Todo(date, content)
makeTodo(db, todo)

saveDB(db)
print(loadDB())