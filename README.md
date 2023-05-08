# UL-Standards-Classify


<b> 1. Data Collection </b>- Scrape UL Standards data from https://www.shopulstandards.com/Catalog.aspx?UniqueKey=1 <br>
 - <b> Scraper_UL_standards.py <br><b>
 - <b> End Result: UL-Standards-List.csv <b>
 
  
<b> 2. Data Cleaning before Analysis <b> <br>
- Preprocess.ipynb <br> 
  - Removed duplicates separated by / in each description
  - Removed Spanish from description that contains Spanish 
  - Extracted type of standard from the description ('Standard', 'Test', 'Method', 'Outline', 'Procedure' and etc.) ans stored under column name "Category"
  - Applied YAKE algorithm as an unsupervised keyword extraction method for extracting keywords from each description (description saved under column name "Topic", which is the remainder after taking out the "Category" strings from the description. 
- End Result: Preprocessed.csv


  


