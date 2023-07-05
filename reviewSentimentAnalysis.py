import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def main():
    # Read the csv file:
    reviews=pd.read_csv("C:/Users/Kishor Balgi/OneDrive/Documents/UiPath/Flipkart Product Review Analysis/Reviews.csv")

    list_res=[]
    positive=0
    negative=0
    neutral=0

    # Sentiment Analysis using VaderSentiment:
    sid_obj = SentimentIntensityAnalyzer()

    # Iterate through the reviews and get the sentiment:
    for i in range(len(reviews)):
        data=reviews.iloc[i][0]
        # Calculate the sentiment:
        sentiment_dict = sid_obj.polarity_scores(data)
        if sentiment_dict['compound'] >= 0.05 :
            positive+=1
            list_res.append("Postive")
    
        elif sentiment_dict['compound'] <= - 0.05 :
            negative+=1
            list_res.append("Negative")
    
        else :
            neutral+=1
            list_res.append("Neutral")

    # Append a new column to the data frame with the sentiment information:
    reviews["Sentiment"] = list_res

    # Plot the pie chart:
    if(positive>negative and positive>=neutral):
        result="The reviews are positive on this product"
    elif(positive<negative and negative>neutral):
        result="The reviews are negative on this product"
    else:
        result="The reviews are neutral on this product"

    answer=np.array([positive,negative,neutral])
    explode=(0.2,0.1,0.05)
    review_labels=["Positive reviews","Negative Reviews","Neutral Reviews"]

    # Add rhe result to the pie chart 
    plt.pie(answer,labels=review_labels,explode=explode,autopct='%1.0f%%')
    plt.title("Result: "+result)
    plt.axis("equal")
    # save the pie chart with size of 15kb:
    plt.savefig("C:/Users/Kishor Balgi/OneDrive/Documents/UiPath/Flipkart Product Review Analysis/AnalysisChart.png",dpi=70)
    plt.show()

main()



