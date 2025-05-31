# Daniel's Training Paces Calculator

A personal VDOT-based running calculator that converts race times into training paces and race predictions, based on Jack Daniels' proven training methodology.

## 🏃‍♂️ What is VDOT?

VDOT (V̇O₂ max with a Dot) is a running performance metric developed by renowned coach Jack Daniels. It represents your current running fitness level and is used to:

- **Calculate optimal training paces** for different workout types
- **Predict race times** across various distances
- **Ensure proper training intensity** to maximize improvement while minimizing injury risk
- **Track fitness progress** over time through consistent pace-based training

Unlike raw V̇O₂ max, VDOT accounts for running economy, making it a more practical measure for determining training paces.

## ✨ Features

- **Race Time Analysis**: Convert any recent race performance into a VDOT score
- **Training Pace Calculation**: Get precise paces for:
  - Easy/Long runs (E/L)
  - Marathon pace (M)
  - Threshold runs (T)
  - Interval training (I)
  - Repetition workouts (R)
- **Race Predictions**: Estimate times for 1500m, Mile, 5K, 10K, and Marathon
- **Automated Reports**: Generate detailed training reports saved as text files
- **Flexible Input**: Accepts multiple distance and time formats

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Quick Setup

1. **Clone or download** this repository to your local machine

2. **Navigate** to the project directory:
   ```bash
   cd daniels-training-paces
   ```

3. **(Recommended) Create a virtual environment**:
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Verify installation**:
   ```bash
   python main.py
   ```

## 📖 Usage

### Running the Calculator

Execute the main script and follow the interactive prompts:

```bash
python main.py
```

### Example Session

```
VDOT Running Calculator
Enter a recent race time and distance to calculate your VDOT and training paces.

Choose race distance (e.g., 5K, 10K, Marathon): 5K
Enter your time for 5K (format MM:SS or HH:MM:SS): 22:30

Report generated successfully!
Location: reports/VDOT_46_Report_2025-05-31_16-30-15.txt
```

### Supported Input Formats

#### Race Distances
- **1500m**: `1500`, `1500m`, `1.5k`
- **Mile**: `mile`, `mi`, `1 mile`
- **5000m**: `5000`, `5000m`, `5k`, `5km`
- **10K**: `10k`, `10km`, `10000`, `10000m`
- **Marathon**: `marathon`, `42k`, `42.2k`, `26.2mi`

#### Time Formats
- **Short distances**: `MM:SS` (e.g., `22:30` for 22 minutes 30 seconds)
- **Long distances**: `HH:MM:SS` (e.g., `3:45:20` for 3 hours 45 minutes 20 seconds)

## 📊 Sample Output

After entering your race data, the calculator generates a comprehensive report:

```
VDOT Running Calculator Report
Generated on: 2025-05-31 16:30:15

Your VDOT: 46

=== Race Time Predictions ===
1500m: 5:42
Mile: 6:10
5000m: 20:35
10K: 42:51
Marathon: 3:10:45

=== Training Paces ===
E/L km: 5:15-5:50
E/L mile: 8:27-9:23
M km: 4:32
M mile: 7:18
T km: 4:08
T mile: 6:40

=== Interval Paces ===
I 400m: 1:35
I km: 4:02
I 1200m: 4:50

=== Repetition Paces ===
R 200m: 45
R 300m: 68
R 400m: 1:31
R 600m: 2:18
R 800m: 3:05
```

## 📁 Project Structure

```
daniels-training-paces/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This documentation
├── data/
│   ├── race_times.py      # VDOT race time lookup tables
│   └── training_paces.py  # VDOT training pace lookup tables
├── utils/
│   ├── converters.py      # Time format conversion utilities
│   └── normalizers.py     # Distance input normalization
└── reports/               # Generated training reports
    └── *.txt             # Individual VDOT reports
```

### Key Components

- **[`VDOTCalculator`](main.py)**: Core class that processes race data and finds corresponding VDOT
- **[`generate_report()`](reports/generator.py)**: Creates comprehensive training reports
- **[`normalize_distance()`](utils/normalizers.py)**: Handles various distance input formats
- **[`time_to_seconds()`](utils/converters.py)**: Converts time strings to seconds for calculations

## 🔧 Technical Details

### Algorithm Overview

1. **Input Processing**: User race time and distance are normalized and converted to seconds
2. **VDOT Lookup**: The closest matching VDOT is found by comparing against Jack Daniels' race time tables
3. **Pace Calculation**: Training paces are retrieved from corresponding VDOT training tables
4. **Report Generation**: All data is formatted and saved to a timestamped text file

### Data Sources

The calculator uses Jack Daniels' established VDOT tables for:
- Race time equivalencies across distances
- Training pace recommendations for each VDOT level
- Interval and repetition pace guidelines

## 💡 Training Pace Guide

- **Easy/Long (E/L)**: Conversational pace for base building and recovery
- **Marathon (M)**: Sustainable pace for marathon racing and tempo runs
- **Threshold (T)**: Comfortably hard pace for lactate threshold development
- **Interval (I)**: Hard pace for V̇O₂ max development (3-5 minute intervals)
- **Repetition (R)**: Very fast pace for speed and neuromuscular development

## 🔍 Troubleshooting

### Common Issues

**"Invalid distance" error**:
- Ensure you're using supported distance formats (see Input Formats section)
- Try alternative formats (e.g., `5K` instead of `5000m`)

**Time format errors**:
- Use `MM:SS` for times under 1 hour
- Use `HH:MM:SS` for longer times
- Avoid extra characters or spaces

**Missing reports**:
- Check that the `reports/` directory exists
- Verify write permissions in the project directory

## 🚀 Future Enhancements

- **Web Interface**: Browser-based calculator for easier access
- **Training Plan Integration**: Generate weekly training schedules
- **Progress Tracking**: Store and compare VDOT improvements over time
- **Additional Distances**: Support for 800m, Half Marathon, and Ultra distances
- **Export Options**: CSV and PDF report formats
- **Mobile App**: iOS/Android companion application

## 📝 Notes

This calculator is designed for personal training use and implements Jack Daniels' VDOT methodology as described in "Daniels' Running Formula." For best results:

- Use recent race times (within 6-8 weeks)
- Choose races where you gave maximum effort
- Consider environmental conditions that may have affected performance
- Adjust paces based on terrain, weather, and personal response to training

---

*Happy training! 🏃‍♂️💨*