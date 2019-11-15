class Turn():
    """Структура для хранения данных о повороте"""
    def __init__(self, x, y, lengthX, lengthY, direction):
        self.x = x
        self.y = y
        self.lengthX = lengthX
        self.lengthY = lengthY
        self.direction = direction
