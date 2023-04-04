import streamlit as st
from PIL import Image
from base64 import b64encode

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">', unsafe_allow_html=True)


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
# Header 
st.write('''
# Arihant Jain, *Murex Consultant*
##### *Resume* 
''')

image = open('media/dp.png', "rb").read()

st.markdown(
    f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{b64encode(image).decode()}" style="text-align:center; width:200px;height:200px;"></div>',
    unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Summary", "Education", "Work Experience", "Certifications", "Skills", "Awards & Recognitions", "Social Media", "Contacts"])

with tab1:
    st.info('''
- Results-oriented MxML and Market data developer with 3+ years of experience at Aurionpro Solution Ltd. 
- Proficient in Murex, Python, Numpy, Pandas, Seaborn, Matplotlib, Scipy, Plotly, Selenium, HTML, CSS, Bootstrap, Angular `6`, Flask Framework (Basics), Database, and Eclipse IDE. 
- Skilled in developing and implementing complex financial models and data analytics solutions. 
- Proven ability to work collaboratively with cross-functional teams to deliver high-quality projects on time and within budget. 
- A detail-oriented professional with excellent problem-solving skills and a strong commitment to quality. 
- Holds a degree in Information Technology from `L.N.C.T.` Bhopal, (M.P.)
''')    

with tab2:
    txt('**Bachelor\'s of Engineering (B.E.)** (Information Technology), *L.N.C.T*, Bhopal, (M.P.)', '2015-2019')
    st.markdown('''
- CGPA: `8.51`
''')

with tab3:
    txt('**MxML and Market Data Developer**, State Bank of India, Aurionpro Pvt. Ltd., Mumbai',
'JUL 22-Present')
    st.markdown('''
    - Led a team of four members in developing new workflows and addressing production issues in Murex for SBI client.
    - Conducted thorough analysis of existing workflows and production issues, identifying pain points and areas for improvement.
    - Developed detailed project plan, including scope, timelines, milestones, and deliverables, and ensured effective communication and collaboration among team members.
    - Monitored project progress and made adjustments as needed to ensure on-time and within-budget completion.
    - Successfully upgrading Murex from version 35 to 55, ensuring seamless integration with existing systems and minimizing downtime.
    - Preparing test cases for testing new Murex environment.
    - Got [Employee of the Quarter](https://drive.google.com/file/d/17_wnhZd9p4LPRg3HRbgw_UuxmFYR9oEl/view?usp=share_link), and cash award (in first Quarter)
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
    txt('**Developer**, Data Science Python Project, Infosys Ltd., Pune',
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
    #############
    ### Internal Projects
    ############
    with st.expander("Internal Project"):
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

    #############
    ### Personal Projects
    ############
    with st.expander("Personal Project"):
        # col1, col2 = st.columns([4,1])
        txt('**Developer**, [Movie Browser](https://ng7-movie-browser.web.app/home)', 'APR-MAY 20')
            # st.write('**Developer**, [Movie Browser](https://ng7-movie-browser.web.app/home)')
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

        txt('**Technical Writer**, [Arihant Jain Blog](https://medium.com/@jarihant130) on Medium.com',
        '2019-Present')
        st.markdown('''
        - Written `4` technical blogs on Data Science, Data Science Libraries and Python.
        ''')
    
with tab4:
    txt4('Python Associate', 'Infosys Certified Python Associate', '')
    txt4('Python Level 1', 'Infosys Certified Python', '')
    txt4('Data Science', 'Infosys Certified Data Science using Python Professional','')
    txt4('Pythogorean Inertia', 'Pythogorean Inertia (Python) of Code Predators', 'https://drive.google.com/file/d/1in65Lnwc5n-hOwBVdV9v50nKQT9LWah0/view?usp=sharing')
    txt4('AZ900', 'Microsoft Certified Azure Fundamentals','https://www.credly.com/users/arihant-jain.aa09554a/badges')
    txt4('AI900', 'Microsoft Certified Azure AI Fundamentals', 'https://www.credly.com/badges/3489ae98-ae7b-4e6f-8bc4-dfb754c69068/public_url')
    txt4('[PCEP-30-01]', 'PCEP – Certified Entry-Level Python Programmer', 'https://verify.openedg.org/?id=oUQc.GyYp.eUV9')

with tab5:
    txt3('Financial Tool', '**`Murex`**(`MxML`, `Market Data`, `VaR`) `module`')
    txt3('Programming', '`Python`, `Angular 6`')
    txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
    txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
    txt3('IDE', '`Eclipse`, `PyCharm`,`Visual Studio Code`')
    txt3('Database', '`MS SQL Server`, `Oracle`')
    txt3('Web development', '`Flask`, `HTML`, `CSS`, `Selenium`')
    txt3('Model deployment', '`streamlit`')

with tab6:
    txt3('Infosys Ltd.', '[Insta Awards](https://drive.google.com/file/d/1Iy_Qh9CwQrDpi24sdJri4vuaQaqcRnlU/view?usp=share_link)')
    txt3('Aurionpro Solution Ltd.', '[Employee of the Quarter](https://drive.google.com/file/d/17_wnhZd9p4LPRg3HRbgw_UuxmFYR9oEl/view?usp=share_link)')
    
with tab7:
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    linkedin = open('media/Linkedin.png', "rb").read()
    twitter = open('media/Twitter.png', "rb").read()
    gitHub = open('media/Github.png', "rb").read()
    youtube = open('media/Youtube.png', "rb").read()
    medium = open('media/Medium.png', "rb").read()
    telegram = open('media/Telegram.png', "rb").read()
    gmail = open('media/Gmail.png', "rb").read()
    
    with col1:
        st.markdown(
            f'<a href="https://www.linkedin.com/in/arihantjain130/"><img src="data:image/png;base64,{b64encode(linkedin).decode()}" style="width:30px;height:30px;"></a>', unsafe_allow_html=True)
    with col2:
        st.markdown(
            f'<a href="http://twitter.com/@jarihant130"><img src="data:image/png;base64,{b64encode(twitter).decode()}" style="width:30px;height:30px;"></a>', unsafe_allow_html=True)
    with col3:
        st.markdown(
            f'<a href="https://www.linkedin.com/in/arihantjain130/"><img src="data:image/png;base64,{b64encode(gitHub).decode()}" style="width:30px;height:30px;"></a>', unsafe_allow_html=True)
    with col4:
        st.markdown(
            f'<a href="https://www.youtube.com/channel/UCeC088dyJsXK_L1bCHZDcjA"><img src="data:image/png;base64,{b64encode(youtube).decode()}" style="width:30px;height:30px;"></a>', unsafe_allow_html=True)
    with col5:
        st.markdown(
            f'<a href="https://jarihant130.medium.com/"><img src="data:image/png;base64,{b64encode(medium).decode()}" style="width:30px;height:30px;"></a>', unsafe_allow_html=True)
    with col6:
        st.markdown(
            f'<a href="https://t.me/studymaterial_1"><img src="data:image/png;base64,{b64encode(telegram).decode()}" style="width:30px;height:30px;"></a>', unsafe_allow_html=True)   
    with col7:
        st.markdown(
            f'<a href="mailto:jarihant130@gmail.com"><img src="data:image/png;base64,{b64encode(gmail).decode()}" style="width:30px;height:30px;"></a>', unsafe_allow_html=True)

with tab8:
    txt2('Address', ':round_pushpin: Flat No-S01, 2nd Floor, Plot No-16, Hansa Apartment-5, Ward No-38, Ashoka Garden, Bhopal, (M.P.) 462023')
    txt2('WhatsApp', ':telephone_receiver:[+91-9685790871](https://web.whatsapp.com/send?phone=919685790871)')

