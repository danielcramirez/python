import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mi Primer Juego - Pong")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Reloj para controlar FPS
clock = pygame.time.Clock()
FPS = 60

# Paletas
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
player_paddle = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ai_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Pelota
BALL_SIZE = 15
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
ball_dx = 5 * random.choice((1, -1))
ball_dy = 5 * random.choice((1, -1))

# Puntuación
player_score = 0
ai_score = 0
font = pygame.font.Font(None, 74)

# Función para mover la pelota
def move_ball():
    global ball_dx, ball_dy, player_score, ai_score
    
    ball.x += ball_dx
    ball.y += ball_dy
    
    # Colisión con bordes superior/inferior
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1
    
    # Colisión con paletas
    if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
        ball_dx *= -1
    
    # Puntos
    if ball.left <= 0:
        ai_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        player_score += 1
        reset_ball()

# Función para reiniciar la pelota
def reset_ball():
    ball.center = (WIDTH//2, HEIGHT//2)
    global ball_dx, ball_dy
    ball_dx = 5 * random.choice((1, -1))
    ball_dy = 5 * random.choice((1, -1))

# Función para dibujar todo
def draw():
    screen.fill(BLACK)
    
    # Paletas
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, ai_paddle)
    
    # Pelota
    pygame.draw.ellipse(screen, WHITE, ball)
    
    # Línea central
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))
    
    # Puntuación
    player_text = font.render(str(player_score), True, WHITE)
    ai_text = font.render(str(ai_score), True, WHITE)
    screen.blit(player_text, (WIDTH//4, 20))
    screen.blit(ai_text, (3*WIDTH//4, 20))

# Bucle principal
while True:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Controles del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= 7
    if keys[pygame.K_s] and player_paddle.bottom < HEIGHT:
        player_paddle.y += 7
    
    # IA simple
    if ai_paddle.centery < ball.centery and ai_paddle.bottom < HEIGHT:
        ai_paddle.y += 5
    if ai_paddle.centery > ball.centery and ai_paddle.top > 0:
        ai_paddle.y -= 5
    
    # Lógica del juego
    move_ball()
    
    # Dibujar
    draw()
    
    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(FPS)