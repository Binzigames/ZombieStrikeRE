import pyray as pr
import ZVOmbie as vagina


class PPO:
    def __init__(self):
        self.x = 145
        self.y = 470
        self.destroyed = False  # Флаг для знищення кулі
        self.rectangle = pr.Rectangle(self.x, self.y, 3, 3)  # Рект кулі
        self.vag = vagina.ZVOmbie()  # Ініціалізуємо ворога

    def Draw(self):
        if not self.destroyed:  # Малюємо тільки, якщо куля існує
            pr.draw_circle_v(pr.Vector2(self.x, self.y), 3, pr.YELLOW)

    def Update(self):
        if not self.destroyed:  # Оновлення, якщо куля ще не знищена
            self.x += 1  # Рух кулі
            self.rectangle = pr.Rectangle(self.x, self.y, 3, 3)  # Оновлюємо рект кулі

            # Перевірка колізії з ворогом
            if pr.check_collision_recs(self.rectangle, self.vag.rect):
                self.destroyed = True  # Куля знищується
                self.vag.destroyed = True  # Ворог теж знищується
