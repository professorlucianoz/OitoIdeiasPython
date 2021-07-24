from pytube import YouTube

link = "https://www.youtube.com/watch?v=vje3tGYGSAo&t=202s"

yt = YouTube(link)

print("Título: ", yt.title)
print("Views: ", yt.views)

ys = yt.streams.get_highest_resolution()

ys.download()


