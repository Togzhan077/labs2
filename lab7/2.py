import pygame
import sys
import os

pygame.init()

# Терезе жасау
window = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Музыка плеер")

# Суреттерді жүктеу
try:
    Play = pygame.image.load('c:/Users/User/Downloads/play (1).jpg')
    Stop = pygame.image.load('c:/Users/User/Downloads/stop.jpg')
    Next = pygame.image.load('c:/Users/User/Downloads/next.jpg')
    Last = pygame.image.load('c:/Users/User/Downloads/past.jpg')
except pygame.error as e:
    print("Суретті жүктеу қатесі:", e)
    sys.exit()

# Батырма беті
Button = pygame.Surface((173, 173))

# Әндер тізімі
_songs = [
    'c:/Users/User/Downloads/its safe now.mp3',
    'c:/Users/User/Downloads/LABS_LAB_7_music_Hotline_Miami_2_Wrong_Number_Soundtrack_Acid_Spit.mp3'
]

# Музыка біткен оқиға
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

# Музыканы қосу
if os.path.exists(_songs[0]):
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
else:
    print(f"Файл табылмады: {_songs[0]}")

# Келесі ән
def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    if os.path.exists(_songs[0]):
        pygame.mixer.music.load(_songs[0])
        pygame.mixer.music.play()
    else:
        print(f"Файл табылмады: {_songs[0]}")

# Алдыңғы ән
def play_last_song():
    global _songs
    _songs = _songs[-1:] + _songs[:-1]
    if os.path.exists(_songs[0]):
        pygame.mixer.music.load(_songs[0])
        pygame.mixer.music.play()
    else:
        print(f"Файл табылмады: {_songs[0]}")

# Ойнау күйі
play = True

# Шрифт
font = pygame.font.SysFont(None, 28)

# Негізгі цикл
while True:
    pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 300 < pos[0] < 450 and 50 < pos[1] < 200:
                play = not play
                if play:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
            elif 500 < pos[0] < 650 and 50 < pos[1] < 200:
                play_next_song()
                play = True
            elif 100 < pos[0] < 250 and 50 < pos[1] < 200:
                play_last_song()
                play = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = not play
                if play:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
            elif event.key == pygame.K_RIGHT:
                play_next_song()
                play = True
            elif event.key == pygame.K_LEFT:
                play_last_song()
                play = True
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                play = False

        if event.type == SONG_END:
            play_next_song()

    # Батырманы жаңарту
    Button.fill((255, 255, 255))
    if play:
        Button.blit(Stop, (0, 0))
    else:
        Button.blit(Play, (0, 0))

    # Экранды толтыру
    window.fill((255, 255, 255))
    window.blit(Last, (100, 50))
    window.blit(Next, (500, 50))
    window.blit(Button, (300, 50))

    # Қазіргі әннің атын шығару
    song_name = _songs[0].split("/")[-1]
    text_surface = font.render(f"Ойнап жатыр: {song_name}", True, (0, 0, 0))
    window.blit(text_surface, (10, 10))

    pygame.display.flip()
