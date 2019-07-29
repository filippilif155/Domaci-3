import json
import copy
with open("myjson.json", "r", encoding="utf-8") as json_file:
    content = json.load(json_file)
content_1 = copy.deepcopy(content)
lay_num = 0
for (count, elem) in enumerate(content_1["flight_data"]["outgoing"]):
    if "layover" not in elem:
        count_1 = count - lay_num
        try:
            del content["flight_data"]["outgoing"][count_1]["from"]["timestamp"]
            del content["flight_data"]["outgoing"][count_1]["from"]["timestamp_utc"]
            del content["flight_data"]["outgoing"][count_1]["to"]["timestamp"]
            del content["flight_data"]["outgoing"][count_1]["to"]["timestamp_utc"]
        except:
            pass
    else:
        count_1 = count - lay_num
        try:
            del content["flight_data"]["outgoing"][count_1]
            lay_num += 1
        except:

            pass
lay_num = 0
for (count, elem) in enumerate(content_1["flight_data"]["return"]):
    if "layover" not in elem:
        count_1 = count - lay_num
        try:
            del content["flight_data"]["return"][count_1]["from"]["timestamp"]
            del content["flight_data"]["return"][count_1]["from"]["timestamp_utc"]
            del content["flight_data"]["return"][count_1]["to"]["timestamp"]
            del content["flight_data"]["return"][count_1]["to"]["timestamp_utc"]
        except:
            pass
    else:
        count_1 = count - lay_num
        try:
            del content["flight_data"]["return"][count_1]
            lay_num += 1
        except:
            pass
try:
    del content["passenger_data"][0]["final_date"]
    del content["passenger_data"][0]["adult_ind"]
    del content["passenger_data"][0]["_type"]
except:
    pass
try:
    del content["_price_change"]
except:
    pass
try:
    del content["keep_alive"]
except:
    pass
name = content["flight_data"]["info"]["route"].split('|')
for (count,i) in enumerate(name):
    name[count] = i.lower().replace(' ', '_')
file_name = name[0] + "_" + name[1]
print(file_name)
with open(f"{file_name}.json", "w", encoding="utf-8") as json_file:
    json.dump(content, json_file, indent=4, ensure_ascii=False)