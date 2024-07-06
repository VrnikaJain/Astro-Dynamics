from datetime import datetime, timedelta

def calculate_launch_window(departure_date, target_date, launch_window_days=7):
    """
    Calculate the optimal launch window for a mission.
    
    Parameters:
    departure_date (datetime): Desired departure date
    target_date (datetime): Desired target date
    launch_window_days (int): Duration of the launch window in days
    
    Returns:
    tuple: Start and end date of the launch window
    """
    launch_window_start = departure_date - timedelta(days=launch_window_days // 2)
    launch_window_end = departure_date + timedelta(days=launch_window_days // 2)
    
    return launch_window_start, launch_window_end

if __name__ == "__main__":
    departure_date = datetime(2024, 7, 20)
    target_date = datetime(2024, 8, 15)
    
    launch_window_start, launch_window_end = calculate_launch_window(departure_date, target_date)
    print(f"Launch window: {launch_window_start} to {launch_window_end}")
