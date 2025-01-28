import pyray as pr
import ZVOmbie as vagina


class PPO:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.destroyed = False  # Флаг для знищення кулі
        self.rectangle = pr.Rectangle(self.x, self.y, 5, 5)  # Рект кулі

    def Draw(self):
        if not self.destroyed:  # Малюємо тільки, якщо куля існує
            pr.draw_circle_v(pr.Vector2(self.x, self.y), 5, pr.YELLOW)

    def Update(self):
        if not self.destroyed:  # Оновлення, якщо куля ще не знищена
            self.x += 5  # Рух кулі вперед
            self.rectangle = pr.Rectangle(self.x, self.y, 3, 3)  # Оновлюємо рект кулі

            # Перевірка, чи куля вийшла за межі екрану
            if self.x > pr.get_screen_width():
                self.destroyed = True  # Куля знищується, якщо вона вийшла за межі екрану
