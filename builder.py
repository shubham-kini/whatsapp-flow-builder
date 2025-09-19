import json
import os

BASE_DIR = os.path.dirname(__file__)
SCREENS_DIR = os.path.join(BASE_DIR, "screens")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    version = load_json("version.json")
    routing_model = load_json("routing_model.json")

    # Load screens
    screens = []
    for file in sorted(os.listdir(SCREENS_DIR)):
        if file.endswith(".json"):
            screens.append(load_json(os.path.join(SCREENS_DIR, file)))

    # Build final flow JSON
    flow = {
        "version": version["version"],
        "data_api_version": version["data_api_version"],
        "routing_model": routing_model,
        "screens": screens
    }

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(os.path.join(OUTPUT_DIR, "flow.json"), "w", encoding="utf-8") as f:
        json.dump(flow, f, indent=2, ensure_ascii=False)

    print("✅ flow.json generated successfully in /output")

if __name__ == "__main__":
    main()
