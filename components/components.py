class Button():
    pass

class Text():
    pass

class PromptPanel():
    width: int
    height: int
    pos_x: int
    pos_y: int
    prompt: Text = 'Here goes the prompt'
    answer: Text = 'Here goes the answer'
    source: Text = 'Here goes the source'
    btn_higher : Button = None
    btn_lower : Button = None
