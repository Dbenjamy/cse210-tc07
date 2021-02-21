from time import sleep
from game import constants
from game.score import Score
from game.wordActor import WordActor
from game.point import Point

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

    def start_game(self):
        """Controls the loop that executes each step of the game.

        Args: 
            Self (Director): An instance of Director
        """
        while self._keep_playing == True:
            word = self._get_inputs()
            self._do_updates(word)
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
                if "*" in user_word:
                    user_word.replace("*", "")
                return user_word

    def _do_updates(self, word):
        """Manages the game events that must be executed. In this case
        it would be managing when a word hits the wall, how many losses
        the user has and can have, and if they typed a correct word.

        Args:
            Self (Director): An instance of Director
        """
        self.check_win(word)
        self.check_wall()
        self.track_loss()

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means refreshing the screen, and drawing the necessary
        words, score, and end game messages.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()

        # TODO: AS ACTOR AND WORD ARE FINISHED I WILL UPDATE THIS CODE 
        # TO CORRECTLY PASS THE WORDS AND SCORE TO OUTPUT_SERVICE
        self._output_service.draw_actors(self._word)
        self._output_service.draw_actor(self._score)

        self._output_service.flush_buffer()

    def check_wall(self):
        """This method will execute the necessary code to check and
        track if a word has hit the right wall.

        Args:
            Self (Director): An instance of Director
        """
        # for n in list_actors:
        self.hit_wall = 0
        if len(self._word) + self._word.get_x() > constants.MAX_X:
            self.hit_wall += 1
            self._word.reset(self._word)
            ##TODO: Change to represent accurate indexes
        

    def track_loss(self):
        """This method will run the necessary code when the end
        of the game has been reached.

        Args: 
            Self (director): An instance of Director
        """
        if self.hit_wall >= 5:
            self._keep_playing = False

    def check_win(self, word):
        """This method will execute the portion of code that 
        will compare the users word to all current words and 
        update the score accordingly.

        Args:
            self (Director): An instance of Director
            word: the word entered by the user.
        """
        self._score.update_score(self._word.compare_words(word))