# program entry point
import random
from data import constants
from data.point import Point
from data.control_actors_action import ControlActorsAction
from data.draw_actors_action import DrawActorsAction
from data.collisions import Collisions
from data.move_actors_action import MoveActorsAction
from data.arcade_input_service import ArcadeInputService
from data.arcade_output_service import ArcadeOutputService


from data.player import Player
from data.brick import Brick
from data.enemy import Enemy

from data.director import Director
import arcade

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    player = Player()
    cast["player"] = [player]

    cast["enemy"] = []

    for i in range(constants.NUM_ENEMY):
        enemy = Enemy()
        cast["enemy"].append(enemy)
        pass

    cast["bricks"] = []
    for x in range(constants.BRICK_WIDTH * 2,
                constants.MAX_X - constants.BRICK_WIDTH * 2,
                constants.BRICK_WIDTH + constants.BRICK_SPACE):
        for y in range(int(constants.MAX_Y * .7),
                    int(constants.MAX_Y * .9),
                    constants.BRICK_HEIGHT + constants.BRICK_SPACE):
            brick = Brick(x, y)
            cast["bricks"].append(brick)
    


    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = Collisions()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the data
    director = Director(cast, script, input_service)
    director.setup()
    arcade.run()


if __name__ == "__main__":
    main()