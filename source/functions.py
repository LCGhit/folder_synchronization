import pandas as pd
import os.path
from colorama import Fore, Style
from collections import OrderedDict
import time
import math

tableMusic_df = pd.read_csv("data/tableMusic.csv", sep=(","))
playlists_df = pd.read_csv("data/playlist.csv", sep=(','))

def checkInput(query, warning):
    variable = ""
    while variable == "":
        try:
            variable = int(input(query))
        except:
            print("\033[1m WARNING: \033[0;0m" + warning)
            continue
        return variable

def song_style(theFilter):
    for i in range(0, len(theFilter), 1):
        print("\033[1m", str(i+1), "\033[0;0m ", str(theFilter[i]))
    # print("\033[1m", "0", "\033[0;0m ", "(next)")
    print("\033[1m", 0, "\033[0;0m ", "(add new style)")
    print("-------------------------------------------------------------------------")
    choice = str(checkInput("❓ What's the style? (pick number) => ", " please enter a number"))
    if choice == "0":
        new_style = addStyle()
        if new_style == "0":
            song_style(theFilter)
        else:
            return new_style
    else:
        return (theFilter[int(choice)-1])

def addMusicDatabase():
    tableMusic_df = pd.read_csv('data/tableMusic.csv')
    print("-------------------------------------------------------------------------")
    title_new_music = str(input("❓ What's the title of the song? ")).title()
    print("-------------------------------------------------------------------------")
    styles_list = refresh_styles_list()
    style_new_music = song_style(styles_list)

    type_new_music = input("❓ What's the typology? (choose an option: Band, Duo, Solo) => ").title()
    songwriter_new_music = input("❓ What's the songwriter name? ").title()
    year_new_music = checkInput("❓ what year was the song released? ", "please enter a number")
    artist_new_music = input("❓ Who's the artist? ").title()
    rating_global_new_music = checkInput("❓ What's the global rating of the song? ", "please enter a number")
    rating_user_new_music = checkInput("❓ What's your rating of the song? ", "please enter a number")

    duration_new_music = ""
    while duration_new_music == "":
        try:
            duration_new_music = input("❓ What's the duration of the song(min:sec)? ").split(":")
            minutes = int(duration_new_music[0])
            seconds = int(duration_new_music[1])
        except:
            print("\033[1m WARNING: \033[0;0mplease use the format min:sec")
            duration_new_music = ""
            continue
        duration_new_music = (minutes*60)+seconds
    id_new_music = tableMusic_df['id_music'].max() + 1  # id_music goes from 1 to x, the pandas index goes from 0 to x -1
    id_new_music = int(id_new_music)

    new_music_line_dict = {'id_music': id_new_music, 'style': style_new_music, 'type': type_new_music, 'title': title_new_music,'songwriter': songwriter_new_music, 'year': year_new_music, 'artist': artist_new_music,'rating_global': rating_global_new_music, 'rating_user': rating_user_new_music, 'duration': duration_new_music}

    # Convert the dictionary to a DataFrame
    new_music_line = pd.DataFrame([new_music_line_dict], index=[id_new_music])  # Explicitly provide the index

    # Replace append() with concat()
    newMusic = pd.concat([tableMusic_df, new_music_line], ignore_index=False)

    from colorama import Fore, Style

    print("-------------------------------------------------------------------------------------------------------------------------------")
    print(Fore.BLUE + Style.BRIGHT + "----------------------------------------------   YOUR NEW LIBRARY   -----------------------------------------------------------"+ Style.RESET_ALL)
    print(newMusic[['id_music', 'title', 'artist','style','duration']].to_markdown(index=False))
    print(Fore.BLUE + Style.BRIGHT + "💙 SUCCESS: Song added to Your Library 💙" + Style.RESET_ALL)


    newMusic.to_csv('data/tableMusic.csv', index=False)
    tableMusic_df = pd.read_csv('data/tableMusic.csv')
    return tableMusic_df  # Updated DataFrame





def refresh_styles_list():
    # read populate styles with the "styles.csv" from previous execution, if it exists
    if(os.path.isfile('data/styles.csv')):
        return (list(pd.read_csv('data/styles.csv').loc[:, "0"]))
    # otherwise extract styles from tableMusic.csv
    else:
        tm = pd.read_csv('data/tableMusic.csv')
        return (list(tm.loc[:, "style"].drop_duplicates()))

def addStyle():
    styles = refresh_styles_list()
    print("-----------------------------------------------------------------------")
    print(Fore.BLUE + Style.BRIGHT + " Current styles: " + Style.RESET_ALL + ', '.join(styles))
    new_Style = (input("❓ What new style would you like to add?\n    (press 0 to cancel)\n=> "))
    while new_Style.lower() in map(str.lower, styles) and new_Style !="0":
        print(Fore.YELLOW + Style.BRIGHT + "⚠️  The style " + new_Style + " already exists! " + Style.RESET_ALL)
        print("                                                                   ")
        new_Style = (input("❓ What new style would you like to add?\n    (press 0 to cancel)\n=>"))
    if new_Style == "0":
        print(" Operation cancelled")
    else:
        print(styles)
        styles.append(new_Style)
        styles_Df = pd.DataFrame(styles)
        # create/update styles.csv with the new style
        styles_Df.to_csv('data/styles.csv', index=False, na_rep="NAN!")
        print(f"💙 The style {new_Style} was added successfully! 💙")
    return new_Style





# get an especific playlist from a playlist_df
def getPlaylist(playlists, playListName):
    return playlists[playlists["id_playlist"] == playListName]

# formula to calculate an average
def addToAverage(average, size, value):
    return (size * average + value) / (size + 1)

def subtractFromAverage(average, size, value):
    return ((average * size) - value) / (size - 1)





def rankByStyle():
    tableMusic = pd.read_csv('data/tableMusic.csv')
    print(" Filter best songs by style")
    #print only one value using .unique. for not repeat the same result. it makes the code more clean.
    for item in list(pd.unique(tableMusic["style"])):
        print(" ", item)
    styleInput = input(" enter a music style (0 to return) => ")
    #returns the best musics from one style
    songStyle = getSongsOfStyle(tableMusic,styleInput)
    if styleInput == "0":
        return
    elif songStyle.empty:
        print("\033[1m WARNING: \033[0;0mstyle not found")
        rankByStyle()
    else:
        bestRankStyle = rankingStyle(songStyle)
        print(" Here are the best ranking "+styleInput+" songs: ")
        print(" ", bestRankStyle)





#Retrieves all the songs of a certain style
def getSongsOfStyle(tableMusic, style):
    #returns a subset of the dataframe "tableMusic"
    #with the songs of style corresponding to the argument "style"
    return tableMusic[tableMusic["style"].str.lower() == style.lower()]

# the function ranking that create a ranking of the style selected,
# if it's greater than 3, and sort in descending order.
def rankingStyle(songs):
    bestSongs = songs[songs["rating_global"] > 3]
    return bestSongs.sort_values("rating_global", ascending=False)





class IDGenerator: #Generator id class
    def __init__(self): #take id's in use
        self.last_id = 0
        self.used_ids = set()

    def generate_id(self): #new id
        self.last_id += 1
        while self.last_id in self.used_ids: #Keep generating a new ID unique
            self.last_id += 1
        self.used_ids.add(self.last_id)  #Add new ID to used IDs
        return self.last_id #Return last id created

# Instance of the IDGenerator class
id_generator = IDGenerator()

# Function to obtain ID
def get_new_id():
    return id_generator.generate_id()





# list of error codes

messages = ["INFO: Successfull execution",
                  "ERROR: Playlist not found",
                  "ERROR: Invalid rating",
                  "ERROR: Sintax error",
                  "ERROR: The specified song is already present in playlist",
                  "ERROR: The specified song was not found in the database",
                  "ERROR: The program can not be executed when the file is open. Please close the file and try again"]

successfull_execution = 0
playlist_not_found = 1
invalid_rating = 2
sintax = 3
playlist_duplicate = 4
song_not_found = 5
file_open = 6





# create list of all elements of given category used to create menu
def category_list(category, table):
    try:
        return sorted((list(table.loc[:, category].drop_duplicates())))
    except:
        print("erro")
        return

# retrieve the songs with a given filter
def filterSongs(theFilter, table, filterArray):
    selection = 0
    selectionArray = []

    # present the same menu while input is invalid
    while selection == 0:

        # select multiple elements of a column
        while(selection in range(len(filterArray))):
            filter_menu(theFilter, filterArray)
            if(selectionArray == []):
                print("\033[1m", "0", "\033[0;0m ", "(select all)")
            else:
                print("\033[1m", "0", "\033[0;0m ", "(next)")
            print(" current selection", selectionArray)
            try:
                selection = int(input("\033[5m press a number(toggle selection) => "))-1
                if selection in range(len(filterArray)):
                    if filterArray[selection] in selectionArray:
                        selectionArray.remove(filterArray[selection])
                    else:
                        selectionArray.append(filterArray[selection])
                else:
                    break
            except:
                break
        if(selection == -1):
            table.set_index(theFilter, inplace = True)
            if selectionArray != []:
                table = table.loc[selectionArray]
                print("this print \n", table)
                return table
            else:
                print(table)
                return table
        else:
            selection = 0
            print(" Invalid choice.\n")

# output menu for given filter
def filter_menu(theFilter, theArray):
    print("\n" + "\033[1m" + " FILTER " + theFilter.upper() + "\033[0;0m")
    for i in range(0, len(theArray), 1):
        print("\033[1m", str(i+1), "\033[0;0m ", str(theArray[i]))
    return len(theArray)

# "filtersList" is the array of the columns to filter; "table" is the the path to the csv file
def applyFilters(filtersList, table):
    filtered_songs = pd.read_csv(table)
    for i in range(0, len(filtersList), 1):
        try:
            filter = category_list(filtersList[i], filtered_songs)
            filtered_songs = filterSongs(filtersList[i], filtered_songs, filter)
        except Exception as e:
            print(e)
    return(filtered_songs)





def song_rating(song):
    table = pd.read_csv("data/tableMusic.csv")
    # Locate the song based on the title
    song_selected = table.loc[table['title'].str.lower() == song.lower()]
    print("song selected", song_selected)

    # Check if the song has been found
    if not song_selected.empty:
        # Display information about the song
        print(" Song information:")
        print(" ", song_selected[['title', 'style', 'year', 'artist']])

        # Prompt the user for a rating (limited to integers from 0 to 5)
        try:
            user_rating = int(input(" Enter your rating for this song (0 to 5)=> "))
            if 0 <= user_rating <= 5:
                # Update the rating in the music table
                table.loc[song_selected.index, 'rating_user'] = user_rating
                # Save the changes back to the CSV file
                table.to_csv('data/tableMusic.csv', index=False)
            else:
                print(" Please enter a number from 0 to 5.")
        except ValueError:
            print("\033[1m WARNING: \033[0;0mPlease enter an integer from 0 to 5.")

        print(f" Song {song} reviewed successfully!")





# menu to pick a playlist from a selection
def pickPlaylist(playlist_csv):
    playlists_list = sorted(list(map(str.lower, playlist_csv['id_playlist'].drop_duplicates())))
    playListName = ""
    input_message = " enter a playlist name => "
    while playListName not in playlists_list:
        print("\033[1m AVAILABLE PLAYLISTS \033[0;0m")
        for id in playlists_list:
            print(" ", id)
        playListName = input(input_message).lower()
        input_message = " \033[1m WARNING: \033[0;0minvalid input\n enter a playlist name => "
    return playListName

# the specific function addMusic, add a music from the data base to a playlist
def addMusic(playlists, songDataBase, playlist):

    playListName = playlist

    #checks if chosen playlist is in playlist file:
    playlist = getPlaylist(playlists, playListName)
    #reset the index from the playlist chosen.
    playlist.reset_index(inplace = True, drop = True)
    #variable takes the size of the playlist
    numSongs = len(playlist)
    #if it's empty the condition will return an error
    if numSongs <= 0 :
        return playlist_not_found

    #user input of the playlist
    print("you chose the playlist: ", playListName)

    #music that the user wishes to add in the playlist
    print(songDataBase.to_markdown(index=False))
    chooseMusic = input(" Enter the id of the song to add to " + playListName + " (0 to abort) => ")
    #the input of the music have to be an integer as it is being taking from the column 'id_music'. if it´s not it will return an error.
    try:
        userIdMusic = int(chooseMusic)

    except:
        print("\033[1m WARNING: \033[0;0mInvalid input")
        return

    #the input must be a number that is present in the column íd_music' and that is not already in the playlist chosen, or it will return an error.
    if ((userIdMusic < 0) or ((userIdMusic == playlist['id_music']).any())):
        print("\033[1m WARNING: \033[0;0mSong already in playlist")
        return playlist_duplicate

    if userIdMusic == 0:
        return

    if not((userIdMusic == songDataBase["id_music"]).any()):
        print("\033[1m WARNING: \033[0;0mSong not found")
        return song_not_found

    #get the current global rating of that music.
    songRating = songDataBase['rating_global'][userIdMusic == songDataBase["id_music"]].item()

    #calculate the new rating of the song and put with one decimal place.
    newAverageSongRating = addToAverage(playlist["average_rating_musics"][0], numSongs, songRating)
    newAverageSongRating = round(newAverageSongRating, 1)

    playlists["average_rating_musics"][(playlists["id_playlist"] == playListName)] = newAverageSongRating

    #create new row with the update of the informations of the average.
    newRow = [playListName, playlist["duration_playlist"][0], userIdMusic, playlist["rating_playlist"][0],
              newAverageSongRating, playlist["num_ratings"][0]]

    #insert in the dataframe playlists the new row.
    playlists.loc[len(playlists)] = newRow
    print("these are the playlists\n",playlists)
    #save the file with the new information, if not, return an error.
    try:
        playlists.to_csv("data/playlist.csv", index = False)
        playlist = getPlaylist(playlists, playListName)
        print(playlist.to_markdown(index=False))
        print("\033[1m SUCCESS: \033[0;0mSong added to playlist ", playListName)
    except:
        return file_open

    return successfull_execution





#Get the user parameters
def getUsersFilters(df): #df = tableMusic_df
    available_columns = df.columns.tolist()
    filterList = []

    while True:
        print(" Filter songs\nAvailable filters:")
        for i, column in enumerate(available_columns, start=1): #menu starts in 1
            print("\033[1m", i, "\033[0;0m ", column)
        print("\033[1m", "0", "\033[0;0m ", "(next)")

        try:
            print(f" current selection: {filterList}\n")
            choice = int(input(" Choose a filter: "))

            if choice == 0: #next
                if filterList == []:
                    print(df) # present the whole unfiltered table
                break
            elif 1 <= choice <= len(available_columns):
                selected_column = available_columns[choice - 1] #array index, value - 1
                filterList.append(selected_column) #list with parameters
                filterList = list(OrderedDict.fromkeys(filterList))
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid choice. Please enter a number.")

    print(" selected filters:", filterList)
    return filterList #return array with filters, used on apllyFilters

