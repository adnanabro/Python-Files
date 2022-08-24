def add_time(start, duration, startDay = ""):
    #Now split the input values
    pieces = start.split()
    time = pieces[0].split(":")
    ampm = pieces[1]

    if ampm == "PM":
        hour = int(time[0]) + 12
        time[0] = str(hour)

    #Split duration into hours and minutes
    dur_time = duration.split(":")

    #Now add the corresponding values
    new_hour = int(time[0]) + int(dur_time[0])
    new_mint = int(time[1]) + int(dur_time[1]) 

    if new_mint >= 60:
        ah = new_mint // 60
        new_mint -= ah*60
        new_hour += ah

    days_add = 0
    if new_hour > 24:
        days_add = new_hour // 24
        new_hour -= days_add*24
        
        
    #converting into 12-hour format
    if new_hour > 0 and new_hour < 12:
        ampm = "AM"
    elif new_hour == 12:
        ampm = "PM"  
    elif new_hour > 12:
        ampm = "PM"
        new_hour -= 12
    else:  #new_hour == 0
        ampm = "AM"
        new_hour += 12
      
    if days_add > 0:
        if days_add == 1:
            days_later = " (next day)"
        else:
            days_later = " (" + str(days_add) + " days later)"
    else:
        days_later = ""

    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    
    if startDay :
        weeks = days_add // 7
        i = weekdays.index(startDay.lower().capitalize()) + (days_add - 7*weeks)
        if i > 6:
            i -= 7
        day = ", " + weekdays[i]
    else :
        day = ""
    
    newTime = str(new_hour) + ":" + (str(new_mint) if new_mint > 9 else ("0" + str(new_mint))) + " " + ampm + day + days_later
    
    return newTime

add_time("6:30 PM", "205:12")