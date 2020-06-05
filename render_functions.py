import tcod as libtcod

# Will draw our entites, map
def render_all(con, entities, game_map, screen_width, screen_height, colors):
    # Draw all entities in the list
    # Loops through each tile in the game map, and checks if it blocks sight or not.
    for y in range(game_map.height):
        for x in range(game_map.width):
            wall = game_map.tiles[x][y].block_sight
            # If it does, then it draws it as a wall, and if not, it draws a floor.
            if wall:
                libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'))
            else:
                libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'))
    
    for entity in entities:
        draw_entity(con, entity)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
    

def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)

# Draw entities to screen
def draw_entity(con, entity):
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

# clear all the entities after drawing them to the screen
def clear_entity(con, entity):
    # erase the character that represents this object
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)