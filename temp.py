
# Extract required fields
def extract_info(data):
    records = []

    for commit in data.get("commits", []):
        record = {
            "_id": commit.get("id"),
            "request_id": commit.get("id"),  # Assuming `id` is the request_id
            "author": commit.get("author", {}).get("name"),
            "action": "PUSH" if "Merge pull request" not in commit.get("message", "") else "MERGE",
            "from_branch": data.get("before"),
            "to_branch": data.get("after"),
            "timestamp": commit.get("timestamp")
        }
        records.append(record)

    # Add the head commit separately if needed
    head_commit = data.get("head_commit", {})
    head_commit_record = {
        "_id": head_commit.get("id"),
        "request_id": head_commit.get("id"),
        "author": head_commit.get("author", {}).get("name"),
        "action": "PUSH" if "Merge pull request" not in head_commit.get("message", "") else "MERGE",
        "from_branch": data.get("before"),
        "to_branch": data.get("after"),
        "timestamp": head_commit.get("timestamp")
    }
    records.append(head_commit_record)

    return records

json_data = [
  {
    "_id": "5a021763dc9d2373dfe68f45cc99745122bf2390",
    "request_id": "5a021763dc9d2373dfe68f45cc99745122bf2390",
    "author": "venkatesh",
    "action": "PUSH",
    "from_branch": "9f1f81837bf48c07cf1308dff6c960f9910c5ff1",
    "to_branch": "58b489e8ecf120fa00d12136ff9f83159417b2ac",
    "timestamp": "2024-09-04T04:23:53+05:30"
  },
  {
    "_id": "2478282c40bcf5808b7ef701ff2c14f658ee7555",
    "request_id": "2478282c40bcf5808b7ef701ff2c14f658ee7555",
    "author": "venkatesh",
    "action": "PUSH",
    "from_branch": "9f1f81837bf48c07cf1308dff6c960f9910c5ff1",
    "to_branch": "58b489e8ecf120fa00d12136ff9f83159417b2ac",
    "timestamp": "2024-09-04T04:29:58+05:30"
  },
  {
    "_id": "58b489e8ecf120fa00d12136ff9f83159417b2ac",
    "request_id": "58b489e8ecf120fa00d12136ff9f83159417b2ac",
    "author": "venkatesh",
    "action": "MERGE",
    "from_branch": "9f1f81837bf48c07cf1308dff6c960f9910c5ff1",
    "to_branch": "58b489e8ecf120fa00d12136ff9f83159417b2ac",
    "timestamp": "2024-09-04T04:33:09+05:30"
  },
  {
    "_id": "58b489e8ecf120fa00d12136ff9f83159417b2ac",
    "request_id": "58b489e8ecf120fa00d12136ff9f83159417b2ac",
    "author": "venkatesh",
    "action": "MERGE",
    "from_branch": "9f1f81837bf48c07cf1308dff6c960f9910c5ff1",
    "to_branch": "58b489e8ecf120fa00d12136ff9f83159417b2ac",
    "timestamp": "2024-09-04T04:33:09+05:30"
  }
]