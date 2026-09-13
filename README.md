# Sensor Data Logger

A small Python program that reads temperature and light readings from a CSV file, calculates basic statistics, and creates a text report and graph. It processes stored data only; hardware connections and real-time sensor collection are not implemented.

## Main features

- Read temperature and light values from a CSV file.
- Skip and report rows with missing or incorrectly formatted values.
- Count valid, skipped, and total readings.
- Calculate the average, minimum, and maximum for each measurement.
- Print a summary, save a text report, and plot both measurements against reading number.
- Configure input and output file paths with `config.json`.

## Project structure

```text
Data Sensor Logger/
|-- main.py                  # Loads configuration and runs the analysis
|-- data_processing.py       # CSV loading and statistics functions
|-- visualization.py         # Graph creation and display
|-- test_data_processing.py  # Automated tests
|-- config.json              # Input and output paths
|-- sensor_data.csv          # Sample input readings
|-- analysis.txt             # Generated text report
|-- graphs/
|   `-- sensor_data.png      # Generated graph
|-- .gitignore               # Excludes generated outputs and Python caches
`-- README.md
```

## How to run

Install Python 3 with pip, then open a terminal in the project folder (the folder containing `main.py` and `config.json`).

Install Matplotlib, the external library used for graphs:

```sh
python -m pip install matplotlib
```

Run the program:

```sh
python main.py
```

The program prints the analysis, saves the output files, and opens a graph window when a graphical display is available. Close the graph window to finish the run.

## Automated tests

From the project folder, run:

```sh
python -m unittest discover -v
```

The 11 tests cover statistics calculations and CSV loading, including valid data, invalid values, empty fields, missing columns, blank rows, and header-only input. They use temporary CSV files and do not change `sensor_data.csv`. The tests use Python's built-in `unittest` module; no separate test library is required.

## Input file

The default input is `sensor_data.csv`. It must contain a header row followed by temperature in the first column and an integer light reading in the second column:

```csv
temperature,light
20.4,532
24.1,542
25.7,561
```

Temperature values are parsed as decimal numbers and reported in degrees Celsius. Light values are parsed as integers. Rows whose first two values cannot be parsed are skipped and listed in the report.

The included sample has 30 readings: 25 valid rows and 5 deliberately invalid rows.

**Current labeling limitation:** the text report labels light values as ADC, while the graph labels them as lux. The program does not convert between these units.

## Generated outputs

- **Terminal summary:** skipped-row warnings, reading counts, statistics, and output paths.
- **`analysis.txt`:** the same text report saved as a UTF-8 file.
- **`graphs/sensor_data.png`:** a graph with separate temperature and light axes, plotted against valid reading number.

Output files are overwritten when the program runs. The graph directory is created automatically. If there are no valid readings, the program writes and prints an error summary and skips graph creation; any graph from a previous run remains.

## Configuration

`config.json` specifies the files the program reads and writes:

```json
{
  "sensor_data_file": "sensor_data.csv",
  "analysis_file": "analysis.txt",
  "graph_file": "graphs/sensor_data.png"
}
```

- `sensor_data_file`: path to the input CSV file.
- `analysis_file`: path for the text report.
- `graph_file`: path for the saved graph.

Keep all three keys. Relative paths are resolved from the folder where you run the command, so run it from the project folder. The input file must exist. If you choose a different folder for the analysis report, create that folder first; only the graph's folder is created automatically.

## Technologies used

- **Python 3** for program logic and data processing.
- **Matplotlib** for plotting and saving the graph.
- **Python standard library** modules including `csv`, `json`, and `unittest`.
- **CSV and JSON** for input data and configuration.
