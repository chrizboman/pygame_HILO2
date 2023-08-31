from dataclasses import dataclass
import csv
import random

PROMPT_STRING = 'The amount of Calories in '

@dataclass
class Prompt:
    prompt: str
    answer: float
    unit : str = None
    source: str = None


class ImportCalories:
    calories = None
    def ListOfCaloriesPrompts(self) -> list[Prompt]:
        caloriesPrompts = []
        with open('calories.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                answer = row[3].split(' ')[0]
                caloriesPrompts.append(Prompt(PROMPT_STRING + str(row[1]) + ' (' + str(row[2]) +')', answer=answer, source="calories.csv datatable"))
        caloriesPrompts.pop(0)
        self.calories = caloriesPrompts
        return self.calories
    
    def Prompts20 (self) -> list[Prompt]:
        if self.calories is None : self.ListOfCaloriesPrompts()
        prompts = []
        for i in range(20):
            prompts.append(self.calories[random.randint(0, len(self.calories))])
        return prompts
    
    def PromptsOne(self) -> Prompt:
        if self.calories is None : self.ListOfCaloriesPrompts()
        return self.calories[random.randint(0, len(self.calories))]



path = 'data/frågor.csv'

class ImportAutolivQuestions():
    questions = None

    def __init__(self) -> None:
        with open(path, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';', )
            questions = []
            for row in csv_reader:
                question, answer, source = row[0], row[1], row[2]
                if source != "" and question != "" and answer != "":
                    questions.append(Prompt(question, answer, source=source))
            self.questions = questions
        print(f'Imported {len(self.questions)} questions from {path}')
    
    def RandomQuestions(self, number : int) -> list[Prompt]:
        if self.questions is None : self.__init__()
        prompts = []
        questions_copy = self.questions.copy()
        for i in range(number):
            randomint = random.randint(0, len(questions_copy) -1)
            # print('popping', randomint, 'from', len(questions_copy)-1)
            prompts.append(questions_copy.pop(randomint))
        return prompts