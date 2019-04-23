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
    artist = graphene.Field(ArtistType, id=graphene.Int())
    album = graphene.Field(AlbumType, id=graphene.Int())
    all_artists = graphene.List(ArtistType)
    all_albums = graphene.List(AlbumType)

    def resolve_artist(self, info, **kwargs):
        id = kwargs.get('id')
        if id:
            return Artist.objects.get(pk=id)
        return None

    def resolve_album(self, info, **kwargs):
        id = kwargs.get('id')
        if id:
            return Album.objects.get(pk=id)
        return None

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_all_albums(self, info, **kwargs):
        return Album.objects.all()
