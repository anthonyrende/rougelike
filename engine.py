import tcod as libtcod

from input_handlers import handle_keys

def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # we’re telling libtcod which file and font to use
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    # creates the screen - width/height, title, fullscreen False
    libtcod.console_init_root(screen_width, screen_height, 'rougelike', False)
    # these variables will hold our keyboard and mouse input
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        # captures new 'events' (user input). Updates the key and mouse variables with what the user inputs
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        # set the color for our ‘@’ symbol, 0 is the console we're drawing to
        libtcod.console_set_default_foreground(0, libtcod.white)
        # 0 is the console we are printing to, x, y coords
        libtcod.console_put_char(0, player_x, player_y, '@', libtcod.BKGND_NONE)
        # presents it to the screen
        libtcod.console_flush()
        # We’re capturing the return value of handle_keys in the variable action (which is a dict)
        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player_x += dx
            player_y += dy
        # check if the key pressed was the Esc, exit
        if exit:
            return True
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()