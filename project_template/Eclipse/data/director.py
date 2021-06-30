import arcade
from data import constants

class Director(arcade.Window):
    def __init__(self, cast, script, input_service):
        """Initialize the game
        """
        super().__init__(constants.MAX_X, constants.MAX_Y, "director")

        self._cast = cast
        self._script = script
        self._input_service = input_service

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_update(self, delta_time):
        self._cue_action("update")
        if(self._cast["player"][0].get_game_over()):
            print("game over")
            #self.texture = arcade.load_texture("game_over.png")


    def on_draw(self):
        self._cue_action("output")

    def on_key_press(self, symbol, modifiers):
        self._input_service.set_key(symbol, modifiers)
        self._cue_action("input")

    def on_key_release(self, symbol, modifiers):
        self._input_service.remove_key(symbol, modifiers)
        self._input_service.end_attack() #this will end the attack so it doesn't kill everything for the rest of the game.
        self._cue_action("input")

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)