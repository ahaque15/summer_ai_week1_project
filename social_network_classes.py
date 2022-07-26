# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        self.list_of_friends = []
        self.list_of_blocked = []
        self.messages = []
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here
        print("Creating ...")
        pass

    def add_friends(self, user):
        new_Friend = input("Friend to be added? ")
        user.addFriend(new_Friend)
        print("Your friend " + new_Friend + " has been added!")


    def view_friends(self, user):

        print(user.self.list_of_friends)
    

    
    #complete
    def block_person(self, recipient):

        recipient = input("Who would you like to block? ")
        self.list_of_blocked.append(recipient)
        print("You have blocked", recipient)

    #complete
    def add_friends(self, recipient):

        recipient = input("Who would you like to add as a friend? ")
        self.list_of_friends.append(recipient)
        print("You have added", recipient, "as a friend")



        

class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.messages = []

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        pass

    def send_message(self):
        message = input("What message would you like to send? ")
        recipient = input("Who would you like to send the message to? ")
        #implement sending message to friend here
        recipient.messages.append(message)
        pass