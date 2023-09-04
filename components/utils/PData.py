from dataclasses import dataclass
import csv
import random

PROMPT_STRING = 'The amount of Calories in '

@dataclass
class Prompt:
    prompt: str
    answer: int
    unit : str = None
    source: str = None



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
                    questions.append(Prompt(question, int(answer), source=source))
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
    
    
    def GenerateBalansedQuestions(self, number:int) ->list[Prompt]:
        
        jumpDistance = 7
        promptsToTakeFrom = self.SortedList(self.questions.copy())
        
        def GoCrazyChance(q_num):
            if q_num > 20:
                return False
            elif q_num > 10:
                return random.randint(1, 10) == 1
            elif q_num > 5:
                return random.randint(1, 5) == 1
            else: 
                return True

        prompts = []
        index = random.randint(0, len(self.questions)-1)        
        for i in range(50):

            if GoCrazyChance(i):
                index = random.randint(0, len(promptsToTakeFrom)-1)
                # print('-')
            else:
                distance = random.randint(-jumpDistance, jumpDistance)
                if (index + distance) < 0 or (index + distance) > len(promptsToTakeFrom)-1:
                    distance = -distance
                index += distance
            #make sure index in range when question starts to run out
            if index < 0:
                index = 0
            elif index > len(promptsToTakeFrom)-1:
                index = len(promptsToTakeFrom)-1
            
            # print('index', index, 'len', len(promptsToTakeFrom))
            takenPrompt = promptsToTakeFrom.pop(index)
            prompts.append(takenPrompt)
        return prompts
        # return prompts


    
    def __DrawAndTakeMin(self, prompts, number: int):
        prompt = prompts[random.randint(0, len(prompts))-1]
        for i in range(number -1):
            r_prompt = prompts[random.randint(0, len(prompts)-1)]
            if r_prompt.answer < prompt.answer:
                prompt = r_prompt
        return prompt
    
    def SortedList(self, listPrompts):
        # sort the list of Prompts based on prompt.answer
        return sorted(listPrompts, key=lambda x: x.answer)
    



