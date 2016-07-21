# h = hour, m = minute
def calculateAngle(h, m):
    if m = 60:
        m = 0

    if h = 12:
        h = 0;

    degrees_per_minute = 360 / 60 = 6
    degrees_per_hour = 360 / 12 = 30

    angle_between_minute_hand_and_twelve = m * 6

    # There are five minutes between two numbers, each minute is 6 degrees.
    angle_between_two_numbers = 5 * 6 = 30

    # Minutes as fractional hours
    fractional_hours = angle_between_two_numbers = x / 60

    angle_between_hour_hand_and_twelve = degrees_per_hour * h + x * fractional_hours * angle_between_two_numbers

    # Get absolute of difference so we don't have negative numbers.
    angle = abs(angle_between_hour_hand_and_twelve - angle_between_minute_hand_and_twelve)

    # Get the smaller angle as it can be > 180.
    angle = min(360 - angle, angle)

    return angle