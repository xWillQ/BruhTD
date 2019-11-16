class Turn():
    """Структура для хранения данных о повороте"""
    def __init__(self, x, y, radius, clockwise):
        self.x = x
        self.y = y
        self.radius = radius
        self.clockwise = clockwise
