import json

# JSON data for 50 syslog entries
syslog_data = [
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 0,
        "message": "Line protocol on Interface GigabitEthernet0/1, changed state to up",
        "remote_address": ""
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 0,
        "message": "partition health measures for /var did not suffice - still using 96% of partition space",
        "remote_address": ""
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 4,
        "message": "Invalid user asmith",
        "remote_address": "192.168.10.83"
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 4,
        "message": "Invalid user bsmith",
        "remote_address": "192.168.10.83"
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 4,
        "message": "Invalid user csmith",
        "remote_address": "192.168.10.83"
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 4,
        "message": "Invalid user dsmith",
        "remote_address": "192.168.10.83"
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 4,
        "message": "Invalid user esmith",
        "remote_address": "192.168.10.83"
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 4,
        "message": "Invalid user fsmith",
        "remote_address": "192.168.10.83"
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 0,
        "message": "partition health measures for /var did not suffice - still using 96% of partition space",
        "remote_address": ""
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 0,
        "message": "partition health measures for /var did not suffice - still using 96% of partition space",
        "remote_address": ""
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 4,
        "message": "Invalid user bsmith",
        "remote_address": "192.168.10.83"
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 0,
        "message": "partition health measures for /var did not suffice - still using 96% of partition space",
        "remote_address": ""
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 0,
        "message": "Line protocol on Interface GigabitEthernet0/1, changed state to up",
        "remote_address": ""
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 4,
        "message": "Invalid user asmith",
        "remote_address": "192.168.10.83"
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 0,
        "message": "partition health measures for /var did not suffice - still using 96% of partition space",
        "remote_address": ""
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 4,
        "message": "Invalid user asmith",
        "remote_address": "192.168.10.83"
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 0,
        "message": "Line protocol on Interface GigabitEthernet0/1, changed state to up",
        "remote_address": ""
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 4,
        "message": "Invalid user asmith",
        "remote_address": "192.168.10.83"
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 0,
        "message": "partition health measures for /var did not suffice - still using 96% of partition space",
        "remote_address": ""
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 0,
        "message": "Line protocol on Interface GigabitEthernet0/1, changed state to up",
        "remote_address": ""
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 0,
        "message": "partition health measures for /var did not suffice - still using 96% of partition space",
        "remote_address": ""
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 0,
        "message": "partition health measures for /var did not suffice - still using 96% of partition space",
        "remote_address": ""
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 4,
        "message": "Invalid user dsmith",
        "remote_address": "192.168.10.83"
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 0,
        "message": "partition health measures for /var did not suffice - still using 96% of partition space",
        "remote_address": ""
    },
    {
        "ts": 1634382476,
        "host": "asgard.example.com",
        "facility": 4,
        "message": "Invalid user bsmith",
        "remote_address": "192.168.10.83"
    }
]

# Write the JSON data to a log file
with open("syslog.log", "w") as log_file:
    for entry in syslog_data:
        log_file.write(json.dumps(entry) + "\n")

print("Log file 'syslog.log' created.")
