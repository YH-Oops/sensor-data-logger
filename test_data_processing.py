"""Basic tests for sensor statistics and CSV parsing."""

import tempfile
import unittest
from pathlib import Path

from data_processing import calculate_average, find_max, find_min, load_sensor_data


class StatisticsTests(unittest.TestCase):
    def test_calculate_average(self):
        self.assertAlmostEqual(calculate_average([20.4, 24.1, 25.7]), 23.4)
        self.assertEqual(calculate_average([-10, 0, 10]), 0)

    def test_find_max(self):
        self.assertEqual(find_max([24.1, 28.9, 20.4]), 28.9)
        self.assertEqual(find_max([-5, -2, -8]), -2)

    def test_find_min(self):
        self.assertEqual(find_min([24.1, 20.4, 28.9]), 20.4)
        self.assertEqual(find_min([-5, -8, -2]), -8)

    def test_single_reading(self):
        self.assertEqual(calculate_average([25]), 25)
        self.assertEqual(find_max([25]), 25)
        self.assertEqual(find_min([25]), 25)


class LoadSensorDataTests(unittest.TestCase):
    def load_csv(self, rows):
        """Read a temporary fixture without changing sensor_data.csv."""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "readings.csv"
            path.write_text("temperature,light\n" + rows, encoding="utf-8")
            return load_sensor_data(path)

    def test_fully_valid_data(self):
        result = self.load_csv("20.4,532\n24.1,542\n")
        self.assertEqual(result, ([20.4, 24.1], [532, 542], 0, []))

    def test_invalid_temperature(self):
        result = self.load_csv("abc,620\n")
        self.assertEqual(result, ([], [], 1, [["abc", "620"]]))

    def test_invalid_light(self):
        result = self.load_csv("27.1,hello\n")
        self.assertEqual(result, ([], [], 1, [["27.1", "hello"]]))

    def test_empty_fields(self):
        result = self.load_csv(",580\n25.0,\n,\n")
        self.assertEqual(
            result, ([], [], 3, [["", "580"], ["25.0", ""], ["", ""]])
        )

    def test_mixed_valid_and_invalid_rows(self):
        result = self.load_csv(
            "20.4,532\nabc,620\n27.1,hello\n,580\n24.1,542\n"
        )
        self.assertEqual(
            result,
            ([20.4, 24.1], [532, 542], 3,
             [["abc", "620"], ["27.1", "hello"], ["", "580"]]),
        )
        temperatures, lights, skipped_count, _ = result
        self.assertEqual(len(temperatures), 2)
        self.assertEqual(len(lights), 2)
        self.assertEqual(len(temperatures) + skipped_count, 5)

    def test_missing_column_and_blank_row(self):
        result = self.load_csv("25.0\n\n20.4,532\n")
        self.assertEqual(result, ([20.4], [532], 2, [["25.0"], []]))

    def test_header_only(self):
        self.assertEqual(self.load_csv(""), ([], [], 0, []))


if __name__ == "__main__":
    unittest.main()
