#PF-Prac-17
train_list=[
{"train_no":16453,"name":"Prasanti Express","from":"SBC","to":"BBS","days_of_run":['Mo','We','Th'],"sleeper_fare":600,"ac_fare": 987},
{"train_no":25627,"name":"Karnataka Express","from":"SBC","to":"DEC","days_of_run":['Su','Tu'],"sleeper_fare":1600,"ac_fare": 2500},
{"train_no":22642,"name":"Trivandrum SF Express","from":"VSKP","to":"TVM","days_of_run":['Mo','Tu','We','Th','Fr','Sa'],"sleeper_fare":800,"ac_fare": 1256},
{"train_no":22905,"name":"Okha Howrah Express","from":"ST","to":"KOAA","days_of_run":['We','Sa'],"sleeper_fare":987,"ac_fare": 2879}]


def get_train_name (train_no):
    for i in range(len(train_list)):
        if train_no==train_list[i]["train_no"]:
            return train_list[i]["name"]
            
def get_trains_for_day(day_of_run, train_list):
    trains = []
    for i in range(len(train_list)):
        if day_of_run in train_list[i]["days_of_run"]:
            trains.append(train_list[i]["train_no"])
    return trains
            
def get_total_fare(train_no,passenger_dict, train_list):
    total = 0
    for i in range(len(train_list)):
        if train_no == train_list[i]["train_no"]:
            total = passenger_dict["sleeper"]*train_list[i]["sleeper_fare"] + passenger_dict["ac"]*train_list[i]["ac_fare"]
    return total
        
    
    
print(get_train_name(22642))
print(get_trains_for_day("Mo", train_list))
print(get_total_fare(22642,{"sleeper":5, "ac":1}, train_list) )