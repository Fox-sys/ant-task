from field import Field


class Ant:
    def __init__(self, pos_x, pos_y, field: Field):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rotation = 0
        self.field = field
        self._move_map = {0: [0, -1], 1: [-1, 0], 2: [0, 1], 3: [1, 0]}

    def step(self) -> bool:
        current_color = self.field.get_color(self.pos_x, self.pos_y)
        if current_color:
            self.rotate(1)
        else:
            self.rotate(-1)
        self.field.change_color(self.pos_x, self.pos_y)
        return self.move()

    def rotate(self, side):
        if side not in [-1, 1]:
            raise Exception('Incorrect side')
        if side == 1:
            self.rotation = (self.rotation + 1) if self.rotation < 3 else 0
        else:
            self.rotation = (self.rotation - 1) if self.rotation > 0 else 3

    def move(self) -> bool:
        bias_x, bias_y = self._move_map[self.rotation]
        if self.field.size > self.pos_x + bias_x > 0 and self.field.size > self.pos_y + bias_y > 0:
            self.pos_x += bias_x
            self.pos_y += bias_y
            return True
        return False
