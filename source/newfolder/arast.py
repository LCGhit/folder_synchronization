import pandas as pd
import functions as f

playlist_df = pd.read_csv('data/playlist.csv')
tableMusic_df = pd.read_csv('data/tableMusic.csv')

df_min_sec = pd.read_csv('data/tableMusic.csv')
df_min_sec['duration'] = pd.to_timedelta(df_min_sec['duration']).astype('int64')
df_min_sec['columnAsMinutes'] = df_min_sec['duration'].floordiv(60)
df_min_sec['columnAsMinutes'] = df_min_sec['columnAsMinutes'].astype(str)
df_min_sec['columnAsMinutes'] = df_min_sec['columnAsMinutes']+":"+df_min_sec['duration'].mod(60).astype(str)
df_min_sec.drop('duration', axis = 1, inplace = True)

main_menu = """
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
\033[94m                       J U K E B O T I F Y      \033[0;0m
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

\033[35m M A I N   M E N U \033[0;0m
======================================================================
\033[1m┇ 1️⃣ \033[0;0m manage your library                                              ┇
\033[1m┇ 2️⃣ \033[0;0m manage your playlists                                            ┇
\033[1m┇ 3️⃣ \033[0;0m quick play                                                       ┇
\033[1m┇ 0️⃣ \033[0;0m exit Jukebotify                                                  ┇
======================================================================
🎶  Please select the option by number 🎶 >>> """

submenu_1 = """
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

 main menu / \033[94mMANAGE YOUR LIBRARY \033[0;0m
\033[1m 1️⃣ \033[0;0m check library
\033[1m 2️⃣ \033[0;0m add song to library
\033[1m 3️⃣ \033[0;0m delete song from library
\033[1m 4️⃣ \033[0;0m create new music style
\033[1m 0️⃣ \033[0;0m back
        🎵 🎵 🎵   Please enter a number >>> """

submenu_2 = """
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

 main menu / \033[94mMANAGE YOUR PLAYLISTS \033[0;0m
\033[1m 1️⃣ \033[0;0m create random playlist
\033[1m 2️⃣ \033[0;0m create a personalized playlist
\033[1m 3️⃣ \033[0;0m edit a playlist
\033[1m 4️⃣ \033[0;0m show playlists ranking
\033[1m 0️⃣ \033[0;0m back
        🎵 🎵 🎵   Please enter a number >>> """

