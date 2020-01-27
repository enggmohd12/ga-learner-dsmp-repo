# --------------
##File path for the file 
file_path 
def read_file(path):
    file = open(path,"r")
    sentence = file.read()
    file.close()
    return sentence
sample_message = read_file(file_path)
print(sample_message)
#Code starts here


# --------------
#Code starts here

message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)

print(message_1)
print(message_2)

def fuse_msg(message_a,message_b):
    int_msg1 = int(message_1)
    int_msg2 = int(message_2)
    quotient = int_msg2 // int_msg1
    return str(quotient)

secret_msg_1 = fuse_msg(message_1,message_2)    
print(secret_msg_1)





# --------------
#Code starts here
message_3 = read_file(file_path_3)

print(message_3)

def substitute_msg(message_c):
    sub = (message_c == 'Red' and 'Army General') or (message_c == 'Green' and 'Data Scientist') or 'Marine Biologist'
    return sub

secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)             


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5
#Code starts here
message_4 = read_file(file_path_4)
#print(message_4)
message_5 = read_file(file_path_5)
#print(message_5)

def compare_msg(message_d,message_e):
    alist = message_d.split()
    blist = message_e.split()
    clist =[ ]
    for i in alist:
        if i not in blist:
          clist.append(i)
    final_msg = " ".join(clist)
    print(final_msg)
    print(type(final_msg))
    return str(final_msg)

secret_msg_3 = compare_msg(message_4,message_5)


# --------------
#Code starts here
message_6 = read_file(file_path_6)
print(message_6)

def extract_msg(message_f):
    alist = message_f.split()
    even_word = lambda x: (len(x)%2 == 0)
    b_list = list(filter(even_word,alist))
    final_msg = " ".join(b_list)
    print(final_msg)
    return str(final_msg)

secret_msg_4 = extract_msg(message_6)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
print(message_parts)
secret_msg = " ".join(message_parts)
print(secret_msg)

final_path= user_data_dir + '/secret_message.txt'

def write_file(secret_msg,path):
    f = open(path,'a+')
    f.write(secret_msg)
    f.close()
#Code starts here
a = write_file(secret_msg,final_path)
print(secret_msg)


