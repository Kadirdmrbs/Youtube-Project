from django.db import models

# Create your models here.

Category_Choices = (
    ('Soccer-International','Soccer-International'),
    ('Soccer-Highlights', 'Soccer-Highlights'),
    ('Soccer-LaLiga','Soccer-LaLiga'),
    ('Soccer-SerieA','Soccer-SerieA'),

    ('Basketball-Highlights','Basketball-Highlights'),
    ('Basketball-NBA','Basketball-NBA'),
    ('Basketball-Highlights','Basketball-Highlights'),

    ('Fighting-Highlights','Fighting-Highlights'),
    ('Fighting-UFC','Fighting-UFC'),
    ('Fighting-WWE','Fighting-WWE'),

    ('Racing-Formula 1','Racing-Formula 1'),
    ('Racing-Formula 2','Racing-Formula 2'),
    ('Racing-MotoGP','Racing-MotoGP'),
    ('Racing-Highlights','Racing-Highlights'),
    ('Racing-Son Viraj','Racing-Son Viraj'),

    ('Betting','Betting'),

    ('Tennis-Highlights','Tennis-Highlights'),
    ('Tennis-Wimbledon','Tennis-Wimbledon'),
    ('Tennis-ATP','Tennis-ATP')
)

Year_Choices = (
    ('2018','2018'),
    ('2019', '2019'),
    ('2020','2020'),
    ('2021','2021'),
    ('2022','2022')
)

class MlModel(models.Model):
    likes = models.IntegerField()
    comments = models.IntegerField()
    duration = models.IntegerField()
    category = models.CharField(max_length=30,choices=Category_Choices, default='Soccer-International')
    year = models.CharField(max_length=5,choices=Year_Choices, default='2022')