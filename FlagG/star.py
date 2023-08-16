import pygame
import math  

#Inicializa o Pygame
pygame.init()

#Define o tamanho do espaço (Comprimento e largura)
width, height = 300, 200 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Estrela de Cinco Pontos")

#Definindo o ponto médio na resolução para utilizar como centro da estrela

center_x, center_y = width // 2, height // 2

raio = 80

pontos = []
for i in range(5):
    angulo = math.radians(i * 72)  # Convertendo para radianos
    x = center_x + raio * math.cos(angulo)
    y = center_y - raio * math.sin(angulo)
    pontos.append((int(x), int(y)))

# Inicializando o pygame
print(str(pontos))
pygame.init()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenchendo a tela com branco
    screen.fill((255, 255, 255))

    # Desenhando os pontos da estrela
    for ponto in pontos:
        pygame.draw.circle(screen, (0, 0, 0), ponto, 5) # Desenhando círculo de raio 5

# Desenhando a estrela preenchida em amarelo
    pygame.draw.polygon(screen, (255, 255, 0), pontos)

  
    # Atualizando a tela
    pygame.display.flip()
  

# Encerrando o pygame
pygame.quit()