# "filtersList" is the array of the columns to filter, "loc_df" is the the path to the csv file
def createPlaylist(filtersList, loc_df, playlist_title):
    playlist_df = pd.read_csv('data/playlist.csv')
    tableMusic_df = pd.read_csv("data/tableMusic.csv", sep=',')
    selectedSongs_df = pd.DataFrame()
    applyFilters(filtersList, loc_df) #menu with filters

    add_playlist_df = pd.DataFrame()

    while True:
        try:
            selected_song_id = input(" Enter the id of the song to add to " + playlist_title + "(0 to finish, ENTER to reset filters): ")

            if selected_song_id == "0":
                break
            elif selected_song_id == "": #add new filters

                new_filters_list = getUsersFilters(tableMusic_df)
                applyFilters(new_filters_list, loc_df)
                # new_filtered_songs_df = applyFilters(new_filters_list, loc_df)
                continue

            else:
                selected_song = tableMusic_df[tableMusic_df['id_music'] == int(selected_song_id)] #select songs per id to add on playlist
                selectedSongs_df = pd.concat([selectedSongs_df, selected_song])

                print(f"Added song to the playlist: {playlist_title}\n{selectedSongs_df[['id_music', 'title', 'artist', 'style', 'year']].to_markdown(index=False)}\n")

        except ValueError:
            print("Invalid value. Please enter a valid song ID.")

    try:
        duration_playlist = selectedSongs_df['duration'].sum()
        print(f'Duration Playlist: {duration_playlist}')

        average_rating = "{:.1f}".format(selectedSongs_df['rating_global'].mean()) #averange rating songs in playlist

        print(f"\nYour Created Playlist: {playlist_title}\t Duration Playlist: {duration_playlist}\n{selectedSongs_df[['id_music', 'title', 'artist', 'style', 'year']].to_markdown(index=False)}")
        rating_playlist = float(input(" Rate your new playlist (1-5)? ")) #user rating playlist

        id_songs_playlist = list(set(selectedSongs_df['id_music']))

        for id_songs in id_songs_playlist: #loop for add all songs in csv file
            add_music = {'id_playlist': playlist_title, 'duration_playlist': duration_playlist,'id_music': id_songs,'rating_playlist': rating_playlist,'average_rating_musics': average_rating, 'num_ratings': '1.0'}
            playlist_manual_df = pd.DataFrame([add_music]) #dictionary to dataFrame
            add_playlist_df = pd.concat([add_playlist_df,playlist_manual_df], ignore_index=True) #concat all songs in only dataframe

        new_playlist = pd.concat([playlist_df,add_playlist_df]) #concat the new playlist with rest of playlists
        new_playlist = new_playlist.set_index('id_playlist')

        new_playlist.to_csv('data/playlist.csv') #add in csv file
        return selectedSongs_df #return the playlist
    except:
        print("\033[1m WARNING: \033[0;0mempty playlist")

# Main program
def playlistManualFun():
    name_playlist = input(" Enter a name for your playlist: ")
    tableMusic_df = pd.read_csv("data/tableMusic.csv", sep=',')
    filters_list = getUsersFilters(tableMusic_df)
    createPlaylist(filters_list, "data/tableMusic.csv", name_playlist)





def automaticPlaylist(): #automatic playlist
    while True:
        music_rating_max = tableMusic_df[(tableMusic_df['rating_global'] > 4)].sample(10) # 10 songs with rating > 4
        music_rating_min = tableMusic_df[(tableMusic_df['rating_global'] <= 4)].sample(5) # 5 songs with rating <= 4

        playlist_df = pd.concat([music_rating_max, music_rating_min])
        duration_total = playlist_df['duration'].sum() # total playlist duration

        if duration_total <= 3600: # total duration <= 60 minutes, 3600 seconds
            break

    return playlist_df # return the playlist DataFrame

def createdPlaylists():
    createdPlaylists = []  # store all created playlists
    add_playlist_df = pd.DataFrame()
    while True:
        flag = ''
        while flag != 'y':
            print("----------------------------------------------------------------------")
            flag = input("❓ Do you want to create a new automatic playlist? (Y/N) ").strip().lower()
            if flag == 'n':
                break
        if flag == 'n':
            print(Fore.YELLOW + Style.BRIGHT + "⚠️   WARNING: operation aborted" + Style.RESET_ALL)
            break
        # flag = input(" Do you want to create a new automatic playlist? (Y/N) ").strip().lower()
        # if flag != 'y':
        #     print("\033[1m WARNING: \033[0;0moperation aborted")
        #     break

        new_playlist_id = get_new_id()  # get a new unique playlist ID
        name_playlist = f'play_auto_{new_playlist_id}'  # save as play_auto and the playlist number

        play_auto = automaticPlaylist()
        play_auto['id_playlist'] = name_playlist  # assign the playlist ID

        createdPlaylists.append(play_auto) # add new playlist_auto to the list

        count_style = play_auto['style'].value_counts() #count all songs per style present in playlist

        # Add the 'duration_playlist' column to the DataFrame
        duration_playlist = play_auto['duration'].sum()
        play_auto['duration_playlist'] = duration_playlist
        duration_min_sec = str(math.floor(duration_playlist/60)) + ":" + str(duration_playlist % 60)

        average_rating = "{:.1f}".format(play_auto['rating_global'].mean()) #averange rating songs in playlist
        id_songs_playlist = list(set(play_auto['id_music'])) #list id songs present in playlist

        print("                                                                          ")
        print(Fore.BLUE + Style.BRIGHT + "💙    YOUR NEW PLAYLIST    💙" + Style.RESET_ALL)
        print("                                                                          ")
        print(f">>>>>  Playlist '{name_playlist}' created successfully! >>>> Duration: {duration_min_sec}")
        print("                                                                          ")
        print(play_auto[['id_music','title', 'rating_global', 'style', 'year']].to_markdown(index=False))
        print(f"\nDuration: {duration_min_sec}\nAverage Rating: {average_rating}")
        print("\nSongs per style:")
        print(count_style)

        #rating_playlist = float(input(" What grade do you give to the playlist (1-5)? ")) #user rating playlist

        for id_songs in id_songs_playlist: #take all songs and save in dataframe

            new_playlist_auto = {"id_playlist": name_playlist, "duration_playlist": duration_playlist, "id_music": id_songs, "average_rating_musics": average_rating, "num_ratings": "1.0"} #dictionary to csv file

            playlist_auto_df = pd.DataFrame([new_playlist_auto]) # Convert the dictionary to a DataFrame
            add_playlist_df = pd.concat([add_playlist_df,playlist_auto_df], ignore_index=True) # Concat the new line of playlist (present in dictionary) on add_playlist_df

        new_playlists = pd.concat([playlists_df,add_playlist_df])
        new_playlists = new_playlists.set_index('id_playlist')

        new_playlists.to_csv('data/playlist.csv') #add on csv file
        # Create a DataFrame containing all created playlists
        createdPlaylists_df = pd.concat(createdPlaylists)

    return createdPlaylists_df

