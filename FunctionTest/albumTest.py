def make_album(singer_name,album_name,countNum=20):
    album={}
    album['singer_name']=singer_name
    album['album_name']=album_name
    album['count']=countNum

    return album

TheAlbum=make_album('Zhoujielun','anxiang')

print(TheAlbum)