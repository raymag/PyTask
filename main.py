from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import json
#Gerenciador de Tarefas
class PyTask(BoxLayout):
    def __init__(self, **kwargs):
        def showTasks(self):
            def reloadData(self):
                with open('data/database.json', 'w') as db:
                    json.dump(database, db)
            def delTask(Button):
                if Button.text in database:
                    database.remove(Button.text)
                taskPopupGrid.remove_widget(Button)
            def closeTaskPopup(Button):
                taskPopup.dismiss()
                reloadData(self)
            taskPopup = Popup()
            taskPopup.title = 'Tarefas'
            taskPopupGrid = GridLayout(cols=1)
            taskPopup.add_widget(taskPopupGrid)
            for task in database:
                taskPopupGrid.add_widget(Button(text=task, on_release=delTask, font_size='30sp', background_color=[10, 1, 1, 1]))
            taskPopupGrid.add_widget(Button(text='Fechar', on_release=closeTaskPopup, font_size='30sp', background_color=[1, 2, 2, 1]))
            taskPopup.open()
        def newTask(self):
            def add(Button):
                database.append(newTaskInput.text)
                newTaskPopup.dismiss()
            newTaskPopup = Popup()
            newTaskPopup.title = 'Nova Tarefa'
            newTaskPopupGrid = GridLayout(cols=1)
            newTaskPopup.add_widget(newTaskPopupGrid)

            newTaskInput = TextInput(font_size='100sp', foreground_color=[1, 0, 0, 1])
            newTaskAddButton = Button(text='Adicionar', on_release=add, font_size='30sp', background_color=[1, 2, 2, 1])
            newTaskPopupGrid.add_widget(newTaskInput)
            newTaskPopupGrid.add_widget(newTaskAddButton)
            newTaskPopup.open()
        def save(self):
            with open('data/database.json', 'w') as db:
                json.dump(database, db)
        def loadData(self):
            global database
            try:
                with open('data/database.json', 'r') as db:
                    database = json.load(db)
            except FileNotFoundError:
                with open('data/database.json', 'w') as db:
                    database = []
                    json.dump(database, db)
            print(database)
        PyTask.orientation = 'vertical'
        super(PyTask, self).__init__(**kwargs)

        showTasksButton = Button(text='Ver Tarefas', on_release=showTasks, font_size='30sp', background_color=[10, 1, 1, 1])
        newTaskButton = Button(text='Nova Tarefa', on_release=newTask, font_size='30sp', background_color=[1, 2, 2, 1])
        saveButton = Button(text='Salvar', on_release=save, font_size='30sp', background_color=[10, 1, 1, 1])

        self.add_widget(showTasksButton)
        self.add_widget(newTaskButton)
        self.add_widget(saveButton)

        loadData(self)
        print(database)


class App(App):
    def build(self):
        return PyTask()

App().run()
