# Write a program that displays the time for every 15 minute interval from 12:00 am to 11:45 pm. Your solution should produce the following output:
    
minute_increments = ['00','15','30','45']
hours = ['12','1','2','3','4','5','6','7','8','9','10','11']
am_pm = ['am','pm']
for meridiam in am_pm:
    for hour in hours:
        for minute in minute_increments:
            print(hour + ":" + minute + ' ' + meridiam)
    