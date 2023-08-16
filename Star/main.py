import pygame
import math

# Inicialização do pygame
pygame.init()

# Configurações da tela
width, height = 300, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Estrela de Cinco Pontos")

# Definindo o centro da estrela
centro_x, centro_y = width // 2, height // 2

# Calculando o raio externo da estrela (ajuste conforme necessário)
raio_externo = 80

# Calculando e armazenando as coordenadas dos pontos externos
pontos_externos = []
for i in range(5):
    angulo = math.radians(18 + i * 72)  # Convertendo para radianos e ajustando o ângulo
    x = centro_x + raio_externo * math.cos(angulo)
    y = centro_y - raio_externo * math.sin(angulo)
    pontos_externos.append((int(x), int(y)))

# Calculando o raio interno da estrela (ajuste conforme necessário)
raio_interno = raio_externo * math.sin(math.radians(18)) / math.sin(math.radians(126))

# Calculando e armazenando as coordenadas dos pontos internos
pontos_internos = []
for i in range(5):
    angulo = math.radians(54 + i * 72)  # Convertendo para radianos e ajustando o ângulo
    x = centro_x + raio_interno * math.cos(angulo)
    y = centro_y - raio_interno * math.sin(angulo)
    pontos_internos.append((int(x), int(y)))

# Combinando os pontos externos e internos para formar a estrela
pontos_estrela = []
for ponto_ext, ponto_int in zip(pontos_externos, pontos_internos):
    pontos_estrela.extend([ponto_ext, ponto_int])

# Inicializando o pygame
pygame.init()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenchendo a tela com branco
    screen.fill((255, 255, 255))

    # Desenhando a estrela preenchida em amarelo
    pygame.draw.polygon(screen, (255, 255, 0), pontos_estrela)

    # Atualizando a tela
    pygame.display.flip()

# Encerrando o pygame
pygame.quit()
