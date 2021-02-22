from game import constants
from game.actor import Actor
from game.point import Point
import random

class WordActor:
    """A limbless reptile. The responsibility of Snake is keep track of its segments. It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The snake's body (a list of Actor instances)
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Snake): An instance of snake.
        """
        super().__init__()
        self._segments = []
        self._prepare_body()
    
    def get_all(self):
        """Gets all the snake's segments.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            list: The snake's segments.
        """
        return self._segments

    def get_body(self):
        """Gets the snake's body.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            list: The snake's body.
        """
        return self._segments[1:]

    def get_head(self):
        """Gets the snake's head.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            Actor: The snake's head.
        """
        return self._segments[0]

    def grow_tail(self):
        """Grows the snake's tail by one segment.
        
        Args:
            self (Snake): An instance of snake.
        """
        tail = self._segments[-1]
        offset = tail.get_velocity().reverse()
        text = "#"
        position = tail.get_position().add(offset)
        velocity = tail.get_velocity()
        self._add_segment(text, position, velocity)
    
    def move(self):
        """Moves the snake in the given direction.

        Args:
            self (Snake): An instance of snake.
            direction (Point): The direction to move.
        """
        for n in range(len(self._segments)):
            self._segments[n]._position._x += 1


    def _choose_word(self):
        return random.choice(constants.LIBRARY)

    def compare_words(self,the_word):
        found = False
        for n in range(constants.STARTING_WORDS):
            if the_word == self._segments[n]._text:
                found = True
                self.reset(self._segments[n])
                return found

    def _add_segment(self, position, velocity):
        """Adds a new segment to the snake using the given text, position and velocity.

        Args:
            self (Snake): An instance of snake.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(self._choose_word())
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)

    def _prepare_body(self):
        """Prepares the snake body by adding segments.
        
        Args:
            self (Snake): an instance of Snake.
        """
        x = 0
        y = 2
        for n in range(constants.STARTING_WORDS):
            position = Point(x, y + 2*n)
            velocity = Point(1, 0)
            self._add_segment(position, velocity)

    def reset(self, _wordActor):
        """Resets a word on screen.

        Args:
            Self (wordActor): an instance of WordActor
        """
        _wordActor._text = random.choice(constants.LIBRARY)
        _wordActor._position._x = 0