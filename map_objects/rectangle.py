class Rect:
    """
    Takes the x and y coordinates of the top left corner, and computes the bottom right corner based on the w and h parameters (width and height)
    """
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h