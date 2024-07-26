from pygame import *

init()
PADDLE1_IMG = "кошка.png"
PADDLE2_IMG = "бобик.png"
BALL_IMG = "мяч.png"
BACKGROUND_IMG = "пляж.jpg"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BALL_SIZE = 30
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 100
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
PADDLE_SPEED = 5
GRAY = (34, 34, 34)
WHITE = (255, 255, 255)
window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Ping-pong")
background = image.load(BACKGROUND_IMG)
def reset_game():
    global paddle1_x, paddle1_y, paddle2_x, paddle2_y, ball_x, ball_y, BALL_SPEED_X, BALL_SPEED_Y, finish, winner_text
    paddle1_x = 10
    paddle1_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
    paddle2_x = WINDOW_WIDTH - 20 - PADDLE_WIDTH
    paddle2_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
    ball_x = WINDOW_WIDTH // 2 - BALL_SIZE // 2
    ball_y = WINDOW_HEIGHT // 2 - BALL_SIZE // 2
    BALL_SPEED_X = 5
    BALL_SPEED_Y = 5
    finish = False
    winner_text = ""
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_r:
                reset_game()

    if not finish:
        # Обработка движения и коллизий
        ...

    # Отображение элементов на экране
    window.blit(background, (0, 0))
    window.blit(ball, (ball_x, ball_y))
    window.blit(cat, (paddle1_x, paddle1_y))
    window.blit(bobik, (paddle2_x, paddle2_y))

    if finish:
        # Отображение текста победителя
        ...

    display.update()
    clock.tick(FPS)
