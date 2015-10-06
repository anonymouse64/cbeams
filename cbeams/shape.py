
class Shape():

    def __init__(self, slivers):
        self.slivers = slivers

    def __str__(self):
        return ''.join(
            self.terminal.move(y, x) + ' ' * length
            for y, x, length in self.slivers
        )

    @staticmethod
    def RectFill(terminal, y1, x1, y2, x2):
        '''
        A rectangle from top left (y1, x1), to bottom right (y2, x2), inclusive.
        Negative co-ords are interpretted from the right/bottom terminal edge.
        e.g. RectFill(0, 1, -1, -2) gives:

             x
             01234
          y 0 ###
            1 ###
            2 ###

        '''
        y1 %= terminal.height
        y2 %= terminal.height
        if y1 > y2:
            raise ValueError('{}(y1) > {}(y2)'.format(y1, y2))
        x1 %= terminal.width
        x2 %= terminal.width
        if x1 > x2:
            raise ValueError('{}(x1) > {}(x2)'.format(x1, x2))
        return Shape([
            (y, x1, x2 - x1 + 1)
            for y in range(y1, y2 + 1)
        ])

