"""
Music Recommendation System - Rishikesh Yadav [CWID: 20007668]
"""
#Pledge: I pledge my honor that I have abided by the Stevens Honor System.

from pathlib import Path

#................GLOBAL VARIABLES......................#
FILE = "musicrecplus.txt"

#................HELPER FUNCTIONS......................#
def read_preferences(filename):
    """
    read_preferences() function is a helper function that performs the following tasks:
        1. It reads the input file and converts it into a dictionary where the user name is a key and its value is the list of user preferences.
	2. It returns the above created dictionary as output.
    """
    dic = {}
    with open(filename, "r") as f:
        for line in f:
            [username, singers] = line.strip().split(":")
            singersList = singers.split(",")
            dic[username] = singersList
    return dic

def listCheck(list1, list2):
    """
    listCheck() function is a helper function that performs the following tasks:
        1. It checks if the second list is a subset of the first list of the two input lists.
    """
    flag = True
    for item in list2:
        if item not in list1:
            flag = False
            break
    return flag

def numMatches(userPrefs, storedUserPrefs):
    """
    numMatches() function is a helper function that performs the following tasks:
        1. It returns the number of matching preferences from the two input preference lists.
    """
    count = 0
    for item in userPrefs:
        if item in storedUserPrefs:
            count += 1
    return count

def finalRecCal(list1, list2):
    """
    finalRecCal() function is a helper function that performs the following tasks:
        1. It extracts the preferences to recommend from the preferences of the most matched user.
    """
    output = []
    for item in list2:
        if item not in list1 and item not in output:
            output.append(item)
    return output

def find_individual_artist_count(doc):
    """
    find_individual_artist_count() function is a helper function takes in the dictionary with the key value pair with
    the artist and performs the following functions:
        1. It takes in the dictionary and appends a list of all the artists in the dictionary
        2. It creates a new dictionary with the artist as the key and the count as the value.
        3. If the artist is already in the dictionary, it increments the count by 1.
    """
    newDict ={}
    newList = []
    if(doc):
        for key in doc:
            if(key[-1] == '$'):
             continue
            else:
                newList.append(doc[key])
        for i in newList:
         for j in i:
            if j not in newDict:
                newDict[j] = 1
            else:
                newDict[j] += 1
        return newDict
    else:
        return False

def artist_helper_func(users):
    """
    artist_helper_func() function is a helper function that performs the following functions:
        1. It takes in the dictionary with the key as the artist and the value as the count and checks if the 
        dictionary is empty or not.
        2. If the dictionary is not empty, it sorts the dictionary based on the value and returns the sorted
        dictionary in decending order.
        3. If the dictionary is empty, it returns false.
    """
    sortedDict = {}
    sortedDict = find_individual_artist_count(users);
    #print(sortedDict)
    if(sortedDict):
        sorted_artist = dict(sorted(sortedDict.items(),key = lambda kv: kv[1],reverse=True))
        return sorted_artist;
    else:
        return False

#................PROGRAM FEATURE FUNCTIONS.....................#
def greetings():
    """
    greetings() function is a main feature function that performs the following tasks:
        1. It prints the music recommendation system menu for the user.
    """
    print()
    print("Enter a letter to choose an option :")
    print("e - Enter preferences")
    print("r - Get recommendations")
    print("p - Show most popular artists")
    print("h - How popular is the most popular")
    print("m - Which user has the most likes")
    print("s - Show Preferences")
    print("d - Delete Preferences")
    print("q - Save and quit")
    
def addPreferences(user, users):
    """
    addPreferences() function is a main feature function that performs the following tasks:
        1. It takes input preferences from the user.
	2. If the user is adding preferences for the first time, it will create a new record for the user in the database.
	3. If the user already exists, it will append the input preferences to the existing user preferences.
    """
    List = []
    if user in users:
        List = users[user]
    while True:
        pref = input("Enter an artist that you like(Enter to Finish): ")
        if len(pref) > 0:
            for key in List:
                if key == pref:
                    continue
            List.append(pref)
        else:
            break
    return List

def getRecommendations(user, users):
    """
    getRecommendations() function is a main feature function that performs the following tasks:
        1. It checks if the user has any preferences stored.
	2. It compares the user preferences with all non private user preferences and finds most matching user.
	3. It also ensures the most matched user preferences are not a subset of the current user preferences.
	4. It displays the other artists from the most matched user as recommendations.
        5. It dispays the recommendations one per line.
	6. If the user does not have any recommendations stored, it first asks the user to add some preferences.
	7. If there are no preferences available for recommendation, the user is told "No recommendations available at this time".
    """
    count = 0
    recommender = ''
    if user not in users.keys():
        print(user + ", could you please provide your preferences first so that we can give recommendations.")
        return
    else:
        pref = users[user]
        for key in users.keys():
            if key == user:
                continue
            elif key[-1] == '$':
                continue
            else:
                temp = numMatches(pref, users[key])
                if temp > count:
                    if users[user] == users[key] or listCheck(users[user], users[key]):
                        continue
                    count = temp
                    recommender = key
        if count == 0:
            print("No recommendations available at this time.")
        else:
            recommendations = finalRecCal(users[user], users[recommender])
            if len(recommendations) > 0:
                for item in recommendations:
                    print(item)
            else:
                print("No recommendations available at this time.")
        return

    
