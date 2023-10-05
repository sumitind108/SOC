# Battery SOC Tracking for Fleet Buses

## Overview:
This Python script offers a robust solution for analyzing Battery State of Charge (SOC) data within a fleet of buses. It simplifies the process of reading, processing, and visualizing SOC data from CSV files. By generating a 3D plot, the script provides a clear representation of SOC fluctuations over time for user-specified buses.

## Key Features:
- **Effortless Data Processing:** Seamlessly reads SOC data from CSV files within the specified folder.
  
- **Timestamp Conversion:** Converts timestamps to the local time zone (Asia/Kolkata) for precise data representation.
  
- **Customizable Analysis:** Filters SOC data for specific Bus IDs, enabling focused analysis on chosen vehicles.   
  
- **Visual Insights:** Generates an intuitive 3D plot, utilizing unique colors and markers for each bus, offering a quick overview of SOC trends.

## How to Use:
### 1. Run the Script:
   - Execute the script in your Python environment.
  
### 2. Input Data:
   - Enter the folder path containing SOC data CSV files when prompted.
   - Provide a comma-separated list of Bus IDs for targeted analysis.
  
### 3. Interactive Output:
   - The script dynamically generates a 3D plot showcasing SOC variations over time for the specified buses.
   - Each bus is distinctly colored and shaped for easy identification.
   - Buses with SOC below 20% are highlighted, indicating potential maintenance requirements.

## Sample Usage:
- **Input:**
   - **Folder Path:** `./data`
   - **Bus IDs:** `37673,37676,37675,37649,37699,37687,37654,37700,37659,37681,37669,37653,37671,37637`
  


## Requirements:
- **Python 3.x**
- **Pandas**
- **Matplotlib**
