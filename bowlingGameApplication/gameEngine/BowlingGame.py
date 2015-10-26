from bowlingGameApplication.gameEngine.Game import Game


class BowlingGame(Game):
    """ Implementation class for bowling game.
    Game is played with number of pins hit per round.
    Player with maximum scores wins the game.
    """

    def __init__(self):
        self._rolls = [0]*21
        self._currentRoll = 0

    def roll(self, pins):
        try:
            self._rolls[self._currentRoll] = pins
            self._currentRoll += 1
            # print( self._rolls)
        except IndexError:
            print("Rolled more then permitted in a game")
            raise

    def score(self):
        """ Calculates the score of a game
        :return: Total score
        """
        score = 0
        frames = 10
        frame_index = 0
        for _ in xrange(frames):
            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):   # Spare
                score += 10 + self._rolls[frame_index+2]
                frame_index += 2
            else:
                score += self._rolls[frame_index] + self._rolls[frame_index+1]
                frame_index += 2
        try:
            if score <= 300:
                return score
            else:
                raise Exception('ScoreError: Invalid score generated')
        except Exception as e:
            print e
            raise

    def _is_spare(self, frame_index):
        """ Check if current frame is spare. (Spare means sum of two throws in same frame is 10)
        :param frame_index: Current throw in a frame
        :return: Boolean
        """
        return self._rolls[frame_index] + self._rolls[frame_index + 1] == 10

    def _is_strike(self, frame_index):
        """ Strike if player pins all 10 balls in a single throw
        :param frame_index: current frame in a game. A game has total of 10 frames
        :return: Boolean
        """
        return self._rolls[frame_index] == 10

    def _strike_bonus(self, frame_index):
        """ When strike Bonus is sum of score of next frame
        :param frame_index: current frame
        :return: Bonus value
        """
        return self._rolls[frame_index + 1] + self._rolls[frame_index + 2]
