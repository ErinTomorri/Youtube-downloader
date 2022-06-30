from pytube import YouTube
# you may need to wait a few minutes for it to fully download
'''
This tool is for educational purposes only
Do not use it for illegal work or without the consent of the target
I am not responsible for any action taken using this script
I am not responsible for any damage of any kind for using this script'''
def download(url: str, outpath: str = "./"):

    yt = YouTube(url)

    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath) #change the 360p to whatever quality you want it


if __name__ == "__main__":

    download(
        "Link goes here", #this line is for your link
        "./videos", # this is where the video will be placed, look for a folder called videos after the download is complete
    )

