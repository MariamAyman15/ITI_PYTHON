#create dict
my_dict = {
"s1":0 ,
"s2":0 ,
"s3":0
}
#get the sensors values from the user
s1 = input("1st sensor value")
s2 = input("2nd sensor value")
s3 = input("3rd sensor value")
#create list
my_list = [s1,s2,s3]
#print my_list
print(my_list)
#create my_tuple
my_tuple = (s1,s2,s3)
#print my_tuple
print(my_tuple)
#edit my_dict value
my_dict["s1"] = s1
my_dict["s2"] = s2
my_dict["s3"] = s3
#print my_dict
print(my_dict)