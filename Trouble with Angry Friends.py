'''Question : There are two friends jhon and smith, and the parameters j_angry and s_angry
             to indicate if each is angry.you are in trouble if both of them are angry or
             no one of them is angry'''

s_angry=input("Is smith angry? say yes or no: ")
j_angry=input("Is jhon angry? say yes or no: ")
def angr(s_angry,j_angry):
    if(s_angry==j_angry):
        print("Trouble")
    elif(s_angry!='yes' and j_angry!='yes'):
        print("Trouble")
    else:
        print("Not in trouble")
    
angr(s_angry,j_angry)