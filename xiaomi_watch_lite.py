import re  
import csv
import time
import numpy as np
import requests
from urllib import request  
from bs4 import BeautifulSoup  
 
import io  
import sys 
 
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}  
 
print('Start Crawling...')
 
try:  
    data_list = []
    
    for r in range(197): 
        url_main="https://www.amazon.com/product-reviews/B08P57P577/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
        if r == 0:
            url=url_main
        else:
            page =r +1
            url ="https://www.amazon.com/product-reviews/B08P57P577/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}".format(page,page)
 
        req = requests.get(url, headers=header)  
        res = req.content
        soup = BeautifulSoup(res,'lxml') 
        blog_items = soup.findAll('div', class_='a-section review aok-relative')
        new_items = soup.findAll('div', class_='a-section review aok-relative')  
 
        for item in blog_items:  
            
            #ID
            ID = item.find('span','a-profile-name').text
            '''
            #Star Rating
            star_rating_content = item.find('span', class_='a-icon-alt').text
            star_rating = star_rating_content.split()[0]
            blog=star_rating 
            '''
            #Review_text
            review_text=item.find('span', class_='a-size-base review-text review-text-content').text
            
            #Title
            #Title = item.find('a','a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold').span.text
            
            #Date   
            date_content = item.find('span', 'a-size-base a-color-secondary review-date').text
            date = date_content.split()[6] + date_content.split()[7] + date_content.split()[8]
            
            data_list.append([ID, date, review_text])
        time.sleep(np.random.rand()*7)
 
finally:
    with open('xiaomi_watch_lite.csv', 'w', encoding='utf-8',  newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['ID','Date','Review_text'])
        for u in data_list:
            writer.writerow(u)
            
print('End Crawling')