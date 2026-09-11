"""Functions for loading sensor data and calculating simple statistics."""

import csv


def load_sensor_data(file_name):
    """Read valid temperature and light values from a CSV file."""
    temperatures = []
    lights = []
    skipped_count = 0
    invalid_rows = []

    with open(file_name, newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row.

        for row in reader:
            try:
                temperature = float(row[0])
                light = int(row[1])
            except (ValueError, IndexError):
                skipped_count += 1
                invalid_rows.append(row)
                continue

            temperatures.append(temperature)
            lights.append(light)

    return temperatures, lights, skipped_count, invalid_rows


def calculate_average(data):
    """Return the average value in a list."""
    total = 0

    for value in data:
        total += value

    return total / len(data)


def find_max(data):
    """Return the largest value in a list."""
    maximum = data[0]

    for value in data:
        if value > maximum:
            maximum = value

    return maximum


def find_min(data):
    """Return the smallest value in a list."""
    minimum = data[0]

    for value in data:
        if value < minimum:
            minimum = value

    return minimum
