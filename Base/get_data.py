import os,yaml

from rootpath import rootpath

def get_data_2_list(filename,listname):
    filepath = rootpath+os.sep+"Data"+os.sep+filename+".yml"
    print(filepath)
    with open(filepath,'r',encoding='utf-8') as f:
        data= yaml.load(f)[listname]

    #此处返回一个字典，并且有多余的nub1 键数据，而paratrimeze需要的参数是一个列表
    data_list=[]
    for i in data.values():
        data_list.append(i)
    return data_list

if __name__ == '__main__':
    print(get_data_2_list("data","Login_test1"))