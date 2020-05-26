import tcod as libtcod

def main():
    screen_width = 80
    screen_height = 50

    # we’re telling libtcod which file and font to use
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    # creates the screen - width/height, title, fullscreen False
    libtcod.console_init_root(screen_width, screen_height, 'rougelike', False)

    while not libtcod.console_is_window_closed():
        # set the color for our ‘@’ symbol, 0 is the console we're drawing to
        libtcod.console_set_default_foreground(0, libtcod.white)
        # 0 is the console we are printing to, 1, 1 is x, y, coords
        libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE)
        # presents it to the screen
        libtcod.console_flush()
        # gets any keyboard input to the program, which we store in the key variable
        key = libtcod.console_check_for_keypress()
        # check if the key pressed was the Esc, exit
        if key.vk == libtcod.KEY_ESCAPE:
            return True


if __name__ == '__main__':
    main()