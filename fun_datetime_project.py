from datetime import datetime, timezone,timedelta 



def timezone_conversion() :
    #Prompting user
    aware_naive = input("Is this time converter aware or naive :").strip().lower()
    #when  user wants aware date conversion
    if aware_naive == "aware":
        desired_timezone_offset = int(input("Enter the delta of desired time zone and UTC+0 :"))    
        desired_timezone = timezone(timedelta(hours = desired_timezone_offset))
        now_in_custom_timezone = datetime.now(desired_timezone)
        print(now_in_custom_timezone)

    #when user wants naive date conversion
    elif aware_naive == "naive":
        #Prompting user
        desired_timezone_offset = int(input("Enter the delta of desired time zone and UTC+0 :"))    
        current_timezone_offset = int(input("Enter the delta of current time zone and UTC+0 (default is UTC+7) :"))
        current_time_input = input("Enter current time in HH:MM:SS format (24 hours): ")

        #Convert user input to machine readable time
        current_time = datetime.strptime(current_time_input, "%H:%M:%S")
        time_difference = desired_timezone_offset - current_timezone_offset 
        if time_difference != 0 :
            converted_time = (current_time + timedelta(hours=time_difference)).strftime("%H:%M:%S")
            print(converted_time)
        else : 
            print("HEY YOU ENTERED THE SAME TIME ZONE")
    else : 
        print("typed the wrong stuff")

    

timezone_conversion()

