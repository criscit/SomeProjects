from unittest import TestCase

import work_planner


class WorkPlannerTest(TestCase):
    def test_maximum_income(self):
        """Maximum Income."""
        cases = [
            (2, [334934939, 1234122, 657657], 336169061),
            (5, [], 0),
            (1, [1], 1),
            (4, [1, 1, 3], 5),
            (3, [100, 50, 30, 20, 10], 180),
            (5, [1, 1, 1, 1, 1], 5),
            (0, [1], 0)
        ]
        for i, (k, prices, result) in enumerate(cases):
            with self.subTest(f"Find biggest income #{i}"):
                self.assertEqual(work_planner.find_maximum_income(prices, k), result)

    def test_minimum_managers(self):
        """Find Managers."""
        cases = [
            ([[1, 2], [2, 3]], 1),
            ([[1, 24], [5, 10], [1, 20]], 3),
            ([[7, 9], [8, 10], [9, 10]], 2),
            ([[7, 9], [8, 10]], 2),
            ([[7, 9]], 1),
            ([], 0)
        ]
        for i, (intervals, result) in enumerate(cases):
            with self.subTest(f"Find min managers #{i}"):
                self.assertEqual(work_planner.find_minimum_managers(intervals), result)

    def test_load_truck(self):
        """Fill truck."""
        cases = [
            (1000, [
                [86, 482], [911, 306], [77, 319], [663, 382],
                [58, 408], [918, 348], [395, 372], [757, 384],
                [126, 317], [325, 931]
            ], 2511.08),
            (1000, [[500, 30]], 500),
            (1, [[500, 30]], 16.6),
            (15, [[500, 30]], 250),
            (0, [[500, 30]], 0),
            (1000, [], 0)
        ]

        for i, (truck_capacity, goods, result) in enumerate(cases):
            with self.subTest(f"Fill truck #{i}"):
                self.assertEqual(work_planner.load_truck(truck_capacity, goods), result)
