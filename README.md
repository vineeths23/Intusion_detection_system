# Intrusion Detection System (IDS)

## Overview

This **Intrusion Detection System (IDS)** is designed to **monitor network traffic in real-time** and detect potential security threats based on predefined rules. It helps in identifying suspicious activities such as port scans, brute force attacks, and unauthorized access attempts.

## Features

- **Real-time Network Monitoring**: Captures and analyzes live network traffic.
- **Rule-Based Detection**: Uses custom detection rules to identify attacks.
- **Alert System**: Generates alerts when suspicious activity is detected.
- **Logging**: Stores detected threats in a log file for future analysis.
- **Modular Design**: Organized in different modules for easy maintenance and updates.

## Project Structure

```
IDS_PROJECT/
│-- datasets/
│   │-- clean_traffic.csv        # Clean traffic data for testing
│   │-- traffic_log.csv          # Captured network traffic logs
│-- logs/
│   │-- alerts.log               # Logs of detected alerts
│-- rules/
│   │-- detection_rules.txt      # Custom rules for threat detection
│-- src/
│   │-- __init__.py
│   │-- alert.py                 # Alert generation module
│   │-- capture.py               # Network traffic capturing module
│   │-- main.py                  # Main execution script
│   │-- preprocess.py            # Preprocessing of network data
│   │-- rules_engine.py          # Rule-based detection engine
│-- requirements.txt             # Dependencies and required packages
│-- README.md                    # Project documentation (this file)
```

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/vineeths23/Intrusion_detection_system.git
   cd Intrusion_detection_system
   ```

2. **Install Required Packages**

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the IDS**

   ```sh
   python src/main.py
   ```

## How It Works

1. **Traffic Capture**: The IDS listens for incoming and outgoing network packets.
2. **Preprocessing**: Extracts relevant features from network packets.
3. **Detection Engine**: Compares traffic patterns against predefined rules in `detection_rules.txt`.
4. **Alert Generation**: If a rule is matched, an alert is logged in `alerts.log`.

## Configuration

- Modify the **detection rules** in `rules/detection_rules.txt` to customize threat detection.
- Change **logging settings** in `logs/alerts.log` if needed.

## Example Alert Output

```
[ALERT] 1740062271.6610477: 192.168.1.187 -> 20.195.84.23 | ALERT: Possible Telnet Attack
[ALERT] 1740062286.66195: 192.168.1.187 -> 20.195.84.23 | ALERT: Possible Telnet Attack
```

## Future Improvements

- Add more advanced rule sets for better detection.
- Implement a web dashboard for real-time monitoring.
- Integrate anomaly-based detection techniques (non-ML based).

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License.

---

Developed by **Vineeth S**

