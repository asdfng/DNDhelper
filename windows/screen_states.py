import curses

def menu_screen(stdscr):
    
    options = ['Load Game', 'New Game']

    current_option = 0

    while True:
        stdscr.clear()

        for i, option in enumerate(options):
            if i == current_option:
                stdscr.addstr(i, 0, option, curses.A_REVERSE)
            else:
                stdscr.addstr(i, 0, option)
        
        stdscr.refresh()
        key = stdscr.getch()

        # Check for arrow keys
        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(options) - 1:
            current_option += 1
        elif key == ord('\n'):  # Enter key
            if options[current_option] == 'Load Game':
                return load_game
            else:
                return new_game
            
def load_game(stdscr):
    stdscr.clear()
    stdscr.addstr("Loading Game...")
    stdscr.getch()
    return menu_screen

def new_game(stdscr):
    stdscr.clear()
    stdscr.addstr("New Game...")
    stdscr.getch()
    return menu_screen
