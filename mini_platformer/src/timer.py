import pygame

class Timer:
    def __init__(self, tick_per_second) -> None:
        self.fixed_dt = 1.0 / tick_per_second
        self.accumulator = 0.0
        self.last_time = pygame.time.get_ticks() / 1000.0  # seconds
        self.alpha = 0.0

    def update(self) -> None:
        now = pygame.time.get_ticks() / 1000.0
        frame_time = now - self.last_time
        self.last_time = now
        self.accumulator += frame_time

    def can_fixed_update(self) -> bool:
        return (self.accumulator >= self.fixed_dt)

    def consume_fixed_update(self) -> None:
        self.accumulator -= self.fixed_dt

    def get_fixed_delta(self) -> float:
        return (self.fixed_dt)

    def get_alpha(self) -> float:
        return (self.accumulator / self.fixed_dt)

    def frame_limiter(self, fps) -> None:
        target_frame_time = 1.0 / fps
        now = pygame.time.get_ticks() / 1000.0
        elapsed = now - self.last_time
        if (elapsed < target_frame_time):
            delay_ms = int((target_frame_time - elapsed) * 1000)
            pygame.time.delay(delay_ms)

