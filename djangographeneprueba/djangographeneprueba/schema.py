import graphene
from graphene_django import DjangoObjectType
from farmacia.models import Book


class BooksType (DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id', 'nombre', 'titulo', 'fecha')

class CreateBook(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        titulo = graphene.String(required=True)

    book = graphene.Field(BooksType)

    def mutate(self, info, nombre, titulo):
        book = Book(nombre=nombre, titulo=titulo)
        book.save()
        return CreateBook(book=book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()


class Query(graphene.ObjectType):
    hello = graphene.String()
    books = graphene.List(BooksType)

    def resolve_books(self, info):
        return Book.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)