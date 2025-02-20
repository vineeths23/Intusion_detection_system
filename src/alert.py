import os

ALERT_FILE = "logs/alerts.log"

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

def log_alerts(alerts):
    if not alerts:
        print("[*] No intrusions detected.")
        return

    with open(ALERT_FILE, "a") as f:
        for alert in alerts:
            timestamp, src_ip, dst_ip, msg = alert
            log_entry = f"[ALERT] {timestamp}: {src_ip} -> {dst_ip} | {msg}\n"
            print(log_entry.strip())
            f.write(log_entry)

if __name__ == "__main__":
    print("[*] Alerts are logged in logs/alerts.log")
