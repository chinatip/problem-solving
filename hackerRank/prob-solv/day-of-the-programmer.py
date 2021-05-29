
import calendar

def dayOfProgrammer(year):
    return "12.09." + str(year) if calendar.isleap(year) else "13.09." + str(year)
