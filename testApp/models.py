from django.db import models

class categoryTable(models.Model):
    categoryID = models.CharField(max_length=30, primary_key=True)
    
    def __str__(self):
        return self.categoryID

class card_table(models.Model):
    cardID = models.AutoField(primary_key=True)
    categoryID = models.ForeignKey(
        categoryTable,
        on_delete = models.CASCADE
    )
    serialNO = models.IntegerField(default=0)
    title = models.CharField(max_length=30)
    paragraph = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    
    def __str__(self):
        return str(self.categoryID) + " -> " + self.title

class image_table(models.Model):
    title = models.CharField(max_length=30)
    cardID = models.ForeignKey(
        card_table,
        on_delete = models.CASCADE
    )
    serialNO = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    upload = models.ImageField()

    def __str__(self):
        return self.cardID.title + " -> " + self.title

class code_table(models.Model):
    title = models.CharField(max_length=30)
    cardID = models.ForeignKey(
        card_table,
        on_delete = models.CASCADE
    )
    serialNO = models.IntegerField(default=0)
    text = models.TextField()

    def __str__(self):
        return self.cardID.title + " -> " + self.title

class recommendation_table(models.Model):
    title = models.CharField(max_length=30)
    cardID = models.ForeignKey(
        card_table,
        on_delete = models.CASCADE
    )
    serialNO = models.IntegerField(default=0)
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.cardID.title + " -> " + self.title