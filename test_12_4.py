import logging
import unittest
import Module_12_1_ as mod

logging.basicConfig(level=logging.INFO, filemode='w', filename='py.log',
                    format='%(asctime)s | %(levelname)s | %(message)s | ', encoding='utf-8')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'YES')
    def test_walk(self):
        try:
            runner = mod.Runner('Erzhan', -2)
            logging.info('"Test_walk" выполнен успешно')
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
        except TypeError as error_name:
            logging.warning('Неверное type для Runner', exc_info=True)
        except ValueError as error_speed:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'YES')
    def test_run(self):
        try:
            runner = mod.Runner(12, -5)
            logging.info('"Test_run" выполнен успешно')
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except TypeError as error_name:
            logging.warning('Неверное type для Runner', exc_info=True)
        except ValueError as error_speed:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'YES')
    def test_challenge(self):
        first_runner = mod.Runner("Vova")
        secont_runner = mod.Runner('Petya')
        for _ in range(10):
            first_runner.run()
            secont_runner.walk()
            self.assertNotEqual(first_runner.distance, secont_runner.distance)


if __name__ == '__main__':
    unittest.main()
