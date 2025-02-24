class GameStats:
    """Track statistics for alien invasion """

    def __init__(self, ai_game):
        """Initialize statistics"""
        # start Alien invasion in an active state
        self.game_active = True

        self.settings = ai_game.settings
        self.restart_stats()

    def restart_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit