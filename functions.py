from bs4 import BeautifulSoup
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
import pandas as pd
import requests
import pickle
import spacy
nlp = spacy.load('en_core_web_lg')


text_kmeans = pickle.load( open( "text_kmeans.p", "rb" ) )   
cluster_kmeans = pickle.load( open( "cluster_kmeans.p", "rb" ) )  
scaler = pickle.load( open( "scaler.p", "rb" ) ) 
tfidf_vectorizer = pickle.load( open( "tfidf_vectorizer.p", "rb" ) )

df_books = pd.read_csv('./static/df_books_3845_finale.csv')

def get_books(link):


    cluster_num = get_cluster(link)
    print('-------------------------')
    print(cluster_num)
    print('-------------------------')
    books = df_books[df_books['cluster'] == cluster_num ].sample(3)
    
    books = books.reset_index()
    # get genre
    genre_list = ['Other Genre', 'Business Books', 'Fantasy', 'Fiction',
           'Food & Cookbooks', 'Graphic Novels & Comics', 'Historical Fiction',
           'History & Biography', 'Horror', 'Humor', 'Memoir & Autobiography',
           'Middle Grade & Children\'s', 'Mystery & Thriller', 'Nonfiction',
           'Paranormal Fantasy', 'Picture Books', 'Poetry', 'Romance',
           'Science & Technology', 'Science Fiction', 'Travel & Outdoors',
           'Young Adult', 'Young Adult Fantasy & Science Fiction',
           'Young Adult Fiction']
    
    books['genre'] = ''
    for i in range(len(books)): 
        for col in genre_list:
            if books.iloc[i][col] == 1:
                books.loc[i,'genre'] = col
                # print(col)


    return books.iloc[0],books.iloc[1],books.iloc[2]


def spacy_tokenizer(document):
    tokens = nlp(document)
    tokens = [token.lemma_ for token in tokens if (
        token.is_stop == False and \
        token.is_punct == False and \
        token.lemma_.strip()!= '')]
    return tokens

def get_year(str):
    num = ''
    for i in str:
        if i.isdigit():
            num += i
        else:
            num = ''
        if len(num) == 4:
            return num

def get_user_data(link):
    url = link
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")    

    
    user_book = pd.DataFrame(index=[0], columns=['title', 'num_ratings','num_reviews', 'rating', 'num_pages', 'num_editions','year', 'Other Genre', 'Business Books', 'Fantasy', 'Fiction','Food & Cookbooks', 'Graphic Novels & Comics', 'Historical Fiction','History & Biography', 'Horror', 'Humor', 'Memoir & Autobiography','Middle Grade & Children\'s', 'Mystery & Thriller', 'Nonfiction','Paranormal Fantasy', 'Picture Books', 'Poetry', 'Romance','Science & Technology', 'Science Fiction', 'Travel & Outdoors','Young Adult', 'Young Adult Fantasy & Science Fiction','Young Adult Fiction', 'cluster_books'])
    user_book = user_book.fillna(0)

    # title
    try:
        t = soup.select('#bookTitle')[0].get_text()
        t = t.replace('[[','').replace(']]','').replace('\n','').rstrip().lstrip()
        user_book['title'][0]= str(t)
    except:
         user_book['title'][0]= None

    # num_rating
    try:
        n_rating = soup.select('#bookMeta > a:nth-child(7)')[0].get_text()
        n_rating = n_rating.replace(' ratings', '').replace(',','')
        user_book['num_ratings'][0]= int(n_rating)
    except:
        user_book['num_ratings'][0] = None
      
    # num_reviews
    try:
        review = soup.select('#bookMeta > a:nth-child(9)')[0].get_text()
        review = review.replace(' reviews', '').replace(',','')
        user_book['num_reviews'][0] = int(review)
    except:
        user_book['num_reviews'][0] =None

    # rating 
    try:
        rate = soup.select('#bookMeta > span:nth-child(2)')[0].get_text()
        user_book['rating'][0] =float(rate)
    except:
        user_book['rating'][0] = None

    # num_pages
    try:
        pag = soup.select('#details > div:nth-child(1) > span:nth-child(2)')[0].get_text()
        pag = pag.replace(' pages', '').replace('.', '')
        user_book['num_pages'][0] =int(pag) 
    except:
        user_book['num_pages'][0] =None

    # num_editions
    try:
        edit = soup.select('#bookDataBox > div.infoBoxRowTitle.otherEditions > div > a')[0].get_text()
        edit_num = ''
        for i in edit:
            if i.isdigit():
                edit_num += i
        edit = int(edit_num)   
        user_book['num_editions'][0] =int(edit)
    except:
        user_book['num_editions'][0] =None

    # year
    try:
        y = soup.select('#details > div:nth-child(2)')[0].get_text()
        y = get_year(y)
        user_book['year'][0] = int(y)
    except:
        user_book['year'][0] = None       
      
    # category

    try:
        genre_list = ['Other Genre', 'Business Books', 'Fantasy', 'Fiction',
           'Food & Cookbooks', 'Graphic Novels & Comics', 'Historical Fiction',
           'History & Biography', 'Horror', 'Humor', 'Memoir & Autobiography',
           'Middle Grade & Children\'s', 'Mystery & Thriller', 'Nonfiction',
           'Paranormal Fantasy', 'Picture Books', 'Poetry', 'Romance',
           'Science & Technology', 'Science Fiction', 'Travel & Outdoors',
           'Young Adult', 'Young Adult Fantasy & Science Fiction',
           'Young Adult Fiction']
        
        g = soup.select('body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.rightContainer > div:nth-child(6) > div > div.bigBoxBody > div > div:nth-child(1) > div.left > a')[0].get_text()
        g = g.replace('[[\n ','').replace('\n]]','')
        
        
        for genre in genre_list:
            if g in genre_list:
                if g == genre:
                    user_book[genre][0] = 1
                else:
                    user_book[genre][0] = 0 
            else:                
                user_book[genre][0] = 0
                user_book['Other Genre'][0] = 1

    except:
        for elem in genre_list:
            user_book[elem][0] = 0
            user_book['Other Genre'][0]

    # description

    try:
        descr = soup.select('#description > span:nth-child(2)')[0].get_text()
        descr = descr.replace('\n', ' ')
        descr = [descr]         
        descr = tfidf_vectorizer.transform(descr)  
        cluster_book = text_kmeans.predict(descr)
        user_book['cluster_books'][0] = int(cluster_book)
    except:
        user_book['cluster_books'][0] = None  
     
    return user_book    

def get_cluster(user_book_link):
    user_book = get_user_data(user_book_link)
    user_book = user_book.drop(columns=['title'])

    # scale the data
    X_num = scaler.transform(user_book)

    # build into dataframe
    X_num = pd.DataFrame(X_num, columns=user_book.columns)

    # get cluster
    clusters = cluster_kmeans.predict(X_num)
    X_num["cluster"] = clusters
    return int(X_num['cluster'])

