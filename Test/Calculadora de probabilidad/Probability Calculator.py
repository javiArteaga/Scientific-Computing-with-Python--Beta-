import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        drawn_balls_count = {}
        for ball in drawn_balls:
            if ball in drawn_balls_count:
                drawn_balls_count[ball] += 1
            else:
                drawn_balls_count[ball] = 1
        
        success = True
        for ball, count in expected_balls.items():
            if drawn_balls_count.get(ball, 0) < count:
                success = False
                break
        
        if success:
            success_count += 1
    
    probability = success_count / num_experiments
    return probability