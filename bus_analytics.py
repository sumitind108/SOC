
import os
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker

# Function to read and concatenate CSV files in the given folder
def read_csv_files(folder_path):
    all_files = [pd.read_csv(os.path.join(folder_path, filename)) for filename in os.listdir(folder_path) if filename.endswith(".csv")]
    return pd.concat(all_files, ignore_index=True)  # Concatenate all CSV files into a single DataFrame

# Function to preprocess data and filter SOC for specified Bus IDs
def preprocess_data(data, bus_ids):
    data['can_time'] = pd.to_datetime(data['can_time'], format='%d/%m/%Y %H:%M:%S').dt.tz_localize('UTC').dt.tz_convert('Asia/Kolkata')
    data['hour'] = data['can_time'].dt.hour  # Extract hour of the day
    soc_data = data[(data['can_param'] == 'Battery SOC') & (data['vehicleid'].isin(bus_ids))].copy()  # Filter SOC data for specified Bus IDs and 'Battery SOC' parameter
    return soc_data

# Function to create a 3D plot for SOC values over time for specified buses
def create_3d_plot(ax, soc_data, bus_ids):
    soc_min = 0
    soc_max = soc_data['can_val'].max()
    soc_max_ceil = 10 * ((soc_max // 10) + 1)
    num_ticks = int((soc_max_ceil - soc_min) / 10) + 1
    
    ax.set_zticks(range(soc_min, soc_min + num_ticks * 10, 10))
    ax.zaxis.set_major_formatter(ticker.PercentFormatter())  # Set Z-axis ticks and format as percentages

    color_map = plt.cm.get_cmap('tab10', len(bus_ids))  # Set colors for each bus ID
    marker_cycle = ['o', 's', 'D', '^', 'v', '<', '>', 'p', 'P', 'h', 'H', '*']  # Set markers for each bus ID

    # Plot SOC values for specified buses
    for i, bus_id in enumerate(bus_ids):
        bus_soc_data = soc_data[soc_data['vehicleid'] == bus_id]
        maintenance_needed = bus_soc_data['can_val'].min() < 20
        ax.scatter(bus_soc_data['hour'], [bus_id] * len(bus_soc_data), bus_soc_data['can_val'], 
                   label=f'Bus ID: {bus_id} (Maintenance Needed)' if maintenance_needed else f'Bus ID: {bus_id}',
                   color=color_map(i), marker=marker_cycle[i % len(marker_cycle)], s=30)

    ax.set_ylabel('Bus ID')
    ax.set_yticks(bus_ids)
    ax.set_zlabel('SOC (%)')
    ax.set_title(f'Battery SOC Tracking for Specified Buses: {", ".join(map(str, bus_ids))}')  # Set plot labels and title
    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=2))
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:02d}:00 {}'.format(int(x) % 12 if int(x) % 12 != 0 else 12, 'AM' if int(x) < 12 else 'PM')))
    plt.xticks(rotation=45)  # Format x-axis labels as 12-hour time format and rotate them by 45 degrees
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.legend()  # Show legend
    plt.tight_layout()  # Adjust layout for better appearance
    plt.show()  # Display the plot

# Main function to execute the program
def main():
    folder_path = input("Enter the folder path containing CSV files: ")  # Prompt user for folder path
    bus_ids = input("Enter Bus IDs (comma-separated): ").split(',')
    bus_ids = [int(bus_id.strip()) for bus_id in bus_ids]  # Parse comma-separated Bus IDs

    data = read_csv_files(folder_path)  # Read and concatenate data from CSV files
    soc_data = preprocess_data(data, bus_ids)  # Preprocess data and filter SOC for specified Bus IDs

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    create_3d_plot(ax, soc_data, bus_ids)  # Create 3D plot for SOC values over time for specified buses

# Check if the script is run directly and call the main function
if __name__ == "__main__":
    main()
