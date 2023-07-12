from dataclasses import dataclass
import csv
import random


@dataclass
class Prompt:
    prompt: str
    answer: float
    source: str = None

class ImportCalories:
    calories = None
    def ListOfCaloriesPrompts(self) -> list[Prompt]:
        caloriesPrompts = []
        with open('calories.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                caloriesPrompts.append(Prompt(row[1], row[3]))
        caloriesPrompts.pop(0)
        self.calories = caloriesPrompts
        return self.calories
    
    def Prompts20 (self) -> list[Prompt]:
        if self.calories is None : self.ListOfCaloriesPrompts()
        prompts = []
        for i in range(20):
            prompts.append(self.calories[random.randint(0, len(self.calories))])
        return prompts
