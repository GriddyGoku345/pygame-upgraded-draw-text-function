# Pygame game template

import pygame
import sys
import config  # Import the config module

def init_game():
    pygame.init()
    
    pygame.font.init()  # Initialize fonts here

    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


def draw_text():
    pass

def main():

    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock object

    font_name = "FreeMono.ttf"
    font_color1 = config.RED  # Use a color from the config
    font_color2 = config.MIDNIGHT_PURPLE
    font_color3 = config.DARKORANGE
    font_size_normal = 36
    font_size_bold_italic = 30
    font_size_custom = 48

    # Using a True Type Font (.ttf)
    custom_font_name = 'Jacquard12-Regular.ttf'

    # Define x,y coordinate pairs for top left of text rectangle (stamp)
    text_position_1 = [50, 50]
    text_position_2 = [225, 135]
    text_position_3 = [220, 370]


    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)  # Use color from config

        draw_text(screen, "Hello World!", font_size_normal, font_name, font_color1, text_position_1, italic=True)
        draw_text(screen, "Text which is bold and italic.", font_size_bold_italic, font_name, font_color2, text_position_2, italic=True, bold=True)



        pygame.display.flip()

        # Limit frame rate to certain number of frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