def show_most_popular_artist(artists):
    """
    show_most_popular_artist() function is a main feature function that performs the following functions:
        1. It calls the helper function to get the sorted dictionary.
        2. If the dictionary is not empty, it calls the helper function and stores all the keys in a list.
        3. It prints the first three keys in the list.
        4. If the dictionary is empty, it prints the message "Sorry , no artists found."
    """
    sorted_artist = artist_helper_func(artists)
    if(sorted_artist):
        dictionaryKeys = list(sorted_artist.keys())
        count =0
        for name in range(len(dictionaryKeys)):
            if(count>=3):
             break
            else:
             count +=1
             print(str(count)+":"+dictionaryKeys[name])
    else:
        print("Sorry , no artists found.")

def how_popular_is_the_most_popular_artist(artists):
    """
    how_popular_is_the_most_popular_artist() function is a main feature function that performs the following functions:
        1. It calls the helper function to get the sorted dictionary.
        2. If the dictionary is not empty, it calls the helper function and stores all the values in a list.
        3. It prints the first three values in the list.
        4. If the dictionary is empty, it prints the message "Sorry , no artists found."
    """
    artist_popularity = artist_helper_func(artists)
    if(artist_popularity):
        dictionaryValues = list(artist_popularity.values())
        count =0
        for name in range(len(dictionaryValues)):
            if(name>=3):
                break
            else:
                count +=1
                print(str(count)+":"+ str(dictionaryValues[name]))
    else:
        print("Sorry , no artists found.")

def userWithMostLikes(currentUsers):
    """
    userWithMostLikes() function is a main feature function that performs the following functions:
        1. It takes the input a dictionary of the users and prints the user with most likes
        2. If the user names ends with '$', it excludes the user from the operation
        3. If multiple users exist with same number of lines, it prints all the users one at a time.
    """
    popularuser = {}
    maxLikes = 0
    for user in currentUsers:
        if user[-1] == '$':
            continue
        elif len(currentUsers[user]) > maxLikes:
            popularuser[user] =  len(currentUsers[user])
            maxLikes = len(currentUsers[user])
        elif len(currentUsers[user]) == maxLikes:
            popularuser[user] = len(currentUsers[user])
    
    if maxLikes == 0:
        print("Sorry, no user found.")
    else:
        for user in popularuser:
            if popularuser[user] == maxLikes:
                print(user)

def saveAndQuit(currentUsers, fileToBeSaved):
    """
    saveAndQuit() function is a main feature function that performs the following functions:
        1. It saves the currentUsers dictionary to the given file.
        2. It writes one item in currentUsers per one line.
    """
    file = open(fileToBeSaved, 'w')
    for user in currentUsers:
        file.write(str(user) + ':' + ','.join(currentUsers[user]) + '\n' )
    file.close()

#................EXTRA FEATURE FUNCTIONS........................#
def showPreferences(user, users):
    """
    showPreferences() function is an extra feature function that performs the following tasks:
        1. It displays all the user preferences in order.
	2. If the user does not have any preferences, it displays "You do not have any pref saved".
    """
    if user in users.keys():
        pref = users[user]
        for i in range(len(pref)):
            print(str(i+1) + ". " + pref[i])
    else:
        print("You do not have any preferences saved.")
    return
    
def deletePreference(user, users):
    """
    deletePreference() function is an extra feature function that performs the following tasks:
        1. It displays all the user preferences in order and asks the user which preference to delete.
        2. It accordingly deletes the preference based on user input.
	3. If the user does not have any preferences, it displays "You do not have any pref saved".
	4. If the user deletes their last preference, this function deletes the user record from the database.
    """
    if user in users.keys():
        pref = users[user]
        for i in range(len(pref)):
            print(str(i+1) + ". " + pref[i]) 
        key = input("Please enter the preference number to be deleted(Press anything else to return to menu): ")
        if len(key) > 0 and key.isnumeric():
            if int(key) <= len(pref):
                del pref[int(key)-1]
                if len(pref) > 0:
                    users[user] = pref
                else:
                    del users[user]
    else:
        print("You do not have any pref saved")
    return users
    

#................MAIN FUNCTION........................#
def recommendation():
    """
    recommendation() function is the main function that performs the following tasks:
        1. It takes user details and preferences, and recommends music accordingly.
        2. It puts together the entire music recommendation sytem and all its functions.
    """
    user_Details = {}
    if Path(FILE).is_file():
        user_Details = read_preferences(FILE)
    name = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    print("Welcome " + name)
    while True:
        greetings()
        option = input()
        match option:
            case 'e':
                pref = addPreferences(name, user_Details)
                if len(pref) > 0:
                    pref.sort()
                    user_Details[name] = pref
            case 'r':
                getRecommendations(name, user_Details)
            case 'p':
                show_most_popular_artist(user_Details)
            case 'h':
                how_popular_is_the_most_popular_artist(user_Details)
            case 'm':
                userWithMostLikes(user_Details)
            case 's':
                showPreferences(name, user_Details)
            case 'd':
                user_Details = deletePreference(name, user_Details)
            case 'q':
                saveAndQuit(user_Details, FILE)
                print("Thank You " + name + "!")
                print("Hope to see you soon...")
                break

if __name__ == "__main__":
    recommendation()
    

        
