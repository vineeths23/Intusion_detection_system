import pandas as pd
import os

INPUT_FILE = "datasets/traffic_log.csv"
OUTPUT_FILE = "datasets/clean_traffic.csv"

def preprocess_data():
    if not os.path.exists(INPUT_FILE):
        print("[!] No traffic log found. Run capture.py first.")
        return

    df = pd.read_csv(INPUT_FILE)

    # Normalize Protocol Numbers
    protocol_map = {6: "TCP", 17: "UDP"}
    df['Protocol'] = df['Protocol'].map(protocol_map).fillna("Other")

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    df.to_csv(OUTPUT_FILE, index=False)
    print("[*] Data Preprocessing Complete!")

if __name__ == "__main__":
    preprocess_data()
