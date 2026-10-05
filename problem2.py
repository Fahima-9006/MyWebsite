readings = [21.5, None, 24.0, 31.2, -4.0, 28.5, None, 35.1]
Clean_readings = []
alerts = []



for reading in readings:
    if reading is None:
        continue
    if reading < 0 or reading > 50:
        continue

    Clean_readings.append(reading)

    if reading > 30:
        alerts.append(reading)
average_alert = sum(alerts) / len(alerts)
print("Clear readings:", Clean_readings)
print(f"Average of alerts: {average_alert}")    
print("Alerts:", alerts)