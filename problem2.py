readings = [21.5, None, 24.0, 31.2, -4.0, 28.5, None, 35.1]
Clean_readings = []


for reading in readings:
    if reading is None:
        
        print("f{reading} is None.")
    elif reading < 0: