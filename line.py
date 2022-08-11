from mimetypes import init


class Line:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.l = length

    def compare(self, line):
        print('first line y: ', self.y, 'second line y: ', line.y)
        print('first line terminus: ', self.y-self.l)
        if self.y > line.y and self.y-self.l < line.y:
            return True
        else:
            return False