def playlistRulesFun():
    try:
        createdPlaylists_df = createdPlaylists()
        list_ids_playlist = createdPlaylists_df['id_playlist'].drop_duplicates().tolist()

        # Print all created playlists
        print("\nAll Created Playlists:")
        for id_playlist in list_ids_playlist:
            playlist = createdPlaylists_df[createdPlaylists_df["id_playlist"]==id_playlist]

            print(f"\n\nPlaylist name: {id_playlist}\n")
            print(playlist[['id_music', 'title', 'style', 'duration', 'duration_playlist']].to_markdown(index=False))
    except:
        print(Fore.YELLOW + Style.BRIGHT + "⚠️   WARNING: No playlist created" + Style.RESET_ALL)
        return






def songRecurrence():
    # Load data from the playlists CSV file
    playlist_df = pd.read_csv('data/playlist.csv')

    # Load data from the music CSV file
    tableMusic_df = pd.read_csv('data/tableMusic.csv', index_col='id_music')

    # Perform the join (merge) between the DataFrames using the music ID
    mergedID_df = pd.merge(playlist_df, tableMusic_df, left_on='id_music', right_index=True)

    # Count the presence of songs in the playlists
    count_music_df = mergedID_df['title'].value_counts().reset_index()
    count_music_df.columns = ['title', 'Prevalence on playlists']

    # Sort the songs by presence
    count_music_df = count_music_df.sort_values(by='Prevalence on playlists', ascending=False)

    # Display the most frequent songs
    print("                                                                  ")
    print(Fore.BLUE + Style.BRIGHT + "    This are the most popular songs in your playlists" + Style.RESET_ALL)
    print("                                                                  ")
    print(count_music_df.head().to_markdown(index=False))





def playlistsRanking():
    # Load the DataFrame from the playlists table
    playlist_df = pd.read_csv('data/playlist.csv')

    # Count the prevalence of playlists based on the ratings
    rankingPlaylist_df = playlist_df.groupby('id_playlist')['rating_playlist'].mean().reset_index()
    rankingPlaylist_df.columns = ['id_playlist', 'Playlist rating']

    # Sort the playlists by average rating in descending order
    rankingPlaylist_df = rankingPlaylist_df.sort_values(by='Playlist rating', ascending=False)

    # Display the ranking of playlists
    print("------------------------------------------------")
    print("                                                ")
    print(Fore.BLUE + Style.BRIGHT + "💙 Playlists Ranking 💙" + Style.RESET_ALL)
    print("                                                ")
    print(rankingPlaylist_df.to_markdown(index=False))






