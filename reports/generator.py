import os
from datetime import datetime
import pandas as pd
from data.race_times import RACE_TIMES
from data.training_paces import TRAINING_PACES

def ensure_reports_dir():
    """Ensure the reports directory exists."""
    reports_dir = os.path.join(os.getcwd(), 'reports')
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    return reports_dir

def generate_report_filename(vdot):
    """Generate a human-readable report filename."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    return f"VDOT_{vdot}_Report_{date_str}_{time_str}.txt"

def generate_report(vdot):
    """Generate a complete training report based on VDOT and save to a file."""
    reports_dir = ensure_reports_dir()
    filename = generate_report_filename(vdot)
    filepath = os.path.join(reports_dir, filename)
    
    df_race = pd.DataFrame(RACE_TIMES)
    df_paces = pd.DataFrame(TRAINING_PACES)
    
    race_times = df_race[df_race['VDOT'] == vdot].iloc[0]
    training_paces = df_paces[df_paces['VDOT'] == vdot].iloc[0]
    
    with open(filepath, 'w') as f:
        f.write(f"VDOT Running Calculator Report\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"\nYour VDOT: {vdot}\n")
        
        # Write race predictions
        f.write("\n=== Race Time Predictions ===\n")
        for distance in ['1500m', 'Mile', '5000m', '10K', 'Marathon']:
            f.write(f"{distance}: {race_times[distance]}\n")
        
        # Write training paces
        f.write("\n=== Training Paces ===\n")
        for pace_type in ['E/L km', 'E/L mile', 'M km', 'M mile', 'T km', 'T mile']:
            f.write(f"{pace_type}: {training_paces[pace_type]}\n")
        
        # Write interval paces
        f.write("\n=== Interval Paces ===\n")
        for interval in ['I 400m', 'I km', 'I 1200m']:
            f.write(f"{interval}: {training_paces[interval]}\n")
        
        # Write repetition paces
        f.write("\n=== Repetition Paces ===\n")
        for rep in ['R 200m', 'R 300m', 'R 400m', 'R 600m', 'R 800m']:
            f.write(f"{rep}: {training_paces[rep]}\n")
    
    return filepath