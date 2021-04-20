from flask import Blueprint, request, current_app

from http import HTTPStatus
from app.models.band_model import BandModel

from app.serializers.band_serializer import BandSerializer

bp_band = Blueprint("bp_band", __name__, url_prefix="/api")

@bp_band.route('/band', methods=["POST"])
def band():

    session = current_app.db.session

    data = request.get_json()
    band = BandModel(name=data["name"])
    session.add(band)
    session.commit()

    return {"id": band.id, "band_name": band.name}, HTTPStatus.CREATED

@bp_band.route('/band/<int:id>')
def get_band_by_id(id):
    
    serializer = BandSerializer(id)
    return serializer