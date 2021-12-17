import pandas as pd
import os
from datetime import datetime

# global variable
raw_file_path = "2021_10_22_16_26_07pos.csv"
ifc_file_path = "cali_factor.csv"


def get_accumulation_time():
    df_time = df_normalization['time']
    time_ori = datetime.strptime(df_time[0], "%H:%M:%S")
    time_delta = []
    for time in df_time:
        time_now = datetime.strptime(time, "%H:%M:%S")
        time_delta.append((time_now - time_ori).seconds/60)
    df_normalization.insert(1, column="accumulation", value=time_delta)

def get_StdDev_and_Avg():
    StdDev = []
    Avg = []
    for i in range(0, 16):
        df_current_well = df_normalization[f'well_{i+1}']
        StdDev.append(df_current_well[first_time:twice_time].std())
        Avg.append(df_current_well[first_time:twice_time].mean())
    return StdDev, Avg

def normalize():
    for i in range(0, 16):
        df_current_well = df_raw[f'well_{i+1}']
        df_current_ifc = df_ifc[f'well{i+1}']
        baseline = df_current_well[first_time:twice_time].mean()
        df_normalization[f'well{i+1}'] = (df_raw[f'well_{i+1}']-baseline)/df_current_ifc[0] # normalized = (IF(t)-IF(b))/IFc

def get_ct_threshold():
    threshold_value = []
    StdDev, Avg = get_StdDev_and_Avg()
    for i in range(0, 16):
        threshold_value.append(n_sd*StdDev[i] + Avg[i])
        print(f"Well {i+1}: StdDev is {StdDev[i]}, Avg is {Avg[i]}")
    return threshold_value

def get_ct_value(threshold_value):
    Ct_value = []
    for i in range(0, 16):
        df_current_well = df_normalization[f'well_{i+1}']
        df_accumulation = df_normalization['accumulation']
        print("\n")
        print(df_current_well)
        print(f"Threshold value: {threshold_value[i]}")
        try:
            for j, row in enumerate(df_current_well):
                if row >= threshold_value[i]:
                    print(f"row: {row}")
                    thres_lower = df_current_well[j-1]
                    thres_upper = df_current_well[j]                
                    acc_time_lower = df_accumulation[j-1]
                    acc_time_upper = df_accumulation[j+1]
                    
                    # linear regression
                    x2 = acc_time_upper
                    y2 = thres_upper
                    x1 = acc_time_lower
                    y1 = thres_lower
                    y = threshold_value[i]
                    x = (x2-x1)*(y-y1)/(y2-y1)+x1

                    Ct_value.append(round(x, 2))
                    print(f"Ct of well_{i+1} is {round(x, 2)}")
                    break

                # if there is no Ct_value availible
                elif j == len(df_current_well)-1:
                    Ct_value.append(99.99)
                    print("Ct value is not available")
        except Exception as e:
            print(e)
            Ct_value.append(99.99)
            print("Ct value is not available")

    return Ct_value

def ct_calculation():
    global df_raw, df_ifc, df_normalization ,first_time,twice_time,n_sd
    first_time = int(input("Input first time:   "))
    twice_time = int(input("Input twice time:   "))
    n_sd = int(input("Input Std:   "))   
    df_raw = pd.read_csv(raw_file_path)
    df_ifc = pd.read_csv(ifc_file_path)
    df_normalization = df_raw.copy()

    get_accumulation_time()
    normalize()
    threshold_value = get_ct_threshold()
    Ct_value = get_ct_value(threshold_value)
    print(Ct_value)
    save_excel = pd.DataFrame({"well_1":[Ct_value[0]],"well_2":[Ct_value[1]],"well_3":[Ct_value[2]],"well_4":[Ct_value[3]],
                               "well_5":[Ct_value[4]],"well_6":[Ct_value[5]],"well_7":[Ct_value[6]],"well_8":[Ct_value[7]],
                               "well_9":[Ct_value[8]],"well_10":[Ct_value[9]],"well_11":[Ct_value[10]],"well_4":[Ct_value[11]],
                               "well_13":[Ct_value[12]],"well_14":[Ct_value[13]],"well_15":[Ct_value[14]],"well_16":[Ct_value[15]]}
    ,index=["CT_Value"])
    save_excel.to_excel("CT_Value.xlsx",encoding= "utf_8_sig")
    return Ct_value

def main():
    ct_calculation()
if __name__ == '__main__':
    main()
    
