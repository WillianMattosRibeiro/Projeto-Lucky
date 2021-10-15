import unittest

class TestGetGamesConf(unittest.TestCase):
    def test_get_megasena_conf(self):
        """
        Test: Leitura das configuracoes do arquivo JSON - quina
        """
        from python.modules.configuration import Configuration
        result = Configuration().get_game_config("megasena")
        self.assertEqual(result, {'base_url': 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/', 'game_conf': 'megasena'})

    def test_get_quina_conf(self):
        """
        Test: Leitura das configuracoes do arquivo JSON - quina
        """
        from python.modules.configuration import Configuration
        result = Configuration().get_game_config("quina")
        self.assertEqual(result, {'base_url': 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/', 'game_conf': 'quina'})

    def test_get_lotofacil_conf(self):
        """
        Test: Leitura das configuracoes do arquivo JSON - quina
        """
        from python.modules.configuration import Configuration
        result = Configuration().get_game_config("lotofacil")
        self.assertEqual(result, {'base_url': 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/', 'game_conf': 'lotofacil'})