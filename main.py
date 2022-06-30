from pytube import YouTube
# you may need to wait a few minutes for it to fully download

def download(url: str, outpath: str = "./"):

    yt = YouTube(url)

    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath) #change the 360p to whatever quality you want it


if __name__ == "__main__":

    download(
        "Link goes here", #this line is for your link
        "./videos", # this is where the video will be placed, look for a folder called videos after the download is complete
    )

