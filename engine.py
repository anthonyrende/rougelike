import tcod as libtcod

from entity import Entity
from input_handlers import handle_keys
from render_functions import clear_all, render_all
from map_objects.game_map import GameMap

def main():
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    # These colors will serve as our wall and ground outside the FOV
    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150)
    }

    #  Initializing player, NPC, etc imported from Entity class
    player = Entity(int(screen_height / 2), int(screen_width / 2), '@', libtcod.white)
    npc = Entity(int(screen_height / 2), int(screen_width /2 - 5), '@', libtcod.yellow)
    entities = [npc, player]

    # we’re telling libtcod which file and font to use
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    # creates the screen - width/height, title, fullscreen False
    libtcod.console_init_root(screen_width, screen_height, 'rougelike', False)

    con = libtcod.console_new(screen_width, screen_height)
    # Init GameMap
    game_map = GameMap(map_width, map_height)

    # these variables will hold our keyboard and mouse input
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        # captures new 'events' (user input). Updates the key and mouse variables with what the user inputs
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        # set the color for our ‘@’ symbol, 0 is the console we're drawing to
        # libtcod.console_set_default_foreground(0, libtcod.white)
        # 0 is the console we are printing to, x, y coords
        # libtcod.console_put_char(con, player.x, player.y, '@', libtcod.BKGND_NONE)

        render_all(con, entities,game_map, screen_width, screen_height, colors)

        # presents it to the screen
        libtcod.console_flush()
        # libtcod.console_put_char(con, player.x, player.y, ' ', libtcod.BKGND_NONE)
        # libtcod.console_put_char(0, player.x, player.y, ' ', libtcod.BKGND_NONE)
        clear_all(con, entities)

        # We’re capturing the return value of handle_keys in the variable action (which is a dict)
        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                # Entity class handles the actual movement
                player.move(dx, dy)
        # check if the key pressed was the Esc, exit
        if exit:
            return True
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()