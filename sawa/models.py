from django.db import models

#Models and classes for data attributes
class FileInput(models.Model):
    file_input = models.FileField('data/')
    review_user = models.ForeignKey('ReviewUser', on_delete=models.CASCADE)
    review = models.ForeignKey('Review', on_delete=models.CASCADE)
    smoutreach = models.ForeignKey('SocialMediaOutreach', on_delete=models.CASCADE)

class ReviewUser(models.Model):
    username = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    
class Review(models.Model):
    user = models.ForeignKey('ReviewUser', on_delete=models.CASCADE)
    outreach = models.ForeignKey('SocialMediaOutreach', on_delete=models.CASCADE)
    activity_text = models.CharField(max_length=5000, null=True, blank=True)
    created_date = models.CharField(max_length=25, null=True, blank=True)
    rating = models.IntegerField()
    activity_name = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    
class SocialMediaOutreach(models.Model):
    facebook = models.IntegerField()
    twitter = models.IntegerField()
    offline = models.IntegerField()
    
class Sentiment(models.Model):
    terrible_sentiment = models.FloatField()
    bad_sentiment = models.FloatField()
    neutral_sentiment = models.FloatField()
    good_sentiment = models.FloatField()
    excellent_sentiment = models.FloatField()
    
    #def __str__(self):
        #return self.terrible_sentiment
        
class SentimentCount(models.Model):
    ct_terrible = models.IntegerField()
    ct_bad = models.IntegerField()
    ct_neutral = models.IntegerField()
    ct_good = models.IntegerField()
    ct_excellent = models.IntegerField()
    
    @property
    def show_ct_terrible(self):
        return '%i' % (self.ct_terrible)
    @property
    def show_ct_bad(self):
        return '%i' % (self.ct_bad)
    @property
    def show_ct_neutral(self):
        return '%i' % (self.ct_neutral)
    @property
    def show_ct_good(self):
        return '%i' % (self.ct_good)
    @property
    def show_ct_excellent(self):
        return '%i' % (self.ct_excellent)
    
    def delete_session_values():
        SentimentCount.objects.all().delete()
    
class SentimentPercentage(models.Model):
    pt_terrible = models.FloatField()
    pt_bad = models.FloatField()
    pt_neutral = models.FloatField()
    pt_good = models.FloatField()
    pt_excellent = models.FloatField()
    
    @property
    def show_pt_terrible(self):
        return '%f' % (self.pt_terrible * 100)
    @property
    def show_pt_bad(self):
        return '%f' % (self.pt_bad * 100)
    @property
    def show_pt_neutral(self):
        return '%f' % (self.pt_neutral * 100)
    @property
    def show_pt_good(self):
        return '%f' % (self.pt_good * 100)
    @property
    def show_pt_excellent(self):
        return '%f' % (self.pt_excellent * 100)
    
    def delete_session_values():
        SentimentPercentage.objects.all().delete()
    



    
    


    
        
