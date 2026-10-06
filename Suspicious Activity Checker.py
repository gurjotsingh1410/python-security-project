logs = [
    "Login successful: john",
    "Login failed: admin",
    "Login failed: admin",
    "Login successful: sarah",
    "Login failed: admin",
    "Login failed: guest"
]

failed_logins = 0

for log in logs:
    print("Checking:", log)

    if "Login failed" in log:
        failed_logins += 1

print("\nTotal failed logins:", failed_logins)

if failed_logins >= 3:
    print("⚠️ WARNING: Suspicious activity detected!")
else:
    print("✅ No major suspicious activity detected.")
