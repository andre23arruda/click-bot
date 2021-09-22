import json, pyautogui, time

def main():
    print('\n\n========= INÍCIO ========= \n\n')
    n_coordinates = int(input('Número de coordenadas que deseja salvar: '))

    data = {}

    for i in range(n_coordinates):
        count = i + 1
        print(f'\n\nCOORDENADA { count }')
        print('Posicione o cursor do mouse onde deseja salvar a coordenada. \nEspere 5 segundos...')
        time.sleep(5)
        current_position = pyautogui.position()
        data[f'coordinate_{ count }'] = {
            'x': current_position.x,
            'y': current_position.y
        }
        print(current_position)
        print(f'SALVO COORDENADA { count }')

    with open('./utils/coordinates.json', 'w') as fp:
        json.dump(data, fp)

    print('\n\n========= FIM ========= \n\n')


if __name__ == '__main__':
    main()
