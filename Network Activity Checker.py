import subprocess

devices = [
    "192.168.1.1",
    "192.168.1.5",
    "192.168.1.10"
]

for ip in devices:

    result = subprocess.run(
        ["ping", "-c", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print(ip, "🟢 ACTIVE")
    else:
        print(ip, "🔴 OFFLINE")
