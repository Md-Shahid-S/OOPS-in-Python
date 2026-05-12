# Notice: NO shared base class, NO inheritance between these classes
# They're completely unrelated — but they all have a save() method

class DatabaseWriter:
    def __init__(self, connection_string: str):
        self.connection = connection_string

    def save(self, data: dict):
        print(f"[DB]    Saving to database ({self.connection}): {data}")


class FileWriter:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def save(self, data: dict):
        print(f"[FILE]  Writing to {self.filepath}: {data}")


class APIWriter:
    def __init__(self, endpoint: str, api_key: str):
        self.endpoint = endpoint
        self.api_key = api_key

    def save(self, data: dict):
        print(f"[API]   POST to {self.endpoint}: {data}")


class CloudWriter:
    def __init__(self, bucket: str):
        self.bucket = bucket

    def save(self, data: dict):
        print(f"[CLOUD] Uploading to bucket '{self.bucket}': {data}")


# This function works with ANY object that has a save() method
# It doesn't check type — it just calls save() and trusts it's there
def persist_ml_results(writer, results: dict):
    print(f"\nPersisting ML results via {writer.__class__.__name__}...")
    writer.save(results)
    print("Done.")


results = {
    "model": "MARCO-v2",
    "accuracy": 0.947,
    "f1_score": 0.931,
    "epoch": 50
}

# All four completely unrelated objects work perfectly
persist_ml_results(DatabaseWriter("postgresql://localhost/marco"), results)
persist_ml_results(FileWriter("/outputs/results.json"), results)
persist_ml_results(APIWriter("https://api.mlflow.com/runs", "sk-abc123"), results)
persist_ml_results(CloudWriter("marco-experiment-bucket"), results)

# Python never asked "is this a DatabaseWriter?"
# It only asked "does this object have a save() method?" — yes → run it