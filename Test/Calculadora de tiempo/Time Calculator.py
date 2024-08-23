def add_time(start, duration, starting_day=None):
    # Helper function to convert 12-hour format to 24-hour format
    def convert_to_24_hour(time_str):
        time, meridiem = time_str.split()
        hours, minutes = map(int, time.split(':'))
        if meridiem == 'PM' and hours != 12:
            hours += 12
        if meridiem == 'AM' and hours == 12:
            hours = 0
        return hours, minutes

    # Helper function to convert 24-hour format back to 12-hour format
    def convert_to_12_hour(hours, minutes):
        meridiem = 'AM' if hours < 12 else 'PM'
        hours = hours % 12
        if hours == 0:
            hours = 12
        return f"{hours}:{minutes:02d} {meridiem}"

    # Days of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse the start time and duration
    start_hours, start_minutes = convert_to_24_hour(start)
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculate the new time
    end_minutes = start_minutes + duration_minutes
    extra_hours = end_minutes // 60
    end_minutes = end_minutes % 60

    end_hours = start_hours + duration_hours + extra_hours
    extra_days = end_hours // 24
    end_hours = end_hours % 24

    # Convert the end time back to 12-hour format
    new_time = convert_to_12_hour(end_hours, end_minutes)

    # Calculate the new day of the week if provided
    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (starting_day_index + extra_days) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    # Add the number of days later if applicable
    if extra_days == 1:
        new_time += " (next day)"
    elif extra_days > 1:
        new_time += f" ({extra_days} days later)"

    return new_time