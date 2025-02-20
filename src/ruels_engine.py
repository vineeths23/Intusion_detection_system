import pandas as pd
import os
import alert

RULES_FILE = "rules/detection_rules.txt"
LOG_FILE = "datasets/clean_traffic.csv"

# Ensure rules directory exists
os.makedirs("rules", exist_ok=True)

# Sample rules (Modify as needed)
default_rules = [
    "TCP,80,ALERT: Possible HTTP Flood",
    "TCP,23,ALERT: Possible Telnet Attack",
    "UDP,53,ALERT: Possible DNS Flood",
    "TCP,22,ALERT: Possible Brute Force SSH Attack"
]

# Create rules file if not exists
if not os.path.exists(RULES_FILE):
    with open(RULES_FILE, "w") as f:
        f.write("\n".join(default_rules))

def load_rules():
    rules = []
    with open(RULES_FILE, "r") as f:
        for line in f:
            protocol, port, alert_msg = line.strip().split(",")
            rules.append((protocol, int(port), alert_msg))
    return rules

def check_intrusions():
    if not os.path.exists(LOG_FILE):
        print("[!] No traffic data found. Run preprocess.py first.")
        return

    df = pd.read_csv(LOG_FILE)
    rules = load_rules()

    alerts = []
    for _, row in df.iterrows():
        for rule in rules:
            protocol, port, alert_msg = rule
            if row['Protocol'] == protocol and int(row['Destination IP'].split(".")[-1]) == port:
                alerts.append((row['Timestamp'], row['Source IP'], row['Destination IP'], alert_msg))

    alert.log_alerts(alerts)

if __name__ == "__main__":
    check_intrusions()
