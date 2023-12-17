# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 04:36:22 2023

@author: metis
"""

from scholarly import scholarly
def makale_al(konu):
    # Belirli bir anahtar kelimeyle ilgili en çok atıf alan 20 makaleyi getirme
    search_query = scholarly.search_pubs(konu)  # Arama sorgusu buraya yazılabilir
    dizi=[]
    for i in range(50):  # İlk 20 makaleyi listeleme
        article = next(search_query)
        dizi.append(article['bib']['title']+" | Atıf Sayısı: "+str(article['num_citations']))
    return dizi