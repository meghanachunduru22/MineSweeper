def main():
    from random import randint
    import pygame
    width = 9
    height = 9
    num_of_bombs = 14
    size = 495
    rows = 9
    play = True
    grid_array = [["-" for i in range(width)] for j in range(height)]
    rightclicked = []
    user_array = [["-" for i in range(width)] for j in range(height)]

    n = 0
    while(n <= num_of_bombs):
        x = randint(0, width-1)
        y = randint(0, height-1)
        grid_array[x][y] = "*"
        n += 1

    def not_out_of_range(a, b):
        if a < 0 or b < 0 or a >= width or b >= height:
            return False
        else:
            return True

    for x in range(width):
        for y in range(height):
            if grid_array[x][y] == "-":
                value = 0
                if not_out_of_range(x-1, y-1):
                    if grid_array[x-1][y-1] == "*":
                        value += 1
                if not_out_of_range(x-1, y):
                    if grid_array[x-1][y] == "*":
                        value += 1
                if not_out_of_range(x-1, y+1):
                    if grid_array[x-1][y+1] == "*":
                        value += 1
                if not_out_of_range(x, y-1):
                    if grid_array[x][y-1] == "*":
                        value += 1
                if not_out_of_range(x, y):
                    if grid_array[x][y] == "*":
                        value += 1
                if not_out_of_range(x, y+1):
                    if grid_array[x][y+1] == "*":
                        value += 1
                if not_out_of_range(x+1, y-1):
                    if grid_array[x+1][y-1] == "*":
                        value += 1
                if not_out_of_range(x+1, y):
                    if grid_array[x+1][y] == "*":
                        value += 1
                if not_out_of_range(x+1, y+1):
                    if grid_array[x+1][y+1] == "*":
                        value += 1
                grid_array[x][y] = value

    window = pygame.display.set_mode((size, size))

    def grid(window, size, rows):
        dist_btw_rows = size // rows
        x = 0
        y = 0
        for l in range(rows):
            x += dist_btw_rows
            y += dist_btw_rows
            pygame.draw.line(window, (255, 255, 255), (x, 0), (x, size))
            pygame.draw.line(window, (255, 255, 255), (0, y), (size, y))
    for r in grid_array:
        for c in r:
            print(c, end=" ")
        print()
    print(" ")

    window.fill((0, 0, 0))
    while play:
        grid(window, size, rows)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                textcol = (255, 255, 255)
                pos = pygame.mouse.get_pos()
                row = pos[0] // (55)
                column = pos[1] // (55)
                a = (column*55) + 10
                b = (row*55) + 10
                pygame.font.init()
                default_font = pygame.font.get_default_font()
                font_renderer = pygame.font.Font(default_font, 32)
                user_array[column][row] = grid_array[column][row]
                if event.button == 1:
                    if (column, row) in rightclicked:
                        continue
                    strn = str(grid_array[column][row])
                if event.button == 3:
                    strn = "#"
                    if (column, row) in rightclicked:
                        textcol = (0, 0, 0)
                        rightclicked.remove((column, row))
                    else:
                        rightclicked.append((column, row))

                if strn == "*":
                    white = (255, 255, 255)
                    green = (0, 255, 0)
                    blue = (0, 0, 128)
                    X = 400
                    Y = 400
                    display_surface = pygame.display.set_mode((X, Y))
                    pygame.display.set_caption('Show Text')
                    font = pygame.font.Font('freesansbold.ttf', 32)
                    text = font.render('YOU LOST', True, blue, white)
                    textRect = text.get_rect()
                    textRect.center = (X // 2, Y // 3)
                    replaytext = font.render("Replay", True, green, blue)
                    replaytextRect = replaytext.get_rect()
                    replaytextRect.center = (X//2, 2*Y//3)
                    while True:
                        display_surface.fill(white)
                        display_surface.blit(text, textRect)
                        display_surface.blit(replaytext, replaytextRect)
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                p, q = pygame.mouse.get_pos()
                                if p in range(146, 255) and q in range(252, 280):
                                    main()
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            pygame.display.update()
                    play = False

                label = font_renderer.render(strn, 1, textcol)
                window.blit(label, (b, a))

                if user_array == grid_array:
                    white = (255, 255, 255)
                    green = (0, 255, 0)
                    blue = (0, 0, 128)
                    X = 400
                    Y = 400
                    display_surface = pygame.display.set_mode((X, Y))
                    pygame.display.set_caption('Show Text')
                    font = pygame.font.Font('freesansbold.ttf', 32)
                    text = font.render('YOU WON', True, green, blue)
                    textRect = text.get_rect()
                    textRect.center = (X // 2, Y // 3)
                    replaytext = font.render("Replay", True, green, blue)
                    replaytextRect = replaytext.get_rect()
                    replaytextRect.center = (X//2, 2*Y//3)
                    while True:
                        display_surface.fill(white)
                        display_surface.blit(text, textRect)
                        display_surface.blit(replaytext, replaytextRect)
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                p, q = pygame.mouse.get_pos()
                                if p in range(146, 255) and q in range(252, 280):
                                    main()
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            pygame.display.update()
                    play = False

                pygame.display.update()
            if event.type == pygame.QUIT:
                play = False

        pygame.display.update()


main()
