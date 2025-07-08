# monitor/mock_system_stats.py

import datetime
import random

def get_mock_stats():
    now = datetime.datetime.now().isoformat()

    return {
        "timestamp": now,
        "cpu_percent": round(random.uniform(15.0, 90.0), 2),
        "ram_percent": round(random.uniform(30.0, 95.0), 2),
        "disk_storage_percent": round(random.uniform(60.0, 99.0), 2),
        "read_speed": round(random.uniform(50.0, 500.0), 2),     # in MB/s
        "write_speed": round(random.uniform(30.0, 300.0), 2),    # in MB/s
    }
