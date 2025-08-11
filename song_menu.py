import pygame
import os

def song_selection_menu(song_folder="songs"):
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    font = pygame.font.SysFont("Arial", 32, bold=True)
    songs = [f for f in os.listdir(song_folder) if f.lower().endswith('.mp3')]
    if not songs:
        raise Exception("No .mp3 files found in the 'songs/' directory.")
    selected = 0
    running = True
    while running:
        screen.fill((30, 30, 30))
        title = font.render("Select a Song", True, (0,255,236))
        screen.blit(title, (180, 40))
        for i, song in enumerate(songs):
            color = (255,255,0) if i == selected else (200,200,200)
            surf = font.render(song, True, color)
            screen.blit(surf, (100, 120 + i*40))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(songs)
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(songs)
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    running = False
    pygame.display.quit()
    return os.path.join(song_folder, songs[selected])
