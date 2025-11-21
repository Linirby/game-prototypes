import pygame
from src.player import Player
from src.timer import Timer

class Game:

    def __init__(self) -> None:

        # TIME
        self.game_timer = Timer(60)

        # WINDOW SETTINGS
        pygame.display.set_caption("Mini Platformer - by Lili (Linirby)")
        self.window_size = (1280, 720)
        self.window = pygame.display.set_mode(self.window_size)

        self.scaling = 5.0
        self.player = Player(x=0, y=0, scale=5)

        self.running = True

    def handle_events(self, event: pygame.event.Event) -> None:
        if (event.type == pygame.QUIT):
            self.running = False

        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_q):
                self.running = False

        self.player.handle_inputs();

    def update(self, fixed_dt: float) -> None:
        self.player.update(fixed_dt)

    def render(self, alpha: float) -> None:
        self.window.fill((0, 0, 0))
        self.player.render(self.window, alpha)
        pygame.display.update()

    def run(self) -> None:
        fixed_dt = self.game_timer.get_fixed_delta()

        while (self.running):

            self.game_timer.update()
            # HANDLE EVENT
            for event in pygame.event.get():
                self.handle_events(event)
            # FIXED UPDATE
            while (self.game_timer.can_fixed_update()):
                self.update(fixed_dt)
                self.game_timer.consume_fixed_update()
            # RENDER WITH ALPHA
            alpha = self.game_timer.get_alpha()
            self.render(alpha)

            self.game_timer.frame_limiter(120)
