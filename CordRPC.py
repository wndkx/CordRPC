import json
import pypresence
import pyfiglet
import colorama
import time
import sys
if __name__ == "__main__":
    colorama.init()
    print(pyfiglet.figlet_format("CordRPC", "standard"))
    try:
        config = json.loads(open("config.json", "r").read())
        start = int(time.time())
        RPC = pypresence.Presence(config["client_id"])
        RPC.connect()
        while True:
            print("Polling \n")
            RPC.update(
                large_image=config["large_image"],
                large_text=config["large_text"],
                details=config["details"],
                state=config["state"],
                start=start,
                buttons=config["buttons"]
            )
            time.sleep(config["update_time"])
    except FileNotFoundError:
        print(f"{colorama.Fore.RED}cordrpc: Could not find config.json.")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(f"{colorama.Fore.RED}cordrpc: {str(e)}")