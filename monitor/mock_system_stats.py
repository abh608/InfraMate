import datetime
def get_mock_stats():
    now = datetime.datetime.now().isoformat()
    return {
        "timestamp": now,
        "cpu_percent": 23.8,
        "ram_percent": 42.7,
        "disk_storage_percent": 84.3,
    }
