# # method 1:  opening up a file
# # through this method we need to close the file once we are done using it else it can result in slowing down your processor
#
# file = open ("my_file.txt")
# content = file.read()
# print(content)
# file.close()




# # method 2:  writing into a file
# # by default our mode is set to "r" i.e. read only mode, hence "w" is for mode = write
#
# file = open ("my_file.txt", mode="w")
# file.write("New text!!")
# file.close()                    # new text appear in the file




# method 3:  appending into a file
# to append , set mode = "a"
#
# file = open ("my_file.txt", mode="a")
# file.write("\nNew text!!")
# file.close()




""" ********************----------- WITH KEYWORD ---------*********************** """


# # Method 1: opening up a file using 'with'
# # bcoz it's kind of hard to remember to close a file hence we use 'with' keyword
#
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)





# # Method 2: writing into a file using 'with'
# # by default our mode is set to "r" i.e. read only mode, hence "w" represents write mode
#
# with open("my_file.txt", mode="w") as file:
#     file.write("New text!!!!!")




# # Method 3: appending into a file using 'with'
# # by default our mode is set to "r" i.e. read only mode, hence "a" represents append mode
#
# with open("my_file.txt", mode="a") as file:
#     file.write("\n\nNew text!!!!!")



""" Note: when you try to open a file in weite mode and that file doesn't exist then its going to actually create it for
 you from scratch """

# with open("new_file.txt", mode="w") as file:
#     file.write("\n\nNew text!!!!!")                 # new file created