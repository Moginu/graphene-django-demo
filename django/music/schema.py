import graphene
from graphene_django.types import DjangoObjectType

from music.models import Artist, Album


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album


class Query(object):
    all_artists = graphene.List(ArtistType)
    all_albums = graphene.List(AlbumType)

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_all_albums(self, info, **kwargs):
        return Album.objects.select_related('artist').all()
