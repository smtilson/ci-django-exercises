data = """Return of the Jedi int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Phantom Menace int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Attack of the Clones int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Revenge of the Sith int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Force Awakens int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Last Jedi int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Rise of Skywalker int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Rogue One int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Solo int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Mandalorian int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Book of Boba Fett int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Obi-Wan Kenobi int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Andor int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Ahsoka int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Clone Wars int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Rebels int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Resistance int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Bad Batch int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Visions int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Tales of the Empire int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
Tales of the Jedi int nullable= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)
"""

lines = data.split('\n')
titles = [line.split(' int nullable')[0] for line in lines]
titles = [title.replace(' ', '_') for title in titles]
titles = [title.lower() for title in titles]
value = ' = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],null=True)'
lines = [line+value for line in titles]
for line in lines:
    print(line)
    print()
