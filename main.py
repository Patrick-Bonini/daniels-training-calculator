import pandas as pd
from datetime import datetime
from data.race_times import RACE_TIMES
from data.training_paces import TRAINING_PACES
from utils.converters import time_to_seconds
from utils.normalizers import normalize_distance
from reports.generator import generate_report

class VDOTCalculator:
    def __init__(self):
        self.df_race = pd.DataFrame(RACE_TIMES)
        self.df_paces = pd.DataFrame(TRAINING_PACES)
    
    def find_vdot(self, race_time, race_distance):
        """Find the closest VDOT based on race time and distance."""
        normalized_dist = normalize_distance(race_distance)
        if not normalized_dist:
            return None
        
        race_time_sec = time_to_seconds(race_time)
        self.df_race[normalized_dist + '_sec'] = self.df_race[normalized_dist].apply(time_to_seconds)
        self.df_race['diff'] = abs(self.df_race[normalized_dist + '_sec'] - race_time_sec)
        closest_row = self.df_race.loc[self.df_race['diff'].idxmin()]
        return closest_row['VDOT']

def main():
    print("VDOT Running Calculator")
    print("Enter a recent race time and distance to calculate your VDOT and training paces.")
    
    calculator = VDOTCalculator()
    
    race_distance = input("Choose race distance (e.g., 5K, 10K, Marathon): ").strip()
    race_time = input(f"Enter your time for {race_distance} (format MM:SS or HH:MM:SS): ").strip()
    
    vdot = calculator.find_vdot(race_time, race_distance)
    if vdot is None:
        print("Invalid distance. Please try formats like: 5K, 10K, Marathon, 1500m, Mile")
        return
    
    report_path = generate_report(vdot)
    print(f"\nReport generated successfully!")
    print(f"Location: {report_path}")

if __name__ == "__main__":
    main()