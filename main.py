import pandas as pd
import numpy as np
import math

#read .csv file
def read_csv(path):
    persons_a = []
    persons_b = []
    data_frame=pd.read_csv(path, sep=";")

    persons_U = data_frame.iloc[0:20,1:9]
    persons_U = persons_U.fillna(0)
    persons_U = persons_U.replace(' ', 0)
    persons_U = persons_U.astype(int)
    persons_U = pd.concat([persons_U, data_frame.iloc[0:20,0:1]], axis=1)
    persons_U.set_index("USERS", inplace=True)
    # print(persons_U)

    persons_a = data_frame.iloc[0:20,1:9]
    persons_a = persons_a.replace(' ',0)
    persons_a = persons_a.fillna(0)
    persons_a = persons_a.astype(int)
    persons_a_numpy = persons_a.values

    # print(persons_a_numpy)
    # print("")

    persons_NU = data_frame.iloc[21:26,1:9]
    persons_NU = persons_NU.fillna(0)
    persons_NU = persons_NU.replace(' ', 0)
    persons_NU = persons_NU.astype(int)
    persons_NU = pd.concat([persons_NU, data_frame.iloc[21:26,0:1]], axis=1)
    persons_NU.set_index("USERS", inplace=True)
    # print(persons_NU)
    persons_b = data_frame.iloc[21:26,1:9]
    persons_b = persons_b.replace(' ',0)
    persons_b = persons_b.fillna(0)
    persons_b = persons_b.astype(int)
    persons_b_numpy = persons_b.values
    
    # print(persons_b_numpy)
    # print(type(persons_b_numpy))

    return persons_a_numpy, persons_b_numpy, persons_U, persons_NU   
    

#similarty of each person
def sim(a_person,b_person):
    sim_matrix = []
    for k in range(np.shape(b_person)[0]):
        # print("k:" ,k)
        b_person_row = b_person[k, :]
        r_b = b_person_row.mean()
        #print("b ort:" ,r_b)
        temp = []
        for i in range(np.shape(a_person)[0]):
            #print("i:" ,i)
            sum = 0
            sum_pow_a = 0
            sum_pow_b = 0
            a_person_row = a_person[i, :]
            r_a = a_person_row.mean()
            #print("a ort:" ,r_a)
            #print(a_person_row)
            for j , l in zip(a_person_row , b_person_row):
                r_ap = j
                r_bp = l
                if (not r_bp == 0) and (not r_ap == 0):
                    sum = sum + ((r_ap - r_a) * (r_bp - r_b))
                    sum_pow_a = sum_pow_a + pow((r_ap - r_a),2)  
                    sum_pow_b = sum_pow_b + pow((r_bp - r_b),2) 
            result = sum / (math.sqrt(sum_pow_a) * math.sqrt(sum_pow_b))
            temp.append(result)
        sim_matrix.append(temp)
    sim_matrix = np.asarray(sim_matrix)
    # print(sim_matrix)
    # print(type(sim_matrix))
    return sim_matrix

def n_sim(k, sim_matrix):
    df =  pd.DataFrame(sim_matrix,index=['NU1','NU2','NU3','NU4','NU5'],columns=['U1','U2','U3','U4','U5','U6','U7','U8',
    'U9','U10','U11','U12','U13','U14','U15','U16','U17','U18','U19','U20'])
    
    NU_dict = {
        "NU1":['NU1', 0],
        "NU2":['NU2', 1],
        "NU3":['NU3', 2],
        "NU4":['NU4', 3],
        "NU5":['NU5', 4]
        }  

    df_sorted_NU1 = df.sort_values(by=['NU1'],axis=1,ascending=False)
    NU1 = df_sorted_NU1.iloc[0, 0:k]
    df_sorted_NU2 = df.sort_values(by=['NU2'],axis=1,ascending=False)
    NU2 = df_sorted_NU2.iloc[1, 0:k]
    df_sorted_NU3 = df.sort_values(by=['NU3'],axis=1,ascending=False)
    NU3 = df_sorted_NU3.iloc[2, 0:k]
    df_sorted_NU4 = df.sort_values(by=['NU4'],axis=1,ascending=False)
    NU4 = df_sorted_NU4.iloc[3, 0:k]
    df_sorted_NU5 = df.sort_values(by=['NU5'],axis=1,ascending=False)
    NU5 = df_sorted_NU5.iloc[4, 0:k]
    # print(NU1,"\n",NU2,"\n",NU3,"\n",NU4,"\n",NU5)
    df_NU =  pd.concat([NU1,NU2,NU3,NU4,NU5], axis=1)
    return df_NU

def pred(persons_U, persons_NU, df_NU):
    temp = pd.DataFrame(persons_U.mean(axis=1))
    temp.columns = ['mean']
    persons_U = pd.concat([persons_U, temp],axis=1)
    
    temp = pd.DataFrame(persons_NU.mean(axis=1))
    temp.columns = ['mean']
    persons_NU = pd.concat([persons_NU, temp],axis=1)

    result = {}
    for key in df_NU:
        result[key] = []
        for book in persons_NU:
            r_NU = persons_NU['mean'].get(key)
            div = 0
            up = 0
            if persons_NU[book].get(key) == 0:
                for key_value, value_value in df_NU[key].iteritems():
                    if not pd.isna(df_NU[key][key_value]):
                        rb_U = persons_U['mean'].get(key_value)
                        rp_U = persons_U[book].get(key_value)
                        similarity = df_NU[key][key_value]
                        # print(similarity)
                        div += abs(similarity)
                        up += similarity * (rp_U - rb_U)
                        
                r_NU += up / div
                result[key].append({"book_name" : book, "point" : r_NU})
    return result
       
def calc_maxPoint(pred):
    for key, value in pred.items():
        max = -999
        max_book_name = ""
        for book_info in value:
            if book_info["point"] > max:
                max = book_info["point"]
                max_book_name = book_info["book_name"]
        display(key, max_book_name, max)

def display(key, book_name, point):
    print("")
    print(key, ":")
    print(book_name, ":", point)


PATH = "RecomendationDataSet.csv"
persons_a_numpy, persons_b_numpy, persons_U, persons_NU= read_csv(PATH)
sim_matrix = sim(persons_a_numpy,persons_b_numpy)
df_NU = n_sim(3, sim_matrix)
result = pred(persons_U, persons_NU, df_NU)
calc_maxPoint(result)
