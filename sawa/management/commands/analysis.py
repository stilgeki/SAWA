from django.core.management.base import BaseCommand, CommandError
import csv
from textblob import TextBlob
from sawa.models import Sentiment, SentimentPercentage, SentimentCount
from bokeh.charts import Bar, output_file, show
import pandas as pd

class Command(BaseCommand):
    def handle(self, *args, **options):
        #Initialize all variables
        file_input = '/Users/Jason Plagens/Documents/Spring Semester 2016/ISA 406/Project/Django Project/isa406/sawa/data/Product Reviews - PowerBar Energy Blends.csv'

        #Initialize the sentiment factor lists
        terrible_list = []
        bad_list = []
        neutral_list = []
        good_list = []
        excellent_list = []
        
        #Initialize empty lists for review information
        activity_text_list = []
        clean_activity_text_list = []
        created_date_list = []
        rating_list = []
        activity_name_list = []
        title_list = []

        #Initialize empty lists for user who posted review information
        username_list = []
        age_list = []
        gender_list = []
        city_list = []
        
        #Initialize empty lists for media reach of review information
        facebook_list = []
        twitter_list = []
        offline_list = []
        
        with open(file_input, encoding = 'utf-8') as csvfile:
            readCSV = csv.reader(csvfile, delimiter = ',')

            #Initialize variables
            username = ""
            age = 0
            gender = ""
            city = ""
            activity_text = ""
            created_date = ""
            rating = 0
            activity_name = ""
            title = ""
            facebook = 0
            twitter = 0
            offline = 0


            #For each row in CSV, add review data to associated list
            for row in readCSV:
                activity_text = row[9]
                created_date = row[1]
                rating = row[6]
                activity_name = row[7]
                title = row[8]

                activity_text_list.append(activity_text)
                created_date_list.append(created_date)
                rating_list.append(rating)
                activity_name_list.append(activity_name)
                title_list.append(title)

            #For each row in CSV, add user who posted review data to associated list
            for row in readCSV:
                username = row[0]
                age = row[2]
                gender = row[3]
                city = row[4]

                username_list.append(username)
                age_list.append(age)
                gender_list.append(gender)
                city_list.append(city)

            #For each row in CSV, add media reach of review data to associated list
            for row in readCSV:
                facebook = row[0]
                twitter = row[2]
                offline = row[3]

                facebook_list.append(facebook)
                twitter_list.append(twitter)
                offline_list.append(offline)

            #Print the total number of reviews that are in the file
            print("Total number of reviews = ", len(activity_text_list))

            #For loop to iterate over each item in the review list
            for list_item in activity_text_list:

                #Perform textblob analysis
                review_polarity = TextBlob(list_item).sentiment.polarity

                #If statements that determine the review's sentiment result and which bucket it falls into
                
                if review_polarity >= -1 and review_polarity < -0.5:
                    
                    #Save into internal list
                    terrible_sentiment = review_polarity
                    terrible_list.append(terrible_sentiment)
                    
                    #Save in db
                    terrible_sentiment = Sentiment(terrible_sentiment = review_polarity)
                    terrible_sentiment.save()
                    

                elif review_polarity >= -0.5 and review_polarity < 0:
                    
                    #Save into internal list
                    bad_sentiment = review_polarity
                    bad_list.append(bad_sentiment)
                    
                    #Save into db
                    bad_sentiment = Sentiment(bad_sentiment = review_polarity)
                    bad_sentiment.save()
                    

                elif review_polarity == 0:
                    
                    #Save into internal list
                    neutral_sentiment = review_polarity
                    neutral_list.append(neutral_sentiment)
                    
                    #Save into db
                    neutral_sentiment = Sentiment(neutral_sentiment = review_polarity)
                    neutral_sentiment.save()

                elif review_polarity > 0 and review_polarity <= 0.5:
                    
                    #Save into internal list
                    good_sentiment = review_polarity
                    good_list.append(good_sentiment)
                    
                    #Save into db
                    good_sentiment = Sentiment(good_sentiment = review_polarity)
                    good_sentiment.save()

                elif review_polarity <= 1 and review_polarity > 0.5:
                    
                    #Save into internal list
                    excellent_sentiment = review_polarity
                    excellent_list.append(excellent_sentiment)
                    
                    #Save into db
                    excellent_sentiment = Sentiment(excellent_sentiment = review_polarity)
                    excellent_sentiment.save()


        #Create object for count of sentiment and save to db
        ct_object = SentimentCount(ct_terrible = len(terrible_list), ct_bad = len(bad_list), ct_neutral = len(neutral_list), ct_good = len(good_list), ct_excellent = len(excellent_list))
        
        ct_object.save()

        #Create object for percentage of sentiment and save to db
        pt_object = SentimentPercentage(pt_terrible = (len(terrible_list)/len(activity_text_list)), pt_bad = (len(bad_list)/len(activity_text_list)), pt_neutral = (len(neutral_list)/len(activity_text_list)), pt_good = (len(good_list)/len(activity_text_list)), pt_excellent = (len(excellent_list)/len(activity_text_list)))
        
        pt_object.save()
        
        data = {
            'sentiment factor': ['Terrible', 'Bad', 'Neutral', 'Good', 'Excellent'],
            
            'sentiment count': [len(terrible_list), len(bad_list), len(neutral_list), len(good_list), len(excellent_list)]
        }
        
        p = Bar(data, values='sentiment count', label='sentiment factor',
          title="Sentiment of Reviews", legend='top_right', width=400)
        
        output_file("bar.html")
        
        show(p)
        
        #Comment out print function for counting number of reviews for testing if need be
            
        #print("Number of Terrible reviews = ", len(terrible_list))
        #print("Number of Bad reviews = ", len(bad_list))
        #print("Number of Neutral reviews = ", len(neutral_list))
        #print("Number of Good reviews = ", len(good_list))
        #print("Number of Excellent reviews = ", len(excellent_list))
            
        #Comment out print function for percent of reviews for testing if need be
            
        #print("Percentage of Terrible reviews = ", format(pt_terrible, ',.2%'))
        #print("Percentage of Bad reviews = ", format(pt_bad, ',.2%'))
        #print("Percentage of Neutral reviews = ", format(pt_neutral, ',.2%'))
        #print("Percentage of Good reviews = ", format(pt_good, ',.2%'))
        #print("Percentage of Excellent reviews = ", format(pt_excellent, ',.2%'))