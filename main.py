channels = []
class Channel:
    def __init__(self, Channel_title, Channel_desc, Channel_url): #init method to initialize the object   
        self.Channel_title = Channel_title
        self.Channel_desc = Channel_desc
        self.Channel_url = Channel_url
    
    def Display(self): #method to display the object
        print("Channel Name: ", self.Channel_title, "\nChannel Description: ", self.Channel_desc, "\nChannel_url: ", self.Channel_url)

    @staticmethod
    def Add_Channel(): #method to add new channel by user input
        print("Enter the name of channel")
        Channel_title = input()
        print("Enter the description of channel")
        Channel_desc = input()
        print("Enter the url of channel")
        Channel_url = input()
        c1 = Channel(Channel_title, Channel_desc, Channel_url) #create the new channel
        channels.append(c1) #add the new channel to the list
        return c1
        
    @staticmethod
    def remove_channel(): #method to remove channel by name
        print("Enter the name of channel to remove")
        name = input()
        for item in channels[:]: #loop through the list
            temp = item.Channel_title #store the name of the channel temporary to show in putput if deleted or not
            if item.Channel_title == name:
                channels.remove(item) #removing the object
                print("removed successfully: ",temp)
                return
        print(temp, "Channel not found")
    
    @staticmethod
    def Display_All():
        i = 1
        for item in channels: # loop throgh the channels copy
            print("S. No : ", i, end = " \n")
            item.Display() #calling the display method for each object
            i = i+1

    

c1 = Channel("airbnb", "online booking", "www.airbnb.com")
c2=Channel.Add_Channel()
c3=Channel.Add_Channel()
c4=Channel.Add_Channel()
channels[1].Display()
channels[2].Display()
c2.Display()
Channel.remove_channel()
Channel.Display_All()


"""
import time 
import eel 
from PIL import Image 
eel.init('Page')
eel.start('index.html',size = (300, 450), host = 'localhost', port = 8000 )

Channels = []
class Channel:
    def __init__(self, name, description, subscribers, date_created, channel_url, Channel_profile):
        self.name = name
        self.description = description
        self.subscribers = subscribers
        self.date_created = date_created
        self.channel_url = channel_url
        self.Channel_profile = Channel_profile

    def Display(self):
        print(self.name)
        print(self.description)
        print(self.subscribers)
        print(self.date_created)
        print(self.channel_url)
        image_path = ''
        try:
            img = Image.open(image_path)
            img.show()
            print("file opened")
        except FileNotFoundError:
            print("error: file not found")

    @staticmethod
    def Add_Chananel():
        print("Enter name of the Channel")
        name = input()
        print("Enter description of the Channel")
        description = input()
        print("Enter subscribers of the Channel")
        subscribers = input()
        print("Enter date_created of the Channel")
        date_created = input()
        print("Enter channel_url of the Channel")
        channel_url = input()
        print("Enter path for the Channel profile")
        Channel_profile = input()
        c1 = Channel(name, description, subscribers, date_created, channel_url, Channel_profile)
        Channels.append(c1)
        return Channels
    
    @staticmethod
    def remove_channel(name):
        for item in Channels[:]:
            if item.name == name:
                Channels.remove(item)



Channel.Add_Chananel()
Channels[0].Display()

"""
