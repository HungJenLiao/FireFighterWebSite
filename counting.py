import pandas as pd
import re
import json
 
def count_num(file):
    df_locations = file
    target_str = r"(\w{3})"
    context = []
    for location in df_locations:
        r1 = re.findall(target_str, location)
        # print(r1)
        if r1 == []:
            context.append("此處空白!!")
        elif r1[1] != "埔里鎮":
            context.append(r1[1])
        else:
            if len(r1) == 2:
                context.append("重新查看定位!!")
            else:
                context.append(r1[2])

    region = pd.DataFrame(data = context, columns = ["里別"]).value_counts()

    #index處理
    index = []
    i = 0
    while(i < len(region)):
        index.append(region.index[i][0])
        i = i + 1
    region.index = index
    #Series to dictionary
    region = region.to_dict()
    
    response = json.dumps(region, ensure_ascii=False)
    return response