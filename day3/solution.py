from enum import Enum
import time

file = open('input.txt', 'r')
# file = open('test_input.txt', 'r')
directions_wire1 = file.readline().split(',')
directions_wire2 = file.readline().split(',')


class Direction(Enum):
    VERTICAL = 1
    HORIZONTAL = 2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point):
        return abs(point.x - self.x) + abs(point.y - self.y)

    def distance_to_origin(self):
        return self.distance_to(Point(0, 0))


    def go_by(self, vector):
        return Point(self.x + vector.dx, self.y + vector.dy)

    def __str__(self):
        return f'({self.x},{self.y})'


class Vector:
    def __init__(self, dx, dy, direction):
        self.dx = dx
        self.dy = dy
        self.direction = direction

    def from_string(string):
        if string[0] == 'R':
            return Vector(int(string[1:]), 0, Direction.HORIZONTAL)
        elif string[0] == 'L':
            return Vector(-int(string[1:]), 0, Direction.HORIZONTAL)
        elif string[0] == 'U':
            return Vector(0, int(string[1:]), Direction.VERTICAL)
        else:
            return Vector(0, -int(string[1:]), Direction.VERTICAL)

class Segment:
    def __init__(self, start_point, vector):
        self.start = start_point
        self.vector = vector
        self.end = start_point.go_by(vector)

    def collides_with(self, segment):
        if self.direction() != segment.direction():
            if self.direction() == Direction.HORIZONTAL:
                return self.between_x(segment.start.x) and segment.between_y(self.start.y)
            else:
                return segment.between_x(self.start.x) and self.between_y(segment.start.y)
        else:
            return False

    def between_x(self, x):
        x_min = min(self.start.x, self.end.x)
        x_max = self.start.x + self.end.x - x_min
        return x >= x_min and x <= x_max

    def between_y(self, y):
        y_min = min(self.start.y, self.end.y)
        y_max = self.start.y + self.end.y - y_min
        return y >= y_min and y <= y_max

    def direction(self):
        return self.vector.direction

    def collision_point_with(self, segment):
        if self.direction() == Direction.HORIZONTAL:
            return Point(segment.start.x, self.start.y)
        else:
            return Point(self.start.x, segment.start.y)

    def __str__(self):
        return f'{self.start} -> {self.end}'

def construct_wire(directions):
    start = Point(0, 0)
    segments = []
    current_point = start
    for direction in directions:
        new_segment = Segment(current_point, Vector.from_string(direction))
        segments.append(new_segment)
        current_point = new_segment.end
    return segments

wire1_segmenents = construct_wire(directions_wire1)
wire2_segmenents = construct_wire(directions_wire2)

collisions = []
for segment1 in wire1_segmenents:
    for segment2 in filter(lambda segment: segment1.collides_with(segment), wire2_segmenents):
        collisions.append(segment1.collision_point_with(segment2))


print(min(list(map(lambda c: c.distance_to_origin(), collisions))))
