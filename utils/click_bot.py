import pyautogui, time

def get_delay_and_repeat():
    '''Pergunta ao usuário número de repetições e intervalo'''
    delay = float(input('Intervalo entre as ações (em segudos) ? '))
    repeat = int(input('Quantas vezes deseja repetir o conjunto de ações? '))
    return delay, repeat


def click(coordinate: dict, delay: int):
    '''Clica em um elemento na tela de acordo com a coordenada'''
    pyautogui.moveTo(**coordinate,duration=1)
    pyautogui.click(**coordinate)
    time.sleep(delay)
