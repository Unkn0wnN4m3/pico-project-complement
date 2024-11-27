import requests
import pandas as pd

def download_csv(file_path: str, url: str, year: int, month: int, day: int) -> None:
    end_day = day + 1
    url = f"{url}?start={year}-{month}-{day}&end={year}-{month}-{end_day}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()


        with open(file_path, "wb") as file:
            file.write(response.content)

    except requests.exceptions.RequestException as e:
        print("Error while downloading csv:", e)


def temperature_trends(file_path: str, year: int, month: int, day: int) -> None:
    end_day = day + 1
    df = pd.read_csv(file_path)
    df["created_at"] = pd.to_datetime(df["created_at"])
    df["temperature"] = df["field1"].str.replace("C", "").astype(float)

    start_date = f"{year}-{month}-{day}"
    end_date = f"{year}-{month}-{end_day}"
    
    rango = df[(df['created_at'] >= start_date) & (df['created_at'] <= end_date)]
    
    if rango.empty:
        print("No hay datos en el rango de fechas especificado.")
        return    
    
    print("\nTendencias de temperatura:\n")
    print(f"Temperatura promedio: {rango['temperature'].mean():.2f}°C")
    print(f"Temperatura máxima: {rango['temperature'].max():.2f}°C")
    print(f"Temperatura mínima: {rango['temperature'].min():.2f}°C")
