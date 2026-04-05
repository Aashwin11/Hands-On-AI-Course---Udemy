import threading,time

def monitor_tea_temp():
    while True:
        print(f"Monitoring the tea Temp...")
        time.sleep(2)


threading.Thread(target=monitor_tea_temp,daemon=True).start()

print("MAin program ended")