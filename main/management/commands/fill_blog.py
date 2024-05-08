from django.core.management import BaseCommand

from main.models import Article
from main.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = ['Art', 'Hard', 'Smart']
        for item in categories:
            Category.objects.create(
                title=item
            )

        articles = [
            {'category': 1, 'title': 'News one', 'body': 'Разработчики ПО создали огромную инсталляцию из велосипедов и костылей'},
            {'category': 1, 'title': 'News two', 'body': 'Поступили в продажу воздушные шарики в форме [цензура]'},
            {'category': 2, 'title': 'News three', 'body': 'Два муравья сожрали слона'},
            {'category': 2, 'title': 'News four', 'body': 'Часть лидеров мировых государств - зомби'},
            {'category': 2, 'title': 'News five', 'body': 'Люди без мозга среди нас!'},
            {'category': 3, 'title': 'News six', 'body': 'Как заставить работать вместо себя'},
            {'category': 3, 'title': 'News seven', 'body': 'Промывание мозгов: как научиться'},
        ]

            # for student_item in student_list:
            #     Student.objects.create(**student_item)

            # students_for_create = []
            # for student_item in student_list:
            #     students_for_create.append(Student(**student_item))
            #
            # Student.objects.bulk_create(students_for_create)

        for item in articles:
            print(item)
            # input('\\\see...')
            # category=Category.objects.get(id=item['category']),
            Article.objects.create(
                title=item['title'],
                body=item['body'],
                category=Category.objects.get(id=item['category'])

                )
            #     category=
            #     title=item,
            #     body='Lorem ipsum' + str(item)
            # )
            # for item in articles:
            #     Article.objects.create(
            #         category=Category.objects.get(id=1),
            #         title=item['title'],
            #         body=item['body']
            #     )
