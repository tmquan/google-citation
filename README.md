# Google citation package

This project is aimed to help UNIST CSE department to collect the citation data for reputation conferences. 

**Disclaimer: ** It does not mean to violate the Term of Uses from Google Scholar, please use it as your own risk

After several checking, we decided to put 2 levels of proxy servers so that it is more flexible to avoid blocking effect from Google Scholar. Those related packages are 
`psiphon3.exe` and `u1405.exe`

----------

Initialy, launch psiphon3.exe to activate the first proxy level. 

This python scrip `runme.py` which collects the citation numbers of predefined papers, includes the exception whenever we are banned from google and the seond proxy level. In that case, we need to manually click onto another proxy server of Ultrasurf software (http://ultrasurf.us/ or can be cloned via this repo) 
This executable file must be put in the same folder with python script and input .xlsx file (contains only the paper names in one column)

The input of the script can be modified hardcodely (i.e., `uist-2011-title.xlsx` )
The name of output file `uist-2011-result.csv` also need to be modified hardcodely. 

Then invoking the python scrip runme.py to collect the citation numbers of predefined papers which have been put in one-column of excel file. 

Regarding to the option uncheck the box "Including patent", it will be handle by python

	# Uncheck the include_patents
	elem = driver.find_element_by_name('as_sdtp') #gs_in_checkbox
	if elem.is_selected():
		elem.click()
 
Regarding to the uncheck number of citations box, after fetching the url, append to that link with &as_vis=1 will do that job. For example: (more detail can be found in the script)


	# 2011 - 2011
	# Open the new link
	new_url = elem+'&lr=lang_en&as_vis=1&as_ylo=2011&as_yhi=2011'
	driver.get(new_url)   
	#print new_url
	# Num citations
	st = driver.find_element_by_xpath("//div[@id='gs_ab_md']").text   
	print st
	citation_2011_2011 = st

Keep in mind that you need to monitor the blocking notation and frequently change the options either from psiphon3 or u1405. You may need to kill u1405 manually if necessary. 

----------

For any concern, please drop me an email via quantm@unist.ac.kr     