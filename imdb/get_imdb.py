import numpy as np

def load_imdb(path, shuffle=True, random_state=42):
    import glob 
    print("Loading the imdb data")
    
    train_neg_files = glob.glob(path+"/train/neg/*.txt")
    train_pos_files = glob.glob(path+"/train/pos/*.txt")
    
    X_train_corpus = []
    y_train = []
    
    for tnf in train_neg_files:
        f = open(tnf, 'r', encoding="utf8")
        line = f.read()
        #line = line[:len(line)/2]
        X_train_corpus.append(line)
        y_train.append(0)
        f.close()
    
    for tpf in train_pos_files:
        f = open(tpf, 'r', encoding="utf8")
        line = f.read()
        #line = line[:len(line)/2]
        X_train_corpus.append(line)
        y_train.append(1)
        f.close()
    
    print("Train Data loaded.")
    
    test_neg_files = glob.glob(path+"/test/neg/*.txt")
    test_pos_files = glob.glob(path+"/test/pos/*.txt")
    
    X_test_corpus = []
    y_test = []
    
    for tnf in test_neg_files:
        f = open(tnf, 'r', encoding="utf8")
        X_test_corpus.append(f.read())
        y_test.append(0)
        f.close()
    
    for tpf in test_pos_files:
        f = open(tpf, 'r', encoding="utf8")
        X_test_corpus.append(f.read())
        y_test.append(1)
        f.close()
    
    print("Test Data loaded.")
    
    y_train = np.array(y_train)
    y_test = np.array(y_test)
    
    if shuffle:
        np.random.seed(random_state)
        indices = np.random.permutation(len(y_train))       
        
        #X_train = X_train.tocsr()
        #X_train_corpus = X_train_corpus[indices]
        X_train_corpus = [X_train_corpus[i] for i in indices]
        y_train = y_train[indices]
        #train_corpus_shuffled = [train_corpus[i] for i in indices]
        
        indices = np.random.permutation(len(y_test))
        
        #X_test = X_test.tocsr()
        #X_test_corpus = X_test_corpus[indices]
        X_test_corpus = [X_test_corpus[i] for i in indices]
        y_test = y_test[indices]
        #test_corpus_shuffled = [test_corpus[i] for i in indices]
    #else:
        #train_corpus_shuffled = train_corpus
        #test_corpus_shuffled = test_corpus
    
    return X_train_corpus, y_train, X_test_corpus , y_test



def vectorize_data():
    # load data from path
    path = r"/mnt/d/IIT/ML/dataset/aclImdb"
    X_train_corpus , y_train, X_test_corpus , y_test = load_imdb(path)
    
    # vectorize data
    from sklearn.feature_extraction.text import CountVectorizer
    
    token = r"(?u)\b[\w\'/]+\b"
    vectorizer = CountVectorizer(token_pattern=token)
    
    print("Vectorizing data")
    X_train_vector = vectorizer.fit_transform(X_train_corpus)
    X_test_vector = vectorizer.transform(X_test_corpus)
    
    return X_train_vector, y_train, X_test_vector , y_test
    
    
    

    
    


