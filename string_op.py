# can be iterated same as list 
from loguru import logger

name = "Sarvesh"
for char in name:
    print(char)

#Slicing 
print(name[:4])

#Capitalise capitalises the first letter and smalls all the other

print(name.capitalize())

#Count the number of times the letter appears

print(name.count("a"))

# We can use ordinal to find thr number of the letter as the computer percieves it, like the unicode 

print(ord("a"))

# ENds with gives true or false 

print(name.endswith("h"))

# Upper converts to upper, It is used in joins to avoid casesensitive error

print(name.upper())

#strip removes the extra space in the end or the start 

print(name.strip())

#swapcase to switch capital and small letters

print(name.swapcase())

#Most important function in string 

names = "Sarvesh Sanjay Jere the Goat"

new_name = names.split(" ")
#will return list
print(new_name)

# Assignment 
Input =str(["/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
"/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
"/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"])


lst = []

new_Input = Input.split("/")
print(new_Input)
