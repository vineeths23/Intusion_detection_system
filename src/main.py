import capture
import preprocess
import ruels_engine

if __name__ == "__main__":
    print("[*] Running Intrusion Detection System...")
    capture.start_sniffing()
    preprocess.preprocess_data()
    rules_engine.check_intrusions()
    print("[*] IDS Execution Completed!")
