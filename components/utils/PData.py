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
                caloriesPrompts.append(Prompt(row[1], row[3], source="calories.csv datatable"))
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
