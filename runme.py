# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:40:40 2015

@author: Quan, Sumin, Woohyuk, Gyuhyun
"""
import pandas as pd
import random
import urllib
import time
import subprocess 
import os
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#------------------------------------------------------------------------------
ultrasurf_p = subprocess.Popen('ultrasurf.exe', shell=True, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.STDOUT)
#------------------------------------------------------------------------------
target_url = ['https://scholar.google.co.uk', 	\
              'https://scholar.google.ca', 		\
              'https://scholar.google.co.nz', 	\
              'https://scholar.google.com.au'
              ]

#------------------------------------------------------------------------------
def extractNum(st):
	# TODO
    print st
    tmp = st.split( )
    num = ''
    anchor = filter(lambda ss: 'result' in ss, tmp)
    if anchor:
        pos = tmp.index(anchor[0]) -1 
        num = tmp[pos]
    else: 
        num = '0'
		
    return int(num)
#------------------------------------------------------------------------------
def getNumCitations(title):
        

    #Python code to open the ultrasurf application
    ultrasurf_p = subprocess.Popen('u1405.exe', shell=True, 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)
     
    while True:
     
        try:
# This snippet is grabbed from 
# http://remotalks.blogspot.kr/2013/10/an-alterntaive-to-changing-proxy-server.html
			# Thanks to Remo for the exception of ultrasurf
			
            # Insert your code that raises an exception when 
            # there is a need for a remote proxy server change
            # use_current_remote_proxy_server()

            s = 3
            for i in xrange(s,0,-1):
                time.sleep(1)
                print "Wait for starting proxy in ", i, "seconds"

            #--------------------------------------------------------------------------              
            # Open the url, randomly choose the browser to avoid blocking
            s = 0 #randint(0, 1)
            if s==0:
                driver = webdriver.Firefox()
            elif s==1:
                driver = webdriver.Chrome()

                
            # Randomly choose pick the scholar url from different countries to avoid blocking
            driver.get(random.choice(target_url)) # See pre-defined target_url
			
            # Resize the window to the screen width/height
            #driver.set_window_size(300, 500)
            
            # Move the window to position x/y
            #driver.set_window_position(500, 500)
            
            # Uncheck the include_patents
            elem = driver.find_element_by_name('as_sdtp') #gs_in_checkbox
            if elem.is_selected():
                elem.click()
            
            # Send the title to the box
            elem = driver.find_element_by_name("q")
            elem.send_keys(title)
            elem.send_keys(Keys.RETURN)
            
            # Get the link of the current desired paper            
            elem = driver.find_element_by_xpath("//div[@class='gs_fl']")            \
                         .find_element_by_css_selector('a')                         \
                         .get_attribute('href')   
            print elem
            
			# &lr=lang_en 	for excluding non-English documents
			# &as_vis=1		for excluding number of citations
			# &as_ylo=2011	for starting year of collection
			# &as_yhi=2011	for ending year of collection
			
			#-------------------------------------------------------------------------- 
            # 2011 - 2011
            # Open the new link
            new_url = elem+'&lr=lang_en&as_vis=1&as_ylo=2011&as_yhi=2011'
            driver.get(new_url)   
            #print new_url
            # Num citations in string
            st = driver.find_element_by_xpath("//div[@id='gs_ab_md']").text   
            citation_2011_2011 = extractNum(st)
            
            #print citation_2011_2011
            #-------------------------------------------------------------------------- 
            # 2012 - 2012
            # Open the new link
            new_url = elem+'&lr=lang_en&as_vis=1&as_ylo=2012&as_yhi=2012'
            driver.get(new_url)   
            
            # Num citations in string
            st = driver.find_element_by_xpath("//div[@id='gs_ab_md']").text   
            citation_2012_2012 = extractNum(st)
            
            #-------------------------------------------------------------------------- 
            # 2013 - 2013
            # Open the new link
            new_url = elem+'&lr=lang_en&as_vis=1&as_ylo=2013&as_yhi=2013'
            driver.get(new_url)   
            
            # Num citations in string
            st = driver.find_element_by_xpath("//div[@id='gs_ab_md']").text   
            citation_2013_2013 = extractNum(st)
                
            #-------------------------------------------------------------------------- 
            # 2014 - 2014
            # Open the new link
            new_url = elem+'&lr=lang_en&as_vis=1&as_ylo=2014&as_yhi=2014'
            driver.get(new_url)   
            
            # Num citations in string
            st = driver.find_element_by_xpath("//div[@id='gs_ab_md']").text   
            citation_2014_2014 = extractNum(st)
    

         
            #--------------------------------------------------------------------------    
            # Close the browser
            driver.close()
           
            
           
            # os.system("taskkill /im u1405.exe /")
            # os.system("taskkill /im chrome.exe /T")
            # os.system("taskkill /im firefox.exe /T")
            # os.system("taskkill /im opera.exe /T")
            # os.system("taskkill /im chromedriver.exe /T")
            # os.system("taskkill /im firefoxdriver.exe /T")
            # os.system("taskkill /im operadriver.exe /T")
			
            return [title,
                citation_2011_2011, \
                citation_2012_2012, \
                citation_2013_2013, \
                citation_2014_2014]
			#-------------------------------------------------------------------------- 
        except:
     
            # Kill/Close the currently running Ultrasurf application
			# Or we need to kill by hand (manually close) and current running browsers
            ultrasurf_p.kill()        
            ultrasurf_p.terminate()
            os.system("taskkill /im u1405.exe /T")
            # os.system("taskkill /im chrome.exe /T")
            os.system("taskkill /im firefox.exe /T")
            #Reopen the Ultrasurf application
            ultrasurf_p = subprocess.Popen('u1405.exe', shell=True, 
                                            stdout=subprocess.PIPE, 
                                            stderr=subprocess.STDOUT)
    #--------------------------------------------------------------------------        
   
    
#------------------------------------------------------------------------------
def extractConf(string_title, string_result):
    # First put all of the paper name in an xlsx file 
	# and parse it into a dataframe
    xlsx_file = pd.ExcelFile(string_title)
    
    df = xlsx_file.parse('Sheet1', index_col = None, header = None)
    
    # Print to test
    print df
    

    # Create a new data frame of output to hold the results
    # columns=['Title', '2011', '2012', '2013', '2014']
    df_dst = pd.DataFrame()    
    
	
    # Save to dataframe
    for t in range(len(df.index)):
    #for t in range(1): # debug purpose
        # Randomly wait
        # for i in xrange(s,0,-1):
            # time.sleep(1)
            # print "Wait in ", i, "seconds"
	
	
        title  = df[0][t] # Get the title
        print title
		
        output = getNumCitations(title)
        output = pd.Series(output)
        df_dst = df_dst.append(output.T, ignore_index=True)

		
		
		# s = s+randint(0, 60)
		# if s>=60:            s = 5
        print t, df_dst.ix[t]
		
	#Write to excel is not currently working
    #writer = pd.ExcelWriter('result.xlsx')
    #Write to csv     
    df_dst.to_csv(string_result, encoding='utf-8')
    
if __name__ == "__main__":		
	#extractConf("sigasia_2011_title.xlsx",		"sigasia_2011_result.csv")
	#extractConf("sigasia_2012_title.xlsx",		"sigasia_2012_result.csv")
	
	#extractConf("siggraph_2011_title.xlsx",		"siggraph_2011_result.csv")
	#extractConf("siggraph_2012_title.xlsx",		"siggraph_2012_result.csv")
	
	#extractConf("tog_2011_title.xlsx",		"tog_2011_result.csv")
	#extractConf("tog_2012_title.xlsx",		"tog_2012_result.csv")

	#extractConf("uist_2011_title.xlsx",		"uist_2011_result.csv")
	#extractConf("uist_2012_title.xlsx",		"uist_2012_result.csv")
	
	extractConf("vis_2011_title.xlsx",		"vis_2011_result.csv")
	extractConf("vis_2012_title.xlsx",		"vis_2012_result.csv")

	extractConf("chi_2011_title.xlsx",		"chi_2011_result.csv")
	extractConf("chi_2012_title.xlsx",		"chi_2012_result.csv")
	
	extractConf("eg_2011_title.xlsx",		"eg_2011_result.csv")
	extractConf("eg_2012_title.xlsx",		"eg_2012_result.csv")
	
	extractConf("miccai_2011_title.xlsx",		"miccai_2011_result.csv")
	extractConf("miccai_2012_title.xlsx",		"miccai_2012_result.csv")

	
	
