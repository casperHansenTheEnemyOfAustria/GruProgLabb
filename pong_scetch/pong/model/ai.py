
""" Simple ai for testing"""
class AI:
    def __init__(self, paddle, ball_reader) -> None:
        self.paddle = paddle
        self.ball_reader = ball_reader
        self.run()
    
    def run(self):
        """Moves set paddle to position of ball. ()"""
        self.paddle.set_y(self.ball_reader.get_y())
        
        pass
    
    