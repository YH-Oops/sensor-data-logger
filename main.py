# ==========================================
#            Sensor Data Logger
# ==========================================

from data_processing import calculate_average, find_max, find_min, load_sensor_data
from visualization import create_sensor_graph


def create_report(temperatures, lights, skipped_count, invalid_rows):
    """Create the formatted report used by the terminal and analysis file."""
    total_readings = len(temperatures) + skipped_count
    report_lines = [
        "=" * 40,
        "        SENSOR DATA ANALYSIS",
        "=" * 40,
        "",
    ]

    if invalid_rows:
        report_lines.append("[WARNINGS]")
        report_lines.append("")
        for row in invalid_rows:
            report_lines.append(f"Invalid row skipped: {row}")
    else:
        report_lines.append("No invalid rows detected.")

    report_lines.extend([
        "",
        "----------------------------------------",
        "DATA SUMMARY",
        "----------------------------------------",
        f"Valid readings   : {len(temperatures)}",
        f"Skipped readings : {skipped_count}",
        f"Total readings   : {total_readings}",
    ])

    if not temperatures:
        report_lines.extend([
            "",
            "[ERROR] No valid sensor readings were found.",
            "Analysis and graph were not created.",
        ])
        return "\n".join(report_lines)

    average_temperature = calculate_average(temperatures)
    maximum_temperature = find_max(temperatures)
    minimum_temperature = find_min(temperatures)
    average_light = calculate_average(lights)
    maximum_light = find_max(lights)
    minimum_light = find_min(lights)

    report_lines.extend([
        "",
        "----------------------------------------",
        "TEMPERATURE",
        "----------------------------------------",
        f"Average : {average_temperature:.2f} °C",
        f"Maximum : {maximum_temperature:.2f} °C",
        f"Minimum : {minimum_temperature:.2f} °C",
        "",
        "----------------------------------------",
        "LIGHT",
        "----------------------------------------",
        f"Average : {average_light:.2f} ADC",
        f"Maximum : {maximum_light} ADC",
        f"Minimum : {minimum_light} ADC",
        "",
        "----------------------------------------",
        "OUTPUT FILES",
        "----------------------------------------",
        "Analysis report : analysis.txt",
        "Graph           : graphs/sensor_data.png",
        "",
        "Analysis completed successfully.",
    ])

    return "\n".join(report_lines)


def main():
    temperatures, lights, skipped_count, invalid_rows = load_sensor_data("sensor_data.csv")
    report = create_report(temperatures, lights, skipped_count, invalid_rows)

    with open("analysis.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print(report)

    if not temperatures:
        return

    create_sensor_graph(temperatures, lights)


if __name__ == "__main__":
    main()
