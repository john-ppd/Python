#open file in write mode, a is append mode
#this code will append color_5 onto existing list
#easy to mess up writing to file
txt_file_data = open("write_to.txt","a")
txt_file_data.write("\ncolor_5 magenta")
txt_file_data.close()

#WRITE OVERWRITES TEXT FILE FROM SCRATCH
#if you write to a file that does not exist it will create the new file for you
txt_file_data = open("write_to2.txt","w")
txt_file_data.write("\ncolor_5 magenta")
txt_file_data.close()