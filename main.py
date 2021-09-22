from json import load
from utils.click_bot import click, get_delay_and_repeat
from utils.load_coordinates import load_coordinates

def main():
    print('\n\n========= INÍCIO ========= \n\n')

    coordinates = load_coordinates()
    delay, repeat = get_delay_and_repeat()

    for v in range(repeat):
        print(f'\nREPEAT { v + 1 }')

        for i, coordinate in enumerate(coordinates.values()):
            print(f'CLICK { i + 1 }')
            click(coordinate, delay)

    print('\n\n========= FIM ========= \n\n')

if __name__ == '__main__':
    main()