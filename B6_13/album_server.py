from bottle import route
from bottle import run
from bottle import HTTPError
import album

@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        head = "Группа {} альбомов выпустила {} альбомов:<br>".format(artist, len(album_names))
        album_list = ''
        for i in ['<li>'+i for i in album_names]:
            album_list+=i
        result = head + '<ul>'+album_list+'</ul>'
    return result


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)