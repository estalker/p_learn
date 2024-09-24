import unittest
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r = Runner("Атлет 1")
        for i in range(10):
            r.walk()

        self.assertEqual(r.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r = Runner("Атлет 2")
        for i in range(10):
            r.run()

        self.assertEqual(r.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        w = Runner("Атлет 1")
        r = Runner("Атлет 2")
        for i in range(10):
            w.walk()
            r.run()

        self.assertNotEqual(w.distance, r.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.is_frozen = True
        self.h = Runner("Усэйн", 10)
        self.a = Runner("Андрей", 9)
        self.n = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            for j, entry in i.items():
                print(f"{j}:{entry}")
            print()

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_H_N(self):
        t = Tournament(5,self.n, self.h)
        all_results = t.start()
        self.all_results.append(all_results)
        last = max(all_results.keys())
        self.assertTrue(self.n == all_results[last])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_A_N(self):
        t = Tournament(5,self.n, self.a)
        all_results = t.start()
        self.all_results.append(all_results)
        last = max(all_results.keys())

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_H_A_N(self):
        t = Tournament(5,self.n, self.a, self.h)
        all_results = t.start()
        self.all_results.append(all_results)
        last = max(all_results.keys())
        self.assertTrue(self.n == all_results[last])



if __name__ == "__main__":
    unittest.main()

