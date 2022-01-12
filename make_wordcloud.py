from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# wordcloud function
def word_cloud(text):
    stopwords = set(STOPWORDS)
    frame_mask=np.array(Image.open("cloud_shape.png"))
    wordcloud = WordCloud(max_words=50, mask=frame_mask, stopwords=stopwords, background_color="white").generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

# words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
# text = " ".join(words)

text = """
"Giving. What Does That Mean?. Getting Better at Uncertainty.
Contented Sigh. 
With Omicron Comes Uncertainty Here's How to Handle It. 
How Fast Can You Skydive?
The Sun, as Always, Came Out.
How Does It Work? What's Next?
Review: You're Not Alone.
Photos: Don't Say 'Old'.
Who Wants to Be Governor of New York?
They're Back, and Onstage.
Rush While Racing.
From 'Yes, and' to 'I Do' to 'Who the Heck Are You?'
Checking It Twice? 
Make This Parm.
Go Electric.
Worried About Inflation? Here's What That May Reveal About You.
Feed the Hungry? Let's Discuss
Un-screw-up-able.
If It's Omicron, a Minor Marketing Challenge.
Ahoy! Let's Look Back on 2021, When We Couldn't Stop Looking Back.
Inflation Has Arrived Here's What You Need to Know.
Meadows and the Band of Loyalists: How They Fought to Keep Trump in Power.
To Flummox or Not to Flummox.
What Happens if You Test Positive While Traveling?
It's Not How Much You Fly, It's How Much You Spend.
Omicron Is Spreading Fast Can New York Do More to Slow It Down?
Closing In on the Great One.
Americans are tired, and Omicron is just beginning.
Can Schools Handle Omicron?
How We're Holding It Together. 
Wrangling the Unwrangleable
Drama! TikTok Made Them Famous Figuring Out What's Next Is Tough.
What We're Looking Forward To in 2022.
When Should I Test? What If I Can't Find One?
Tech Won Now What?
'Sober Curious'? Chatty. 
Worldly, Charming, and Quietly Equipping a Brutal Military.
In the Premier League, There's No Looking Back.
Quietly, but Less So. Falling in Love.
What We Forgot to Talk About in 2021.
You Ready? Stay or Go? 
What to Expect When You're Expecting: Supply Chain Issues.
Here's What to Watch.
At Home and Away Readers' Best of 2021.Tell Us About It.
Ungerrymandered: Everything One Needs.
What Do You Think You Should Be Paid?
They Could Be Anything They Want (Together).
In 2021, It Got Pricier.
"""

word_cloud(text)