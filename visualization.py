"""Functions for creating sensor-data charts."""

import os

import matplotlib.pyplot as plt


def create_sensor_graph(temperatures, lights):
    """Create and save a two-axis temperature and light graph."""
    os.makedirs("graphs", exist_ok=True)

    reading_number = range(1, len(temperatures) + 1)
    fig, ax1 = plt.subplots()

    ax1.plot(reading_number, temperatures, label="Temperature", color="blue")
    ax1.set_xlabel("Reading Number")
    ax1.set_ylabel("Temperature (°C)", color="blue")

    ax2 = ax1.twinx()
    ax2.plot(reading_number, lights, label="Light", color="orange")
    ax2.set_ylabel("Light (lux)", color="orange")

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2)

    plt.title("Sensor Data")
    plt.savefig("graphs/sensor_data.png", dpi=300, bbox_inches="tight")
    plt.show()
