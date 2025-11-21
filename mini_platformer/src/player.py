import pygame

class Player:

    def __init__(self, x: int, y: int, scale: float) -> None:
        self.speed = 500.0
        self.pos = pygame.Vector2(x, y)
        self.prev_pos = self.pos
        self.dir = pygame.Vector2(0, 0)
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale_by(self.image, scale)
        self.rect = self.image.get_rect(center=self.pos)

    def handle_inputs(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_l]):
            self.dir.x = 1
        elif (keys[pygame.K_j]):
            self.dir.x = -1
        else:
            self.dir.x = 0

    def update(self, dt: float):
        self.prev_pos = self.pos
        self.pos += self.speed * self.dir * dt
        self.rect.center = self.pos

    def render(self, surface: pygame.Surface, alpha: float):
        render_pos = pygame.Vector2.lerp(self.prev_pos, self.pos, alpha)
        render_rect = (render_pos.x,
                       render_pos.y,
                       self.rect.width,
                       self.rect.width)
        surface.blit(self.image, render_rect)
