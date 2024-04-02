# -*- coding: utf-8 -*-
"""
TFiDF 단어 생성기 : TfidfVectorizer  
  1. 단어 생성기(word tokenizer) & 단어 사전(word dictionary) 
  2. 문서단어행렬(DTM) : 단어 출현 비율에 의해서 가중치 적용 행렬 
    1) TF(Term Frequence) 가중치 : 단어출현빈도수  
    2) TFiDF(Term Frequence inver Document Frequence) 가중치 : 단어출현빈도수(TF) x 문서출현빈도수의 역수(iDF) 
"""

from sklearn.feature_extraction.text import TfidfVectorizer # 단어 생성기

# 테스트 문장 
sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
]

print(sentences)


# 1. 단어 생성기
obj = TfidfVectorizer() # 생성자 


# 2. 단어 사전 
fit = obj.fit(sentences) # 문장 적용 
voca = fit.vocabulary_ 

print(type(fit)) # <class 'sklearn.feature_extraction.text.CountVectorizer'>
print(type(voca)) # <class 'dict'>

print(voca)
'''
{'mr': 14, 'green': 5, 'killed': 11, 'colonel': 2, 'mustard': 15,
 'in': 9, 'the': 24, 'study': 23, 'with': 30, 'candlestick': 1, 
 'is': 10, 'not': 17, 'very': 25, 'nice': 16, 'fellow': 3,
 'professor': 21, 'plum': 20, 'has': 6, 'plant': 19, 'his': 8,
 'miss': 13, 'scarlett': 22, 'watered': 27, 'while': 29, 'he': 7,
 'was': 26, 'away': 0, 'from': 4, 'office': 18, 'last': 12, 'week': 28
'''

# 3. 문서단어행렬(DTM)
dtm = obj.fit_transform(sentences)
help(obj.fit_transform)
print(dtm)
'''
  (0, 3)	0.2205828828763741
  (0, 16)	0.2205828828763741
  (0, 25)	0.2205828828763741
  (0, 17)	0.2205828828763741
  (0, 10)	0.2205828828763741
  (0, 1)	0.2205828828763741
  (0, 30)	0.2205828828763741
  (0, 23)	0.1677589680512606
  (0, 24)	0.4411657657527482
  (0, 9)	0.1677589680512606
  (0, 15)	0.2205828828763741
  (0, 2)	0.2205828828763741
  (0, 11)	0.2205828828763741
  (0, 5)	0.26055960805891015
  (0, 14)	0.4411657657527482
  (1, 8)	0.3464378827197198
  (1, 19)	0.3464378827197198
  (1, 6)	0.4555241832708016
  (1, 20)	0.3464378827197198
  (1, 21)	0.3464378827197198
  (1, 23)	0.3464378827197198
  (1, 9)	0.3464378827197198
  (1, 5)	0.2690399207469689
  (2, 28)	0.27054287522550385
  (2, 12)	0.27054287522550385
  (2, 18)	0.27054287522550385
  (2, 4)	0.27054287522550385
  (2, 0)	0.27054287522550385
  (2, 26)	0.27054287522550385
  (2, 7)	0.27054287522550385
  (2, 29)	0.27054287522550385
  (2, 27)	0.27054287522550385
  (2, 22)	0.27054287522550385
  (2, 13)	0.27054287522550385
  (2, 8)	0.2057548299742193
  (2, 19)	0.2057548299742193
  (2, 20)	0.2057548299742193
  (2, 21)	0.2057548299742193
  (2, 5)	0.15978698032384395
'''

# scipy -> numpy 희소행렬 변경 
dtm_arr = dtm.toarray()
help(dtm.toarray())
print(dtm_arr)
'''
[[0.         0.22058288 0.22058288 0.22058288 0.         0.26055961
  0.         0.         0.         0.16775897 0.22058288 0.22058288
  0.         0.         0.44116577 0.22058288 0.22058288 0.22058288
  0.         0.         0.         0.         0.         0.16775897
  0.44116577 0.22058288 0.         0.         0.         0.
  0.22058288]
 [0.         0.         0.         0.         0.         0.26903992
  0.45552418 0.         0.34643788 0.34643788 0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.34643788 0.34643788 0.34643788 0.         0.34643788
  0.         0.         0.         0.         0.         0.
  0.        ]
 [0.27054288 0.         0.         0.         0.27054288 0.15978698
  0.         0.27054288 0.20575483 0.         0.         0.
  0.27054288 0.27054288 0.         0.         0.         0.
  0.27054288 0.20575483 0.20575483 0.20575483 0.27054288 0.
  0.         0.         0.27054288 0.27054288 0.27054288 0.27054288
  0.        ]]
'''

