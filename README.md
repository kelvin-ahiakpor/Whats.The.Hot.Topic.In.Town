# What's The Hot Topic in Topic Town?
## Information Retrieval & Natural Language Processing
A deep learning project to find trending news in African countries

**Contributors:** Kelvin K. Ahiakpor & Emmanuel A. Acquaye

**Institution:** Ashesi University

**Contact:** kelvin.ahiakpor@ashesi.edu.gh, emmanuel.acquaye@ashesi.edu.gh


### Overview
This project addresses the rampant spread of misinformation and disinformation through credible news reporting using Natural Language Processing (NLP) and Hugging Face Transformers. It aims to provide verified, insightful, and tailored information by analyzing news and understanding underlying sentiments. 
### Application Demo
Link to application demo: [App Video Demo](https://www.youtube.com/watch?v=0HMjTxKRbaI) 

### Interactive app link
Link to interactive app: [Interactive App](https://www.youtube.com/watch?v=0HMjTxKRbaI)

### How to run
1. Ensure a strong and stable internet connection, you may follow the setup first for local hosting here [here](#Setup)
2. Click the link to open the [Interactive App](https://whats-the-hot-topic-in-town.streamlit.app/). If the app is asleep, gently wake it up.
3. Navigate to the drop down list, click `SEARCH` and type your African country
4. Wait about 2 minutes to get news, sentiment analysis and summaries.
5. Note, the more vibrant your country is, the more likely it is that we will have to process more data.
6. If scraping is taking a while, please hang on.
7. Thank you

### Setup (For local hosting)
Ensure you have the following libraries installed:  
`tensorflow`   
`opencv-python`  
`pandas`   
`numpy`   
`streamlit`   
`scrapy`   
`pycountry`   
`twisted`   
`transformers`   
`scikit-learn`   
`torch`   
`evaluate`  
`accelerate`  
You may use the following command:  
`!pip install tensorflow opencv-python pandas numpy streamlit scrapy pycountry twisted transformers scikit-learn torch evaluate accelerate`

### Features
- **Web Scraping:** Scrape news AllAfrica
- **News Display:** Show top 10 news headlines with one-paragraph summaries and allow users to click links to desired articles
- **Summarize News Articles:** Fine-tune the BERT base cased model from Hugging Face with labeled datasets of news articles to generate summaries.
- **Sentiment Analysis:** Apply sentiment analysis tools to understand and display the emotional tone of news articles.
- **Deploy Functional App:** Use Streamlit to build an interactive and responsive web application.

### Technology Stack
Python: Main programming language.  
Requests & Scrapy: For scraping web content.  
Sqlite3: For interacting with the SQL database.  
Transformers: For applying natural language processing tasks.  



