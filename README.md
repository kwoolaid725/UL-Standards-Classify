# UL-Standards-Classify


<b> 1. Data Collection </b>- Scrape UL Standards data from https://www.shopulstandards.com/Catalog.aspx?UniqueKey=1 <br>
 - <b> Scraper_UL_standards.py <br><b>
 - <b> End Result: UL-Standards-List.csv <b>
 
  
<b> 2. Data Cleaning before Analysis <b> <br>
- Preprocess.ipynb <br> 
  - Removed duplicates separated by / in each description
  - Removed Spanish from description that contains Spanish 
  - Extracted type of standard from the description ('Standard', 'Test', 'Method', 'Outline', 'Procedure' and etc.) and stored under column name "Category"
  - Applied YAKE algorithm as an unsupervised keyword extraction method for extracting keywords from each description (description saved under column name "Topic", which is the remainder after taking out the "Category" strings from the description. 
- End Result: Preprocessed.csv<img width="1247" alt="Screenshot 2023-05-08 at 2 28 16 PM" src="https://user-images.githubusercontent.com/107806433/236915416-1422c086-a42b-44e4-a9d2-6e97d243b618.png">

<img width="1472" alt="Screenshot 2023-05-08 at 2 26 51 PM" src="https://user-images.githubusercontent.com/107806433/236915462-455027bf-d5df-45bd-aee7-e02014077548.png">


  
<img width="1339" alt="Screenshot 2023-05-08 at 2 27 07 PM" src="https://user-images.githubusercontent.com/107806433/236915471-4d7f8526-509a-4830-9f48-c6c14040f40f.png">