submenu_2_1 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu/manage playlists/\033[1mRANDOM PLAYLIST \033[0;0m
\033[1m 1 \033[0;0m start playback
\033[1m 0 \033[0;0m back
 (enter a number) => """

submenu_2_2 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu/manage playlists/\033[1mPERSONALIZED PLAYLIST \033[0;0m
\033[1m 1 \033[0;0m create another playlist
\033[1m 0 \033[0;0m back
 (enter a number) => """

submenu_2_3 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu/manage playlists/\033[1mEDIT PLAYLIST \033[0;0m
\033[1m 1 \033[0;0m expand playlist
\033[1m 2 \033[0;0m add song to playlist
\033[1m 3 \033[0;0m remove song from playlist
\033[1m 4 \033[0;0m rate playlist
\033[1m 5 \033[0;0m pick another playlist
\033[1m 0 \033[0;0m back
 """

submenu_3 = """
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

 main menu / \033[94mQUICK PLAY \033[0;0m
\033[1m 1️⃣ \033[0;0m play random song
\033[1m 2️⃣ \033[0;0m pick song
\033[1m 3️⃣ \033[0;0m check most popular songs in playlists
\033[1m 4️⃣ \033[0;0m check highest rated songs
\033[1m 0️⃣ \033[0;0m back
        🎵 🎵 🎵   Please enter a number >>> """

from colorama import Fore, Style

def welcome_message():
    print(Fore.WHITE)
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                      ║")
    print(Fore.BLUE + Style.BRIGHT +"║                       J U K E B O T I F Y                            ║"+ Style.RESET_ALL)
    print("║                                                                      ║")
    print("║                🎶 Bringing Your Tunes to Life 🎶                     ║")
    print("║                                                                      ║")
    print("║  Hello there! Welcome to Jukebotify, your ultimate music companion.  ║")
    print("║                                                                      ║")
    print("║  Whether you're into pop, jazz, rock any other style...              ║")
    print("║  ... we've got you covered!                                          ║")
    print("║                                                                      ║")
    print("║  Explore a world of music management, automatic playlist generation, ║")
    print("║  and personalized playlists based on your tastes.                    ║")
    print("║  With Jukebotify, you're in control of your musical journey.         ║")
    print("║                                                                      ║")
    print("║  Get ready to dive into the rhythm and let Jukebotify curate the     ║")
    print("║  perfect playlists for every moment.                                 ║")
    print("║                                                                      ║")
    print("║  Let the music play!                                                 ║")
    print("║                                                                      ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print(Style.RESET_ALL)

# Call the function to display the welcome message
welcome_message()


def farewell_message():
    print(Fore.WHITE)
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                      ║")
    print(Fore.BLUE + Style.BRIGHT + "║                       J U K E B O T I F Y                            ║" + Style.RESET_ALL)
    print("║                                                                      ║")
    print("║              🎶 Thank you for using Jukebotify! 🎶                   ║")
    print("║                                                                      ║")
    print("║        We hope you enjoyed the musical journey with us.              ║")
    print("║        Your tunes are always just a click away.                      ║")
    print("║                                                                      ║")
    print("║        Keep the rhythm alive and come back soon for more tunes.      ║")
    print("║        Jukebotify is here whenever you need a melody.                ║")
    print("║                                                                      ║")
    print("║        Until next time, farewell and let the music play on!          ║")
    print("║                                                                      ║")
    print("║        🎶 Let the music be the soundtrack of your life. 🎶           ║")
    print("║                                                                      ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print(Style.RESET_ALL)



def subMenu_1():                            # MANAGE YOUR LIBRARY
    second_input = -1
    while second_input != 0:
        second_input = input(submenu_1)
        match(second_input):
            case("1"):
                #print(Fore.BLUE + Style.BRIGHT + "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   Y O U R    L I B R A R Y   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + Style.RESET_ALL)
                #tableMusic_df = pd.read_csv("data/tableMusic.csv")
                #print(tableMusic_df.to_markdown(index=False))
                #print(Fore.BLUE + Style.BRIGHT + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+ Style.RESET_ALL)

                selected_columns = ['id_music', 'style', 'type', 'title', 'year', 'artist' , 'rating_global' , 'columnAsMinutes']
                filtered_table = df_min_sec[selected_columns]

                print(Fore.BLUE + Style.BRIGHT + "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   Y O U R    L I B R A R Y   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:" + Style.RESET_ALL)
                print(filtered_table.to_markdown(index=False))
                print(Fore.BLUE + Style.BRIGHT + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:" + Style.RESET_ALL)


            case("2"):
                f.addMusicDatabase()
            case("3"):
                f.removeSongDataBaseMenu()
            case("4"):
                f.addStyle()
            case("0"):
                return
            case(_):
                print("\033[1m WARNING: \033[0;0minvalid input")
                continue

def subMenu_2():                          # MANAGE YOUR PLAYLISTS
    second_input = -1
    while second_input != 0:
        second_input = input(submenu_2)
        match(second_input):
            case("1"):
                subMenu_2_1()
            case("2"):
                subMenu_2_2()
            case("3"):
                subMenu_2_3()
            case("4"):
                f.playlistsRanking()
            case("0"):
                return
            case(_):
                print("\033[1m WARNING: \033[0;0minvalid input")
                continue


def subMenu_2_1():                      # Create random playlists
    f.playlistRulesFun()
    return

def subMenu_2_2():                      # Create personalized playlist
    f.playlistManualFun()
    second_input = -1
    while second_input != 0:
        second_input = input(submenu_2_2)
        match(second_input):
            case("1"):
                f.playlistManualFun()
                continue
            case("0"):
                return
            case(_):
                print(Fore.YELLOW + Style.BRIGHT + "⚠️   WARNING: invalid input" + Style.RESET_ALL)
                continue

def subMenu_2_3():                      # Edit playlist
    playlist_df = pd.read_csv('data/playlist.csv')
    second_input = 5
    playlist_pick = f.pickPlaylist(playlist_df)
    while second_input != 0:
        print(submenu_2_3 , "selected playlist[\033[1m" , playlist_pick , "\033[0;0m]\n")
        second_input = input(" (enter a number) => ")
        match(second_input):
            case("1"):
                f.view_playlist_songs(playlist_pick)
            case("2"):
                f.addMusic(playlist_df, tableMusic_df, playlist_pick)
            case("3"):
                f.removeSongPlaylist(tableMusic_df, playlist_df, playlist_pick)
            case("4"):
                f.addRank(playlist_df, playlist_pick)
            case("5"):
                playlist_pick = f.pickPlaylist(playlist_df)
                continue
            case("0"):
                return
            case(_):
                print("\033[1m WARNING: \033[0;0minvalid input")
                continue

def subMenu_3():                    # QUICK PLAY
    second_input = -1
    while second_input != 0:
        tableMusic_df = pd.read_csv('data/tableMusic.csv')
        second_input = input(submenu_3)
        match(second_input):
            case("1"):
                print(tableMusic_df.sample())
                f.playback(tableMusic_df.sample())
                return
            case("2"):
                f.songPlaybackMenu(tableMusic_df)
                return
            case("3"):
                f.songRecurrence()
            case("4"):
                f.rankByStyle()
            case("0"):
                return
            case(_):
                print("\033[1m WARNING: \033[0;0minvalid input")
                continue

def mainMenu():
    first_input = -1
    while first_input != 0:
        first_input = input(main_menu)
        match(first_input):
            case("1"):
                subMenu_1()
            case("2"):
                subMenu_2()
            case("3"):
                subMenu_3()
            case("0"):
                farewell_message()
                return
            case(_):
                print("\033[1m WARNING: \033[0;0minvalid input")
                continue
mainMenu()
