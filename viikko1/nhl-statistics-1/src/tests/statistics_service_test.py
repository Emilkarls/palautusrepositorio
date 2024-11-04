import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_haku(self):
        pelaaja = self.stats.search("Kurri")
        self.assertEqual("Kurri", pelaaja.name)

    def test_vaara_nimi(self):
        pelaaja = self.stats.search("Kuri")
        self.assertEqual(None, pelaaja)

    def test_joukkue(self):
        joukkue = self.stats.team("PIT")
        self.assertEqual("Lemieux", joukkue[0].name)
    
    def test_lajittelu(self):
        pelaaja = self.stats.top(1)
        self.assertEqual("Gretzky", pelaaja[0].name)

    def test_lajittelu_maalit(self):
        pelaaja = self.stats.top(1, SortBy.GOALS)
        self.assertEqual("Lemieux", pelaaja[0].name)

    def test_lajittelu_assists(self):
        pelaaja = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual("Gretzky", pelaaja[0].name)