from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

GENDERS=((0,"Woman"),(1,"Nonbinary"),(2,"Genderfluid"),(3,"Man"),(4,"Prefer not to answer"))
LOOKING_FOR=((0,"Women"),(1,"Men and Women"),(2,"Neither"),(3,"All"),(4,"Men"))
ALLIGNMENT=((0,"Light Side"),(1,"Force Neutral"),(2,"Dark Side/Sith"))
# Create your models here.
class UserWW(User):
    force_allignment = models.IntegerField(choices=ALLIGNMENT, default=1)
    gender = models.IntegerField(choices=GENDERS, default=4)
    looking_for = models.IntegerField(choices=LOOKING_FOR, default=3)
    profile_image = models.ImageField()
    suggestions = models.ManyToManyField(UserWW)
    matches = models.ManyToManyField(UserWW)
    facebook = models.CharField(max_length=30)
    instagram = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)

class SurveyResult(models.Model):
    user = models.OneToOneField(UserWW, on_delete=models.CASCADE, primary_key=True)
    a_new_hope = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    empire_strikes_back = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    return_of_the_jedi = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    phantom_menace = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    attack_of_the_clones = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    revenge_of_the_sith = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    force_awakens = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    last_jedi = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    rise_of_skywalker = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    rogue_one = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    solo = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    mandalorian = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    book_of_boba_fett = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    obi_wan_kenobi = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    andor = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    ahsoka = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    clone_wars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    rebels = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    resistance = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    bad_batch = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    visions = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    tales_of_the_empire = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
    tales_of_the_jedi = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)

class Message(models.Model):
    from_user = models.ManyToManyField(UserWW)
    to_user = models.ManyToManyField(UserWW)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)

