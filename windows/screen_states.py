import curses
import time

def menu_screen(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    options = ['Load Game', 'New Game', 'Exit']

    options_screens = {
        'Load Game' : load_game,
        'New Game' : new_game,
        'Exit' : close_helper
    }

    current_option = 0

    header_lines =[ 
        ":::::::::  ::::    ::: :::::::::  :::    ::: :::::::::: :::        :::::::::  :::::::::: :::::::::",
        ":+:    :+: :+:+:   :+: :+:    :+: :+:    :+: :+:        :+:        :+:    :+: :+:        :+:    :+:",
        "+:+    +:+ :+:+:+  +:+ +:+    +:+ +:+    +:+ +:+        +:+        +:+    +:+ +:+        +:+    +:+",
        "+#+    +:+ +#+ +:+ +#+ +#+    +:+ +#++:++#++ +#++:++#   +#+        +#++:++#+  +#++:++#   +#++:++#:", 
        "+#+    +#+ +#+  +#+#+# +#+    +#+ +#+    +#+ +#+        +#+        +#+        +#+        +#+    +#+",
        "#+#    #+# #+#   #+#+# #+#    #+# #+#    #+# #+#        #+#        #+#        #+#        #+#    #+#",
        "#########  ###    #### #########  ###    ### ########## ########## ###        ########## ###    ###",
        "                -----------------------------------------------------------------                  "
    ]

    while True:
        stdscr.clear()

        height, width = stdscr.getmaxyx()
        center_x = width//2
        current_y = 0

        for i, header_line in enumerate(header_lines):
            stdscr.addstr(0 + i, center_x - len(header_line) // 2, header_line,\
                        curses.color_pair(1))
            current_y += 1

        for i, option in enumerate(options):

            pos_y = current_y + i
            pos_x = center_x - len(option)//2

            if i == current_option:
                stdscr.addstr(pos_y, pos_x, option, curses.A_REVERSE)
            else:
                stdscr.addstr(pos_y, pos_x, option)
        
        stdscr.refresh()
        key = stdscr.getch()

        # Check for arrow keys
        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(options) - 1:
            current_option += 1
        elif key == ord('\n'):  # Enter key
            selected_option = options[current_option]
            return options_screens[selected_option]
            
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

def close_helper(stdscr):
    stdscr.clear()

    height, width = stdscr.getmaxyx()
    center_x = width//2

    end_credits =[
        "                                       Thanks for trying:                                         ",
        ":::::::::  ::::    ::: :::::::::  :::    ::: :::::::::: :::        :::::::::  :::::::::: :::::::::",
        ":+:    :+: :+:+:   :+: :+:    :+: :+:    :+: :+:        :+:        :+:    :+: :+:        :+:    :+:",
        "+:+    +:+ :+:+:+  +:+ +:+    +:+ +:+    +:+ +:+        +:+        +:+    +:+ +:+        +:+    +:+",
        "+#+    +:+ +#+ +:+ +#+ +#+    +:+ +#++:++#++ +#++:++#   +#+        +#++:++#+  +#++:++#   +#++:++#:", 
        "+#+    +#+ +#+  +#+#+# +#+    +#+ +#+    +#+ +#+        +#+        +#+        +#+        +#+    +#+",
        "#+#    #+# #+#   #+#+# #+#    #+# #+#    #+# #+#        #+#        #+#        #+#        #+#    #+#",
        "#########  ###    #### #########  ###    ### ########## ########## ###        ########## ###    ###",
        "                -----------------------------------------------------------------                  ",
        "                                    Feedback is appreciated!                                       ",
        "                                                                                                   ",
        "                                              v00                                                  ",
        "                                     Made by: Nicholas Gregg                                       "
    ]

    for i, end_line in enumerate(end_credits):
        stdscr.addstr(0 + i, center_x - len(end_line) // 2, end_line,\
                      curses.color_pair(1))

    stdscr.refresh()
    time.sleep(3)
    quit()
