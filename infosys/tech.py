#PF-Tryout
def generate_schedule(module_list,duration_list,start_date):
    date = start_date.split("-")
    day = int(date[0])   
    for i in range(len(module_list)):
        for j in range(i+1):

            if i==j:
                if duration_list[j]<10:
                    print("{0} - Start Date: {1} End Date: {2}".format(module_list[i], start_date, "0"+str((day)+(duration_list[j]-1))+"-"+"03"+"-"+"2016"))
                else:
                    print("-1")
                    

    
module_list=["PF","OOP"]
duration_list=[7,8]
start_date="01-03-2016"
generate_schedule(module_list, duration_list, start_date)