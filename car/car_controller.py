import math

from car.car import Car

class VehicleController:

    def __init__(self, min_following_distance, accel_smoothing, reaction_time,max_accel, comf_decel,
                 max_speed, current_speed):
        self.min_follow_dist = min_following_distance
        self.accel_smoothing = accel_smoothing
        self.reaction_time = reaction_time
        self.max_accel = max_accel
        self.comfortable_decel = comf_decel
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.current_accel = 0

    def update_motion(self, dt, lead: Car, lead_distance):
        # Update position and velocity
        if self.current_speed + self.current_accel * dt < 0:
            self.current_speed = 0
        else:
            self.current_speed += self.current_accel * dt

        # Update acceleration
        alpha = 0
        if lead:
            delta_x = lead_distance
            delta_v = self.current_speed - lead.speed

            sqrt_ab = 2*math.sqrt(self.max_accel * self.comfortable_decel)

            alpha = (self.min_follow_dist + max(0, self.reaction_time * self.current_speed + delta_v * self.current_speed / sqrt_ab)) / delta_x

        self.current_accel = self.max_accel * (1 - (self.current_speed / self.max_speed) ** 4 - alpha ** 2)

