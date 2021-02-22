from time import sleep
from game import constants
from game.score import Score
from game.wordActor import WordActor
from game.point import Point
from game.actor import Actor

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller
    """

    def __init__(self, input_service, output_service):
        """Class constructor

        Args:
            self (Director): An instance of director
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._word = WordActor()     
        self.user_word = Actor()
        self.user_word._position._y = constants.MAX_Y + 1

    def start_game(self):
        """Controls the loop that executes each step of the game.

        Args: 
            Self (Director): An instance of Director
        """
        
        while self._keep_playing == True:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """This method excutes the part of the program responsible for
        gathering the users input. In this game it would be the letters
        or words being typed by the user.

        Args:
            Self (Director): An instance of Director
        """
        user_letter = self._input_service.get_letter()
        if  user_letter == "*":
            self.check_win()
        self.user_word.set_text(self.user_word._text + user_letter)

    def _do_updates(self):
        """Manages the game events that must be executed. In this case
        it would be managing when a word hits the wall, how many losses
        the user has and can have, and if they typed a correct word.

        Args:
            Self (Director): An instance of Director
        """

        self.check_wall()
        # self.track_loss()

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means refreshing the screen, and drawing the necessary
        words, score, and end game messages.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._word.move()
        self._output_service.clear_screen()
        # TODO: AS ACTOR AND WORD ARE FINISHED I WILL UPDATE THIS CODE 
        # TO CORRECTLY PASS THE WORDS AND SCORE TO OUTPUT_SERVICE
        self._output_service.draw_actors(self._word)
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actor(self.user_word)
        self._output_service.flush_buffer()

    def check_wall(self):
        """This method will execute the necessary code to check and
        track if a word has hit the right wall.

        Args:
            Self (Director): An instance of Director
        """
        self.hit_wall = 0
        for n in range(len(self._word._segments)):
            if len(self._word._segments[n]._text) + self._word._segments[n]._position.get_x() > constants.MAX_X:
                self.hit_wall += 1
                self._word.reset(self._word._segments[n])
                ##TODO: Change to represent accurate indexes
        

    def track_loss(self):
        """This method will run the necessary code when the end
        of the game has been reached.

        Args: 
            Self (director): An instance of Director
        """
        if self.hit_wall >= 5:
            self._keep_playing = False

    def check_win(self):
        """This method will execute the portion of code that 
        will compare the users word to all current words and 
        update the score accordingly.

        Args:
            self (Director): An instance of Director
            word: the word entered by the user.
        """
        self._score.add_points(self._word.compare_words(self.user_word._text))
        self.user_word._text = ""

        self._output_service.flush_buffer()
        self._output_service.clear_screen()