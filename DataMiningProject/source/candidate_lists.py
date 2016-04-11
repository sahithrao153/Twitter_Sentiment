import csv
import re,string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def punctuation(tokenized_docs_list1):
    tokenized_docs_no_punctuation=[]
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    for review in tokenized_docs_list1:
        new_review = []
        for token in review:
            new_token = regex.sub(u'', token)
            if not new_token == u'':
                new_review.append(new_token)
        tokenized_docs_no_punctuation.append(new_review)
    return tokenized_docs_no_punctuation


def stop_words(tokenized_docs_no_punctuation):
    tokenized_docs_no_stopwords = []
    for doc in tokenized_docs_no_punctuation:
        new_term_vector = []
        for word in doc:
            if not word in stopwords.words('english'):
                new_term_vector.append(word)
        tokenized_docs_no_stopwords.append(new_term_vector)
    return tokenized_docs_no_stopwords

def main():
    list1=[]
    list2=[]
    list3=[]
    with open('../data/raw_tweets.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            searchObj = re.search( r'GOPDebate', row[0], re.M|re.I)
            if searchObj:
                is_trump = re.search( r'trump', row[0], re.M|re.I)
                is_donald = re.search( r'donald', row[0], re.M|re.I)
                is_mark =  re.search( r'mark', row[0], re.M|re.I)
                is_rubio = re.search( r'rubio', row[0], re.M|re.I)
                is_kashich =  re.search( r'kashich', row[0], re.M|re.I)
                is_john =  re.search( r'john', row[0], re.M|re.I)
                row=str(row)
                row = re.sub(r"http\S+", "", row)
                row=row.strip('\n')
                if is_donald or is_trump:
                    list1.append(row)
                if is_mark or is_rubio:
                    list2.append(row)
                elif is_kashich or is_john:
                    list3.append(row)

    print len(list1)
    print len(list2)
    print len(list3)
    tokenized_docs_list1 = [word_tokenize(doc,language='english') for doc in list1]
    tokenized_docs_list2 = [word_tokenize(doc,language='english') for doc in list2]
    tokenized_docs_list3 = [word_tokenize(doc,language='english') for doc in list3]

    tokenized_docs_no_punctuation_1=punctuation(tokenized_docs_list1)
    tokenized_docs_no_punctuation_2=punctuation(tokenized_docs_list2)
    tokenized_docs_no_punctuation_3=punctuation(tokenized_docs_list3)
    ##Remove punctuation

    #print tokenized_docs_no_punctuation
    tokenized_docs_no_stopwords1=stop_words(tokenized_docs_no_punctuation_1)
    tokenized_docs_no_stopwords2=stop_words(tokenized_docs_no_punctuation_2)
    tokenized_docs_no_stopwords3=stop_words(tokenized_docs_no_punctuation_3)
    for j in tokenized_docs_no_stopwords3:
        print j

if __name__ == '__main__':
    main()
