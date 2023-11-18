from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download("C:\\Users\\hp\\Downloads\\")
      #use the path of the directory where the downloaded videos should be saved
    except:
        print("An error has occurred")
    print("Download successfull")

#creating an empty list to store the links of the videos
links_list = []  
#getting the number of videos to be downloaded
int_of_links = int(input("Enter the number of videos to be downloaded: "))

#using for loop to add multiple links to the list
for i in range(int_of_links):
    input_link = input("Enter the YouTube video URL: ")
    links_list.append(input_link)
  
#iterating through the list and downloading each video
for video in links_list:
    Download(video)

