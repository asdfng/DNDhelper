from windows import screen_states as screens
import curses

def main(stdscr):
    screen = screens.menu_screen
    while screen is not None:
        screen = screen(stdscr)

curses.wrapper(main)