from time import sleep
from game import constants
from game.score import Score
from game.word import Word

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
        self._word = Word()

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
        user_letter = ""
        user_word = ""
        while not(user_letter == "*"):
            user_letter = self._input_service.get_letter()
            #turn individuals letters into a complete string or word to pass along
            user_word += user_letter
            
            if user_letter == "*":
                #this will call a class.method that will reset the input line to blank
                ##TODO: THIS LINE WILL SEND THE USERS WORD TO THE CLASS>METHOD WHERE IT WILL BE COMPARED
                pass

    def _do_updates(self):
        pass

    def _do_outputs(self):
        pass

    def check_wall(self):
        pass

    def check_loss(self):
        pass

    def check_win(self):
        pass