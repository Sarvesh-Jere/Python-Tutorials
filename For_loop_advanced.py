from loguru import logger

count = 0

#We have to count the number of the in the below paragraph


paragraph = """Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
data warehouse and business intelligence industry’s thought leader on the dimen
sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
books written by Ralph and his colleagues have been the industry’s best sellers 
since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
coinvented the Star workstation, the fi rst commercial product with windows, icons, 
and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
electrical engineering from Stanford University"""

paragraph_list = paragraph.lower().split(" ")

print(paragraph_list)

for letter in paragraph_list:
    if letter == "the":
        count = count +1



logger.info(f"Total count of the is {count}")

# But this only counts the number of "the", not "The", therefore convert into lowercase first


