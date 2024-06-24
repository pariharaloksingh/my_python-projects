# num=int(input("enter a number i will tell you it is even of odd"))
# if (num % 2 ==0):
#  print("given number is even ")
# else:
#      print("given number is odd")


# friends=["alok","abhishek","adarsh","zoro"]
# for friend in friends:
#     print(friend)
    
    
# def calcute_area(length,width):
#     area=length*width
#     return area
# print(calcute_area(5,6))


current_number=5
while current_number<=10:
    print(current_number)
    current_number+=1

def full_name(first_name,last_name):
    name=f"{first_name} {last_name}" 
    return name.title()
function_use=full_name('alok singh','parihar')   
print(function_use)

def favda(first_name,last_name):
    name=f"{first_name} {last_name}"
    return name.upper()
pura_name=favda('adarsh yadav','badmash')
print(pura_name)


uncomplete_model=['pizza','burger','momos','sandwitch']
complete_model=[]

while uncomplete_model:
    current_model=uncomplete_model.pop()
    print(f"current model is {current_model}")
    complete_model.append(current_model)
    
for completed_models in complete_model:
 print(f"completed_models are {complete_model}")
      
    
def print_models(uncomplete_model,complete_model):
    while uncomplete_model:
        current_model=uncomplete_model.pop()
        print(f"current_model is {current_model}")
        complete_model.append(current_model)
        
def show_completed_model(completed_model):
    for completed_models in completed_model:
        print(f"completed models is{completed_models}")

print_models(uncomplete_model,completed_models)             


    
 