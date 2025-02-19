![Banner](https://github.com/kelvin-ahiakpor/kelvin-ahiakpor.github.io/blob/main/images/hottopic1.png)
# What's The Hot Topic in Topic Town?
## Information Retrieval & Natural Language Processing
A deep learning project to find trending news in African countries

**Contributors:** Kelvin K. Ahiakpor & Emmanuel A. Acquaye

**Institution:** Ashesi University

**Contact:** kelvin.ahiakpor@ashesi.edu.gh, emmanuel.acquaye@ashesi.edu.gh


### Overview
This project addresses the rampant spread of misinformation and disinformation through credible news reporting using Natural Language Processing (NLP) and Hugging Face Transformers. It aims to provide verified, insightful, and tailored information by analyzing news and understanding underlying sentiments. 
This project automates the extraction, summarization from "All Africa", storing all scraped news data in an SQLLite3 database. It is designed to provide on-the-go accessible news reporting to individuals, journalists, and social trend enthusiasts with trending news topics in African countries.
### Application Demo
Link to application demo: [App Video Demo](https://youtu.be/g32Ly-Z1nrk) 

### Interactive app link
Link to interactive app: [Interactive App](https://whats-the-hot-topic-in-town.streamlit.app/)

### How to run
1. Ensure a strong and stable internet connection, you may follow the setup first for local hosting [here](#Setup)
2. Click the link to open the [Interactive App](https://whats-the-hot-topic-in-town.streamlit.app/). If the app is asleep, gently wake it up, otherwise reboot the app!
3. Navigate to the drop down list, click `SEARCH` and type your African country
4. Wait about 2 minutes to get news, sentiment analysis and summaries.
5. Note, the more news your country has, the more likely it is that we will have to process more data.
6. If scraping is taking a while, please hang on.
7. Thank you

### Setup
1. Ensure you have the following libraries installed:  
`tensorflow`   
`opencv-python`  
`pandas`   
`numpy`   
`streamlit`   
`scrapy`   
`pycountry`   
`beautifulsoup4`   
`transformers`   
`scikit-learn`   
`torch`   
`evaluate`  
`accelerate`  
You may use the following command:  
`!pip install tensorflow opencv-python pandas numpy streamlit scrapy pycountry beautifulsoup4 transformers scikit-learn torch evaluate accelerate`
2. Download the contents of this repository, specifically the `bert2bertMK` and `newsscraper` folders and store in a folder, ex. `Hot Topics`
3. Open a terminal at the folder you stored and use this command `streamlit run home.py`
4. For mac users, edit all relative directories in the home.py with `./` to `../`
5. Enjoy finding the hot topics in your town.

### Features
- **Web Scraping:** Scrape news AllAfrica
- **News Display:** Show top 10 news headlines with one-paragraph summaries and allow users to click links to desired articles
- **Summarize News Articles:** Fine-tune the BERT base cased model from Hugging Face with labeled datasets of news articles to generate summaries.
- **Sentiment Analysis:** Apply sentiment analysis tools to understand and display the emotional tone of news articles.
- **Deploy Functional App:** Use Streamlit to build an interactive and responsive web application.

### Technology Stack
- **Python**: Main programming language.  
- **Requests & BeautifulSoup**: For scraping web content.  
- **Sqlite3**: For interacting with the SQL database.  
- **Transformers**: For applying natural language processing tasks.  

### Notebooks
The notebooks used to execute this project are in the repository. They are split into 5 phases, however, you may read the integrated version. Also, feel free to view the project proposal and rubric.

### Special Thanks
Dr. Tatenda Kavu   
Kweku Yamoah   
Silas Sangmin 

![Banner](https://github.com/kelvin-ahiakpor/kelvin-ahiakpor.github.io/blob/main/images/hottopic2.png)



