import unittest
from src.chapter8.greedy import (
    classroom_scheduling,
    knapsack,
    truck_loading,
    europe_trip,
    set_cover,
)


class TestGreedyAlgorithms(unittest.TestCase):
    def test_classroom_scheduling(self) -> None:
        classes = [
            (1, 4),
            (3, 5),
            (0, 6),
            (5, 7),
            (3, 9),
            (5, 9),
            (6, 10),
            (8, 11),
            (8, 12),
            (2, 14),
            (12, 16),
        ]
        result = classroom_scheduling(classes)
        self.assertEqual(result, [(1, 4), (5, 7), (8, 11), (12, 16)])

    def test_knapsack(self) -> None:
        items = [("item1", 10, 60), ("item2", 20, 100), ("item3", 30, 120)]
        capacity = 50
        result = knapsack(items, capacity)
        expected = [("item2", 20, 100), ("item3", 30, 120)]
        self.assertCountEqual(result, expected)
        total_weight = sum(item[1] for item in result)
        self.assertLessEqual(total_weight, capacity)

    def test_truck_loading(self) -> None:
        boxes = [10, 5, 7, 3, 2, 8]
        truck_capacity = 20
        result = truck_loading(boxes, truck_capacity)
        self.assertEqual(result, [10, 8, 2])

    def test_europe_trip(self) -> None:
        places = [
            ("Paris", 9, 2),
            ("Rome", 7, 3),
            ("London", 8, 2),
            ("Berlin", 6, 2),
            ("Barcelona", 5, 1),
        ]
        days = 7
        result = europe_trip(places, days)
        expected = [
            ("Paris", 9, 2),
            ("London", 8, 2),
            ("Berlin", 6, 2),
            ("Barcelona", 5, 1),
        ]
        self.assertCountEqual(result, expected)
        total_days = sum(place[2] for place in result)
        self.assertLessEqual(total_days, days)

    def test_set_cover(self) -> None:
        states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
        stations = {
            "kone": set(["id", "nv", "ut"]),
            "ktwo": set(["wa", "id", "mt"]),
            "kthree": set(["or", "nv", "ca"]),
            "kfour": set(["nv", "ut"]),
            "kfive": set(["ca", "az"]),
        }
        result = set_cover(states, stations)
        self.assertTrue(result.issuperset({"ktwo", "kthree", "kfive"}))
        self.assertTrue(len(result) <= 4)


if __name__ == "__main__":
    unittest.main()
