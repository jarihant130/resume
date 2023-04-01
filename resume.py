import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Arihant Jain, Murex Consultant.
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Results-oriented MxML and Market data developer with 3+ years of experience at Aurionpro Solution Ltd. 
- Proficient in Murex, Python, Numpy, Pandas, Seaborn, Matplotlib, Scipy, Plotly, Selenium, HTML, CSS, Bootstrap, Angular `6`, Flask Framework (Basics), Database, and Eclipse IDE. 
- Skilled in developing and implementing complex financial models and data analytics solutions. 
- Proven ability to work collaboratively with cross-functional teams to deliver high-quality projects on time and within budget. 
- A detail-oriented professional with excellent problem-solving skills and a strong commitment to quality. 
- Holds a degree in Information Technology from `L.N.C.T.` Bhopal, (M.P.)
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.youtube.com/channel/UCeC088dyJsXK_L1bCHZDcjA" target="_blank">Arihant Jain</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certifications">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact">Contact</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a, b):
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)

def txt3(a, b):
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5,2,2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Bachelor\'s of Engineering (B.E.)** (Information Technology), *L.N.C.T*, Bhopal, (M.P.)',
'2015-2019')
st.markdown('''
- CGPA: `8.51`
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**MxML and Market Data Developer**, State Bank of India, Aurionpro Pvt. Ltd., Mumbai',
'JUL 22-Present')
st.markdown('''
- 
''')

txt('**Python Developer**, Intel Project (Content Management Team), Infosys Ltd., Pune',
'NOV 21-JUN 22')
st.markdown('''
- Working on professional content improvement for few of the Knowledge Articles and create an atuomation script.
- Our target is to provide the automation script for the existing content for professional and user friendly.
''')
txt('**IT Automation Developer**, Intel Project (ESD Team) , Infosys Ltd., Pune',
'NOV 20-OCT 21')
st.markdown('''
- Intel API maintenance for core Intel employees and external Intel employees.
- Provide the automation scripts for the applications that are divided into domains based on impact area, e.g., s/w, payment, etc.
- Team handles the software domain.
- Got [Insta Award](https://drive.google.com/file/d/1Iy_Qh9CwQrDpi24sdJri4vuaQaqcRnlU/view?usp=sharing) and cash award (in 3 months)
''')
txt('**Deveploer**, Data Science Python Project, Infosys Ltd., Pune',
'APR 20-NOV 20')
st.markdown('''
- Performing data analysis and feature engineering to create additional attributes which will be used in predictive models.
''')

txt('**System Engineer Trainee**, PackXprez, Infosys Ltd., Mysore',
'SEP 19 - FEB 20')
st.markdown('''
- Involved in developing backend using C#, ASP.Net, web API, ADO.Net , including Node JS & SQL Server.
- Involved in developing presentation logic and integration using Angular `6`.
- Involved in building a dynamic single page application using Angular `6`.
''')
st.markdown('''
### Internal Projects
''')
txt('**Developer**, Create Bot- AddFormulaColumnInExcel',
'MAY-JUN 20')
st.markdown('''
- Create a bot which adds a new column with the input formula in excel.
- Skills - **Microsoft Technologies | C#(C Sharp)**
''')
txt('**Developer**, Create Bot- CreatePivotTableInExcel',
'MAY-JUN 20')
st.markdown('''
- Create a bot which creates pivot table in excel on the inputs provided.
- Skills - **Microsoft Technologies | C#(C Sharp)**
''')

txt('**Developer**, Python Code Migration (`2.7` to `3.7`)',
'MAY-JUN 20')
st.markdown('''
- Python code migration for an upcoming Infosys product. The product is being developed as in Infosys Intellectual Property.
- Skills – **OpenSystem | Python – OpenSystem | Python**
''')
st.markdown('''
### Personal Projects
''')
txt('**Developer**, [Movie Browser](https://ng7-movie-browser.web.app/home)',
'APR-MAY 20')
st.markdown('''
- Involved in developing frontend using Angular `6`, HTML, CSS, Bootstrap & API.
- Involved in building a dynamic single page application using Angular `6`.
''')
txt('**Developer**, [Study Material Website](https://material-to-study.firebaseapp.com/)',
'APR-MAY 20')
st.markdown('''
- Involved in developing frontend using Angular `6`, HTML, CSS, Bootstrap & API.
- Involved in building a dynamic single page application using Angular `6`.
''')

txt('**Developer**, Chatbot Automation using Python',
'APR-MAY 20')
st.markdown('''
- Involved in developing automation enviroment using Selenium Framework.
- Involved automate Facebook profile, WhatsApp, auto reply feature, movie downloads, Text to Audio (Vice Versa), music (Offline /Online), emoji generator, password encryption in Social Media, System programs.
- Involved [Automate Zerodha Kite](https://www.youtube.com/playlist?list=PLcVqA0qm8vQ9E1bIMMmaoO8AxYXXMzViV), that will generate graph of Today’s Profit/Loss.
''')

txt('**Content Creator**, [Study Material YouTube Channel](https://www.youtube.com/channel/UCeC088dyJsXK_L1bCHZDcjA)',
'2015-Present')
st.markdown('''
- `3,100+` subscribers on YouTube
- Created `340` educational videos on Recuritment process, Government exam, Interview experiences, Certifications, Python Programming and projects, etc.
''')

txt('**Developer**, [Convert Anything](https://convertanything.streamlit.app/) on Streamlit Cloud',
'FEB 23-Present')
st.markdown('''
- It helps to convert any image file into different format.
- It also helps to download YouTube vidoes, generate passwords, trim videos, Online Python Interpreter and much more. 
''')

txt('**Technical Writer**, [Data Professor Blog](https://medium.com/@jarihant130) on Medium.com',
'2019-Present')
st.markdown('''
- Written `4` technical blogs on Data Science, Data Science Libraries and Python.
''')

#####################
st.markdown('''
## Certifications
''')
txt4('Python Associate', 'Infosys Certified Python Associate', '')
txt4('Python Level 1', 'Infosys Certified Python', '')
txt4('Data Science', 'Infosys Certified Data Science using Python Professional','')
txt4('Pythogorean Inertia', 'Pythogorean Inertia (Python) of Code Predators', 'https://drive.google.com/file/d/1in65Lnwc5n-hOwBVdV9v50nKQT9LWah0/view?usp=sharing')
txt4('AZ900', 'Microsoft Certified Azure Fundamentals','https://www.credly.com/users/arihant-jain.aa09554a/badges')
txt4('AI900', 'Microsoft Certified Azure AI Fundamentals', 'https://www.credly.com/badges/3489ae98-ae7b-4e6f-8bc4-dfb754c69068/public_url')
txt4('[PCEP-30-01]', 'PCEP – Certified Entry-Level Python Programmer', 'https://verify.openedg.org/?id=oUQc.GyYp.eUV9')

#####################
st.markdown('''
## Skills
''')
txt3('Financial Tool', '**`Murex`**')
txt3('Programming', '`Python`, `Angular 6`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('IDE', '`Eclipse`, `PyCharm`,`Visual Studio Code`')
txt3('Database', '`MS SQL Server`, `Oracle`')
txt3('Web development', '`Flask`, `HTML`, `CSS`, `Selenium`')
txt3('Model deployment', '`streamlit`')


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/arihantjain130/')
txt2('Twitter', 'http://twitter.com/@jarihant130')
txt2('GitHub', 'https://github.com/jarihant130')
txt2('YouTube', 'https://www.youtube.com/channel/UCeC088dyJsXK_L1bCHZDcjA')
txt2('Medium', 'https://jarihant130.medium.com/')
txt2('Telegram', 'https://t.me/studymaterial_1')
txt2('Gmail', 'jarihant130@gmail.com')

#####################
st.markdown('''
## Contact
''')
txt2('Address', 'Flat No-S01, 2nd Floor, Plot No-16, Hansa Apartment-5, Ward No-38, Ashoka Garden, Bhopal, (M.P.) 462023')
txt2('WhatsApp', 'https://web.whatsapp.com/send?phone=919685790871')
