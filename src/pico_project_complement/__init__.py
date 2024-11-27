from pico_project_complement.app import download_csv, temperature_trends
import os

__FILE_NAME = "temperature.csv"
__URL = "https://api.thingspeak.com/channels/2746470/feeds.csv"

__root_path = os.path.dirname(os.path.abspath(__file__))
__file_path = os.path.join(__root_path, __FILE_NAME)

def main() -> None:

    try:
        day = int(input("day: "))
        month = int(input("month: "))
        year = int(input("year: "))

        download_csv(__file_path, __URL, year, month, day)
        temperature_trends(__file_path, year, month, day)

    except Exception as e:
        print("Something went wrong:", e)