def removeSongDataBaseMenu():
    #Reads TableMusic and Playlist CSVs into dataframe variables
    tableMusic_df = pd.read_csv('data/tableMusic.csv')
    playlist_df = pd.read_csv('data/playlist.csv')

    #Shows all the available songs

    selected_columns = ['id_music', 'style', 'title', 'year', 'artist' , 'rating_global' , 'duration']
    filtered_table = tableMusic_df[selected_columns]

    print(Fore.BLUE + Style.BRIGHT + "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   Y O U R    L I B R A R Y   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:" + Style.RESET_ALL)
    print(filtered_table.to_markdown(index=False))
    print(Fore.BLUE + Style.BRIGHT + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:" + Style.RESET_ALL)

    #Testing function that removes a song from the entire database (tableMusic and playlists)
    songId = input("❓ Enter id of the song you wish to remove (0 to abort) => ")
    if songId == "0":
        return
    try:
        removeSongDataBase(tableMusic_df, playlist_df, int(songId))
    except:
        print("\033[1m ⚠️ WARNING: \033[0;0minvalid input")
        removeSongDataBaseMenu()
    print(tableMusic_df)
    return tableMusic_df


# function responsible for remove a song for the database and for the playlist in the same time.
def removeSongDataBase(tableMusic, playlists, id):
    #the condition sees if the index is in the dataframe tableMusic
    while id not in tableMusic["id_music"].values:
        print("\033[1m ⚠️ WARNING: \033[0;0mThis song is not in our system.")
        id = int(input(" Please choose a valid option (0 to abort) => "))
        if id == 0:
            break
    playlistsToUpdate = playlists["id_playlist"][playlists["id_music"]==id]

    for playListName in playlistsToUpdate:

        playlist = getPlaylist(playlists, playListName)
        playlist.reset_index(inplace = True, drop = True)
        numSongs = len(playlist)

        songRating = tableMusic['rating_global'][id == tableMusic["id_music"]].item()
        #calculate the new average song rating and put with one decimal place.
        newAverageSongRating = subtractFromAverage(playlist["average_rating_musics"][0], numSongs, songRating)
        newAverageSongRating = round(newAverageSongRating, 1)

        playlists["average_rating_musics"][(playlists["id_playlist"] == playListName)] = newAverageSongRating

    # .drop is the pandas function to remove anything; and get boolean array of music id matches
    tableMusic.drop(tableMusic[tableMusic["id_music"] == id].index,inplace=True)
    playlists.drop(playlists[playlists["id_music"] == id].index, inplace = True)
    #tableMusic and playlists are the dataframes where the music is going to be removed.
    tableMusic.to_csv("data/tableMusic.csv", index=False)
    playlists.to_csv("data/playlist.csv", index=False)
    print(Fore.BLUE + Style.BRIGHT + "SUCCESS: Song removed from database " + Style.RESET_ALL)

def removeSongPlaylist(tableMusic, playlists, playListName):

    #getPlaylist = playlist dataFrame
    used_playlist = getPlaylist(playlists, playListName)
    id_songs_playlist = list(set(used_playlist['id_music'])) #list id songs present in playlist
    #print(f"\nid_songs_playlist: {id_songs_playlist}")
    duration_playlist = int((used_playlist['duration_playlist']).iloc[0])

    average_rating = float((used_playlist['average_rating_musics']).iloc[0])
    print(f"\naverage_rating: {average_rating}")

    actual_playlist_df = pd.DataFrame()
    for id_songs in id_songs_playlist: #take all songs and save in dataframe
        title_per_id = (tableMusic[tableMusic['id_music']==id_songs]).iloc[0] #for print all songs titles
        title_music = title_per_id['title']
        #print(f"\ntitle_music: {title_music}")

        actual_playlist = {"id_music": id_songs, 'title': title_music,"average_rating_musics": average_rating, "duration_playlist": duration_playlist} #dictionary with playlist informations

        line_actual_playlist = pd.DataFrame([actual_playlist])
        actual_playlist_df = pd.concat([actual_playlist_df, line_actual_playlist], ignore_index=True)

    actual_playlist_df = actual_playlist_df.set_index('title')
    print(actual_playlist_df.to_markdown())

    songId = ""
    while songId == "":
        try:
            songId = int(input(" Enter id of song to be removed from " + playListName + " (0 to return) => "))
        except:
            # if songId == "0":
            #     return
            # else:
            print("\033[1m ⚠️ WARNING: \033[0;0mInvalid input.")
    #gets chosen playlist
    playlist = getPlaylist(playlists,playListName)
    numSongs = len(playlist)

    #checks if chosen id is in playlist
    print("playlist[id_music].values ", playlist["id_music"].values)
    if int(songId) in map(int, playlist["id_music"].values):
    # if (" " + str(songId) + " ") in str(playlist["id_music"].values):


        songRating = tableMusic['rating_global'][(songId == tableMusic["id_music"])].item()
        #calculate the new average song rating and put with one decimal place.
        newAverageSongRating = subtractFromAverage(list(playlist["average_rating_musics"])[0], numSongs, songRating)
        newAverageSongRating = round(newAverageSongRating, 1)

        playlists["average_rating_musics"][(playlists["id_playlist"] == playListName)] = newAverageSongRating


        #get boolean array of playlist matches
        playListMatch = playlists["id_playlist"] == playListName
        #get boolean array of music id matches
        idMatch = playlists["id_music"] == int(songId)
        #get indexes of songs to remove from playlist
        removeIndex = playlists[playListMatch & idMatch].index
        #removes from playLists dataframe the specified song of the specified playlist
        playlists.drop(removeIndex, inplace = True)
        print(Fore.BLUE + Style.BRIGHT + " SUCCESS: Song removed from playlist " + Style.RESET_ALL, playListName)

        try:
            playlists.to_csv("data/playlist.csv", index = False)
            print(getPlaylist(playlists, playListName))

        #error message from file errorCode
        except:
            return file_open
    elif songId == 0:
        return
    else :
        print("\033[1m ⚠️ WARNING: \033[0;0mInvalid input.")
        removeSongPlaylist(tableMusic, playlists, playListName)






def songPlaybackMenu(table):
    # Solicitar ao usuário o título  da música
    songs_list = sorted(list(table['title'].drop_duplicates()))
    print("\033[1m AVAILABLE SONGS \033[0;0m")
    for title in songs_list:
        print(" ", title)

    song_input = input(" What song do you want to play => ").lower()
    while song_input not in list(table['title'].str.lower()):
        print("\033[1m ⚠️ WARNING: \033[0;0mInvalid input.")
        song_input = input(" What song do you want to play => ").lower()
    playback(table.loc[table['title'].str.lower() == song_input])

# # define the countdown func.
# based off example found at https://www.programiz.com/python-programming/examples/countdown-timer
def playback(song):
    print("Now playing: ",list(song['title'])[0])
    # duration = int(song['duration'])
    duration = 5  # for testing purposes we set 5 seconds
    while duration:
        mins, secs = divmod(duration, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        duration -= 1
    song_rating(list(song['title'])[0])
    autoPlaylistUpdate()






# Read the playlists and music tables
playlist_df = pd.read_csv('data/playlist.csv')
tableMusic_df = pd.read_csv('data/tableMusic.csv')

def aviableUser():
    rating_min_user_df = tableMusic_df[(tableMusic_df['rating_user'] < 4.0)] #songs with user aviable < 4
    #print(f"rating_min_user_df:\n{rating_min_user_df}")
    id_songs_to_remove = rating_min_user_df['id_music'].tolist() #id songs list with user aviable < 4
    #print(f"\nid_songs_to_remove: {id_songs_to_remove}")

    return id_songs_to_remove

def playlistUpdate(): #update all playlists, excluding songs with user aviable < 4
    id_songs_to_remove = aviableUser()
    print(f"\nId songs to remove: {id_songs_to_remove}")
    list_playlists = playlist_df['id_playlist'].drop_duplicates().tolist() #list with playlists name

    for playlist_name in list_playlists: #id songs per playlist

        per_playlist_df = getPlaylist(playlist_df, playlist_name)
        id_songs_per_playlist = per_playlist_df['id_music'].tolist() #verify id songs list in specify playlist
        #print(f"id_songs_per_playlist {playlist_name}: {id_songs_per_playlist}")

        for songId in id_songs_to_remove: #get id's to remove
            if int(songId) in map(int, id_songs_per_playlist):
                songRating = tableMusic_df['rating_global'][(songId == tableMusic_df["id_music"])].item() #calculate the new average song rating and put with one decimal place.
                newAverageSongRating = subtractFromAverage(list(per_playlist_df["average_rating_musics"])[0], len(id_songs_per_playlist), songRating)
                newAverageSongRating = round(newAverageSongRating, 1)

                newAverageSongRating = playlist_df["average_rating_musics"][(playlist_df["id_playlist"] == playlist_name)]

                #get boolean array of playlist matches
                playListMatch = playlist_df["id_playlist"] == playlist_name
                #get boolean array of music id matches
                idMatch = playlist_df["id_music"] == int(songId)
                #get indexes of songs to remove from playlist
                removeIndex = playlist_df[playListMatch & idMatch].index
                #removes from playlist_df dataframe the specified song of the specified playlist
                playlist_df.drop(removeIndex, inplace = True)
                title_per_id = (tableMusic_df[tableMusic_df['id_music']==songId]).iloc[0] #for print all songs titles
                title_music = title_per_id['title']
                print(f"\033[1m SUCCESS: \033[0;0mSong {title_music} removed from playlist ", playlist_name)
                try:
                    playlist_df.to_csv("data/playlist.csv", index = False)
                    print(getPlaylist(playlist_df, playlist_name))

                #error message from file errorCode
                except:
                    return file_open
            else:
                continue
    return

def autoPlaylistUpdate():
    playlist_df = pd.read_csv("data/playlist.csv", sep=(','))
    playlist_prefix = 'play_auto_' #specif playlist name
    # Filter playlists by prefix name
    filtered_playlist_df = playlist_df[playlist_df['id_playlist'].str.startswith(playlist_prefix)]
    id_songs_to_remove = aviableUser()

    # Check if there are playlists with the playlist prefix name
    if not filtered_playlist_df.empty:
        list_playlists = filtered_playlist_df['id_playlist'].drop_duplicates().tolist()

        for playlist_name in list_playlists: #id songs per playlist

            per_playlist_df = getPlaylist(filtered_playlist_df, playlist_name)
            id_songs_per_playlist = per_playlist_df['id_music'].tolist() #verify id songs list in specify playlist
            for songId in id_songs_to_remove: #get id's to remove
                if int(songId) in map(int, id_songs_per_playlist):
                    songRating = tableMusic_df['rating_global'][(songId == tableMusic_df["id_music"])].item() #calculate the new average song rating and put with one decimal place.
                    newAverageSongRating = subtractFromAverage(list(per_playlist_df["average_rating_musics"])[0], len(id_songs_per_playlist), songRating)
                    newAverageSongRating = round(newAverageSongRating, 1)

                    newAverageSongRating = playlist_df["average_rating_musics"][(playlist_df["id_playlist"] == playlist_name)]

                    #get boolean array of playlist matches
                    playListMatch = playlist_df["id_playlist"] == playlist_name
                    #get boolean array of music id matches
                    idMatch = playlist_df["id_music"] == int(songId)
                    #get indexes of songs to remove from playlist
                    removeIndex = playlist_df[playListMatch & idMatch].index
                    #removes from playlist_df dataframe the specified song of the specified playlist
                    playlist_df.drop(removeIndex, inplace = True)
                    print("\033[1m SUCCESS: \033[0;0mSong removed from playlist ", playlist_name)
                    try:
                        playlist_df.to_csv("data/playlist.csv", index = False)
                        print(getPlaylist(playlist_df, playlist_name))

                    #error message from file errorCode
                    except:
                        return file_open
                else:
                    continue
    else: # playlist not found
        print(" No playlists updated.")

    return





#this function add the rank into a playlist
def addRank(playlists, chosenPlaylist):
    #the playlist will try to find the playlist the user want using the auxiliar function getPlaylist
    playlist = getPlaylist(playlists, chosenPlaylist)
    #checks if chosen playlist is in playlist file:
    if len(playlist) <= 0 :
        return playlist_not_found

#reset the index from the playlist chosen is needed for the average formula
    playlist.reset_index(inplace = True, drop = True)

    print(" You chose the playlist ", chosenPlaylist)
    #user input
    userRating = input(" Rate the chosen playlist (from 1 to 5) => ")
    #the user input can be a decimal number, but if it's something different it will return a sintax error.
    try:
        userRating = float(userRating)
    except:
        print("\033[1m WARNING: \033[0;0mInvalid input")
        return sintax
    #the values accepted are between 1 and 5
    if not(userRating > 0 and userRating <= 5):
        print("\033[1m WARNING: \033[0;0mOut of range")
        return invalid_rating

    #Get column with the playlist ranking
    playlistRatingColumn = playlist["rating_playlist"]

    #Get one element of the column -> ranking of the playlist
    currentRank = playlistRatingColumn[0]

    if math.isnan(currentRank):
        currentRank = 0

    #Get the number of ratings from the playlist chosen
    playlistNumberOfReviewColumn = playlist["num_ratings"]
    #This is the current number of ratings before the changes
    currentNumberOfReview = playlistNumberOfReviewColumn[0]

    #calculate the average with the information above.
    newAverage = addToAverage(currentRank, currentNumberOfReview, userRating)
    newAverage = round(newAverage, 1)

    # new average after the user rating
    playlists["rating_playlist"][playlists["id_playlist"] == chosenPlaylist] = newAverage
    # the number of ratings is the last one plus (+) 1 (the user that have already done the rating)
    playlists["num_ratings"][playlists["id_playlist"] == chosenPlaylist] = currentNumberOfReview+1

    #try save in the file, and if not return an error message.
    try:
        playlists.to_csv("data/playlist.csv", index = False)
        print("\033[1m SUCCESS: \033[0;0mPlaylist rated ", userRating)

    except:
        return file_open

    #print the playlist after the changes
    playlist = getPlaylist(playlists, chosenPlaylist)
    print(playlist)

    #error code = 0
    return successfull_execution





def list_available_playlists():
    # Load the DataFrame from the playlist table
    playlist_df = pd.read_csv('data/playlist.csv')

    # Display the list of available playlists
    available_playlists = playlist_df['id_playlist'].unique()
    print("\033[1m Available Playlists: \033[0;0m")
    for i in range(1, len(available_playlists), 1):
        print(" ", available_playlists[i])

def choose_random_music(tableMusic_df):
    # Choose a music randomly
    random_music = tableMusic_df.sample(n=1)

    return random_music

def view_playlist_songs(playlist_name):
    while True:
        # Load the DataFrame from the playlist table
        playlist_df = pd.read_csv('data/playlist.csv', names=['id_playlist', 'duration_playlist', 'id_music', 'rating_playlist', 'average_rating_musics', 'num_ratings'])

        # Check if the user wants to exit
        if playlist_name == '0':
            print(" Quitting...")
            break

        # Locate the playlist based on the name
        selected_playlist = playlist_df[playlist_df['id_playlist'].str.lower() == playlist_name.lower()]

        # Check if the playlist was found
        if not selected_playlist.empty:
            # Get the IDs of the songs in the playlist
            songs_ids = selected_playlist['id_music']

            # Load the DataFrame from the music table
            tableMusic_df = pd.read_csv('data/tableMusic.csv', names=['id_music', 'style', 'type', 'title', 'songwritter', 'year', 'artist', 'rating_global', 'rating_user', 'duration'])

            # Filter the songs from the desired playlist
            songs_info = tableMusic_df[tableMusic_df['id_music'].isin(songs_ids)][['title', 'style', 'year', 'artist', 'rating_global']]

            # Display the songs in the playlist with global rating in table format
            print("\nSongs in the playlist:")
            print(songs_info.to_markdown(index=False))

            while True:
                # Ask the user what they want to do
                option = input("""\n\033[1m further info: \033[0;0m\n\033[1m 1 \033[0;0m duration\n\033[1m 2 \033[0;0m rating\n\033[1m 0 \033[0;0m back\n (enter a number) => """)


                if option == '1':
                    # Get information about the playlist
                    # playlist_duration = selected_playlist.iloc[0]['duration_playlist']
                    # print(f"\nPlaylist duration: {playlist_duration} minutes")
                    playlist_duration_min = math.floor(int(selected_playlist.iloc[0]['duration_playlist']) / 60)
                    playlist_duration_sec = int(selected_playlist.iloc[0]['duration_playlist']) % 60
                    print(f"\nPlaylist duration : {playlist_duration_min} minutes and {playlist_duration_sec} seconds")

                elif option == '2':
                    # Get information about the playlist
                    playlist_rating = selected_playlist.iloc[0]['rating_playlist']
                    print(f"\n Playlist rating: {playlist_rating}")
                elif option == '0':
                    break
                else:
                    print(" \033[1m WARNING: \033[0;0mInvalid option. Please try again.")
            return
        else:
            print(f"\033[1m WARNING: \033[0;0m Playlist '{playlist_name}' not found. Please try again.")
