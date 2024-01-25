class GameCharacter:

    speed = 1.0

    def __init__(self, name, health, x_pos, y_pos):
        self.name = name
        self.health = health
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move_x(self, amount):
        self.x_pos += amount

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def check_is_dead(self):
        return self.health <= 0
    
    def change_speed(to_speed):
        GameCharacter.speed = to_speed

class PlayerCharacter(GameCharacter):

    def __init__(self, name, health, x_pos, y_pos, num_lives):
        super().__init__(name, health, x_pos, y_pos)
        self.max_health = health
        self.num_lives = num_lives

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
           self.num_lives -= 1
           self.health = self.max_health

    def check_is_dead(self):
        return self.health <= 0 and self.num_lives <= 0
    
pc = PlayerCharacter('Naz', 100, 0, 0, 3)
gc = GameCharacter('Wolf', 100, 5, 0)

print(GameCharacter.speed)
GameCharacter.change_speed(2.0)
print(pc.speed)
#pc.change_speed(3.0)   won't work because a self is also passed???
print(GameCharacter.speed)
print(pc.speed)