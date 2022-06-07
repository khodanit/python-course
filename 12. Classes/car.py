class Car:
    cars = 0

    def __init__(self, speed=0, heading=0):
        self.speed = speed
        self.heading = heading

    def accelerate(self, inc):
        self.speed += inc

    def brake(self):
        self.speed -= 1

    def turn(self, angle):
        heading = self.heading
        heading += angle
        if heading > 360:
            heading -= 360
        elif heading < 0:
            heading += 360
        self.heading = heading

    def __setattr__(self, name, value):
        if name == "speed" and value > 20:
            print("too fast")
        super().__setattr__(name, value)

    def __str__(self):
        return "Car@speed %d" % self.speed


class Convertible(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.top = "soft"
        self.closed = True

    def open_top(self):
        self.closed = False

    def close_top(self):
        self.closed = True
