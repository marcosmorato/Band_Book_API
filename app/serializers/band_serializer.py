from app.models import music_model
from app.models.band_model import BandModel

def BandSerializer(band_id: int):
    band = BandModel.query.get(band_id)
    music_list = band.music_list
    genre_list = band.genre_list

    return {
        "id": band.id,
        "name": band.name,
        "musics": [music.name for music in music_list],
        "genres": [genre.name for genre in genre_list]
    }