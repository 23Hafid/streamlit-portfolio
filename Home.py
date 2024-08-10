import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
from PIL import Image
import base64
from io import BytesIO
from streamlit_extras.let_it_rain import rain
from streamlit_extras.stylable_container import stylable_container

# Custom color palette
colors = {
    'primary': '#bf8065',
    'secondary': '#541f1f',
    'accent': '#901f3b',
    'background': '#ffffff',
    'light': '#ffdbdb',
    'medium': '#ff9d9d',
    'dark': '#ffc0c0'
}


def get_experience(year):
    """
    Retrieve experiences for a given year.

    Args:
    year (int): The year to get experiences for.

    Returns:
    dict: A dictionary of experiences for the given year.
    """
    experiences = {
        2017: {
            "October": "🏅 Completed my SPM with results of 5As and 4Bs."
        },
        2018: {
            "April": "🎓 Started my journey at Selangor College Matriculation."
                     "\n\n- First exposure to programming(Java), leading to pursuit of IT-related degree."
        },
        2019: {
            "April": "🏅 Graduated from Selangor College Matriculation with a CGPA of 3.84.",
            "August": "🎓 Began my studies at Universiti Teknologi MARA (UiTM) pursuing a Bachelor of Information Systems (Hons.) in Intelligent Systems Engineering."
                      "\n\n- This program offers two specializations: Big Data and Intelligent Computing that covers disciplines like Business Intelligence, Analytics, Enterprise Resource Planning, and Software Development."
        },
        2020: {
            "January": "🦉 Began learning the German language as it is a requirement to take a third language subject at UiTM."
        },
        2021: {},
        2022: {
            "July": "💻 Completed my Final Year Project titled 'Sentiment Analysis on COVID-19 Booster Vaccines'.",
            "September": "💼 Started my internship at Xeersoft Sdn. Bhd as a Software Developer Intern."
                         "\n\n- Full-stack developer role contributing to Xeersoft ERP system development, enhancement, and debugging using PHP, JavaScript, and SQL."
        },
        2023: {
            "January": "🏅 Completed internship at Xeersoft Sdn. Bhd."
                       "\n\n🏅 Graduated from UiTM with First Class Honours in Information Systems (Hons.) Intelligent Systems Engineering.",
            "February": "💼 Returned to Xeersoft Sdn. Bhd. as a Junior Software Developer."
                        "\n\n- Worked on developing and enhancing the Xeersoft ERP system, focusing on various modules such as Inventory and Accounting using PHP, JavaScript, and SQL."
                        "\n\n- Contributed to API development in Slim framework."
                        "\n\n- Collaborated with cross-functional teams to deliver high-quality software solutions."
                        "\n\n- Optimized application performance and ensured code quality through rigorous testing and debugging."
                        "\n\n- Redesigned the system dashboard to improve user engagement and enable more informed business decisions."
        },
        2024: {
            "March": "🦉 Began learning the Japanese language for the love of 'The Apothecary Diaries' 🔥🔥🔥.",
            "May": "🎓 Joined the Yayasan Peneraju - Peneraju Teknologi Fullstack Java Professional Train and Upskill Program."
                   "\n\n- This program provides comprehensive training in full-stack development using Java, hands-on experience with Spring Boot, and preparation for obtaining Oracle Certified Foundation Associate and Oracle Certified Professional Java Developer certifications."
        }
    }
    return experiences.get(year, {})


def style_image(image_path, max_width="100%"):
    """
    Apply styling to an image.

    Args:
    image_path (str): Path to the image file.
    max_width="100%" : size of the image container.

    Returns:
    str: HTML string with styled image.
    """
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    html = f'''
    <style>
        .img-container {{
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            max-width: {max_width};
            width: 100%;
            height: auto;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .img-container:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }}
        .rounded-img {{
            width: 100%;
            height: auto;
            object-fit: cover;
            border-radius: 15px;
            transition: all 0.3s ease;
        }}
        .rounded-img:hover {{
            filter: brightness(1.1);
        }}
    </style>
    <div class="img-container">
        <img src="data:image/png;base64,{img_str}" class="rounded-img">
    </div>
    '''
    return html


def create_skill_tags(skills, title=None):
    """
    Create skill tags with styling.

    Args:
    skills (list): List of skill names.
    title (str, optional): Title for the skills section.
    """
    st.markdown(f"""
    <style>
        .skill-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 15px;
        }}
        .skill-tag {{
            background-color: {colors['light']};
            color: {colors['secondary']};
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 0.8em;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }}
        .skill-tag:hover {{
            background-color: {colors['medium']};
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            transform: translateY(-2px);
        }}
    </style>
    """, unsafe_allow_html=True)

    if title:
        st.subheader(title)

    tags_html = "".join([f'<div class="skill-tag">{skill}</div>' for skill in skills])
    st.markdown(f'<div class="skill-container">{tags_html}</div>', unsafe_allow_html=True)


def cherry_blossom_animation():
    """Generate HTML/CSS for cherry blossom header animation."""
    return """
    <style>
    .petal {
        position: absolute;
        background-color: #FFB7C5;
        border-radius: 150% 0 150% 0;
        animation: falling 10s infinite;
    }
    @keyframes falling {
        0% { top: -10%; transform: rotate(0deg); }
        100% { top: 100%; transform: rotate(720deg); }
    }
    </style>
    <div id="petals"></div>
    <script>
    function createPetal() {
        const petal = document.createElement('div');
        petal.classList.add('petal');
        petal.style.left = Math.random() * 100 + '%';
        petal.style.width = Math.random() * 10 + 5 + 'px';
        petal.style.height = Math.random() * 10 + 5 + 'px';
        petal.style.animationDuration = Math.random() * 5 + 5 + 's';
        document.getElementById('petals').appendChild(petal);
        setTimeout(() => petal.remove(), 10000);
    }
    setInterval(createPetal, 300);
    </script>
    """


def setup_page_config():
    """Set up the page configuration."""
    st.set_page_config(page_title="Hafidzahidah Binti Wangit", layout="wide")
    st.components.v1.html(cherry_blossom_animation(), height=50)

    # Body CSS
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;700&display=swap');

        h1, h2, h3, h4, h5, h6 {{
            font-family: 'Quicksand', sans-serif;
            color: {colors['secondary']};
        }}
        .big-font {{
            font-size: 40px !important; 
            font-weight: bold; 
            font-family: 'Comfortaa', cursive;
            color: {colors['primary']};
            text-align: center;
        }}
        .medium-font {{
            font-size: 30px !important; 
            font-family: 'Pacifico', cursive;
            color: {colors['secondary']};
            text-align: center;
        }}
        .small-font {{
            font-size: 16px !important; 
            font-family: 'Quicksand', sans-serif;
            color: {colors['secondary']};
        }}
        .job-font {{
            font-size: 20px !important; 
            font-family: 'Comfortaa', cursive;
            color: {colors['secondary']};
            text-align: center;
        }}
        .stButton>button {{
            background-color: {colors['light']};
            color: {colors['secondary']};
            border: 2px solid {colors['primary']};
            border-radius: 20px;
            padding: 10px 20px;
        }}
        .stSidebar {{
            background-color: {colors['light']};
        }}
        .card {{
            background-color: {colors['background']};
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }}
        .centered {{
            text-align: center;
        }}
    </style>
    """, unsafe_allow_html=True)


def sidebar():
    """Create and populate the sidebar."""
    with st.sidebar:
        col1, col2, col3 = st.columns(3)
        with col2:
            st.image("./image/maomao.jpg")

        # Navigation
        selected = option_menu(
            menu_title=None,
            options=["About", "Projects"],
            icons=["person", "code-slash"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": colors['light']},
                "icon": {"color": colors['secondary'], "font-size": "25px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                             "--hover-color": colors['medium']},
                "nav-link-selected": {"background-color": colors['medium']},
            }
        )

        # Contact details
        st.sidebar.header("Contact Details")
        st.sidebar.write("Email: hafidzahidah@gmail.com")

        # Social media icons
        col1, col2, col3, col4, col5, col6 = st.sidebar.columns(6)
        linkedin_html = '''
        <a href="https://www.linkedin.com/in/hafidzahidah-w-098670198/" target="_blank">
            <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="30" height="30">
        </a>
        '''
        col2.markdown(linkedin_html, unsafe_allow_html=True)
        github_html = '''
        <a href="https://github.com/23Hafid" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="30" height="30">
        </a>
        '''
        col4.markdown(github_html, unsafe_allow_html=True)

        st.sidebar.markdown("---")

        # Download CV
        st.subheader("Download CV 📄")
        st.caption("Download My professional CV")
        with open("./Hafidzahidah_CV.pdf", "rb") as file:
            with stylable_container(
                    key="download_button",
                    css_styles="""
                    button {
                        background-color: #ff9d9d;
                        color: white;
                        border-color: #ff9d9d;
                        border-radius: 10px;
                    }
                    """,
            ):
                if st.download_button(
                        label="Download",
                        data=file,
                        file_name="Hafidzahidah_CV.pdf"
                ):
                    st.toast('Resume Downloded!', icon="😍")

        # Disclaimer
        st.sidebar.markdown("---")
        st.sidebar.caption(
            "Disclaimer: This portfolio is for streamlit demonstration purposes only.")

    return selected


def about_page():
    """Render the About page content."""
    st.markdown('<p class="medium-font">Hi! I am,</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">🌸Hafidzahidah Binti Wangit🌸</p>', unsafe_allow_html=True)
    st.markdown('<p class="job-font">Software Developer</p>', unsafe_allow_html=True)

    st.subheader("About Me")
    st.markdown(
        '<div class="small-font">I am a dedicated and hardworking software developer with knowledge and skills in various programming languages and technologies, who is eager to contribute to the success of the company and self-advancement.\n\nI have experience in PHP software development, machine learning projects in Python and created management system project in Java.</div>',
        unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("My Journey")

    timeline_year = st.select_slider("Select Year", options=range(2017, 2025))
    monthly_experiences = get_experience(timeline_year)

    if not monthly_experiences:
        st.markdown(f"""
            <div style="background-color: {colors['light']}; padding: 10px; border-radius: 5px; color: {colors['secondary']};">
                💤 No specific experiences recorded for {timeline_year}.
            </div>
            """, unsafe_allow_html=True)
    else:
        for month, experience in monthly_experiences.items():
            st.markdown(f"""
                <div style="background-color: {colors['light']}; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
                    <strong style="color: {colors['secondary']};">{month}:</strong>
                    <div style="color: {colors['accent']};">{experience}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown(
        "<p style='text-align: center; color: #888; font-style: italic;'>Check out this year's journey for cute suprise!</p>",
        unsafe_allow_html=True
    )

    # Cherry blossom emoji rain
    if timeline_year == datetime.now().year:
        rain(
            emoji="🌸",
            font_size=15,
            falling_speed=5,
            animation_length="infinite",
        )

    st.markdown("---")

    st.subheader("Skills")

    # First row of skills
    st.markdown(f"""
        <div style='display: flex; justify-content: space-around;'>
            <div style='background: {colors['light']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>Python 🐍</p>
            </div>
            <div style='background: {colors['background']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>Java ☕</p>
            </div>
            <div style='background: {colors['light']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>PHP 🐘</p>
            </div>
            <div style='background: {colors['background']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>SQL 🗄️</p>
            </div>
            <div style='background: {colors['light']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>HTML/CSS 🌐</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Second row of skills
    st.markdown(f"""
        <div style='display: flex; justify-content: space-around; margin-top: 20px;'>
            <div style='background: {colors['background']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>JavaScript 📜</p>
            </div>
            <div style='background: {colors['light']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>Spring Boot 🍃</p>
            </div>
            <div style='background: {colors['background']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>MySQL 🐬</p>
            </div>
            <div style='background: {colors['light']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>MongoDB 🍃</p>
            </div>
            <div style='background: {colors['background']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>SQLyog 🐬</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Third row of skills
    st.markdown(f"""
        <div style='display: flex; justify-content: space-around; margin-top: 20px;'>
            <div style='background: {colors['light']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>Git 🧰</p>
            </div>
            <div style='background: {colors['background']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>Github 🐙</p>
            </div>
            <div style='background: {colors['light']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>Selenium 🤖</p>
            </div>
            <div style='background: {colors['background']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>Power BI 📊</p>
            </div>
            <div style='background: {colors['light']}; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 18%;border: 2px solid {colors['primary']};'>
                <p style='font-size: 14px; color: {colors['secondary']};'>Figma 🎨</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("Language")

    # CSS for card styling
    st.markdown(f"""
        <style>
            .language-card {{
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: all 0.3s ease;
                cursor: pointer;
                background-color: {colors['light']};
            }}
            .language-card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
                background-color: {colors['dark']};
            }}
            .language-name {{
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 15px;
                color: {colors['secondary']};
                transition: color 0.3s ease;
            }}
            .language-card:hover .language-name {{
                color: {colors['accent']};
            }}
            .proficiency-bar {{
                height: 20px;
                border-radius: 10px;
                margin-bottom: 15px;
                transition: all 0.3s ease;
            }}
            .language-card:hover .proficiency-bar {{
                height: 22px;
            }}
            .proficiency-text {{
                font-size: 16px;
                color: {colors['primary']};
                transition: color 0.3s ease;
            }}
            .language-card:hover .proficiency-text {{
                color: {colors['secondary']};
            }}
        </style>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    languages = {
        "Malay": {"Speaking": "Native", "Writing": "Native", "Score": 100},
        "English": {"Speaking": "Fluent", "Writing": "Fluent", "Score": 80},
        "Japanese": {"Speaking": "Beginner", "Writing": "Beginner", "Score": 20},
        "German": {"Speaking": "Beginner", "Writing": "Beginner", "Score": 10}
    }

    for i, (language, data) in enumerate(languages.items()):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
                <div class="language-card">
                    <div class="language-name">{language}</div>
                    <div class="proficiency-bar" style="background-color: {colors['accent']}; width: {data['Score']}%;"></div>
                    <div class="proficiency-text">Speaking : {data['Speaking']}</div>
                    <div class="proficiency-text">Writing : {data['Writing']}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("Areas of Interest")
    st.markdown(
        '<div class="small-font">\n\n - I love EXO 💖.'
        '\n - Ongoing self-study of Japanese🏯 and German languages through Duolingo and YouTube. '
        '\n - Connect with me on Duolingo and motivate each other! @\_Kay___'
        '\n - Appreciation for diverse television genres, with a particular affinity for science fiction, action, fantasy, dystopian narratives, and historical dramas.'
        '\n - Favorite anime selections include Kimi Ni Todoke, Au Haru Ride, and The Apothecary Diaries.'
        '\n - Avid gaming enthusiast: Genshin Impact, Mobile Legends, Play Together</div>',
        unsafe_allow_html=True)

    # From GitHub KevzPeter / Duolingo-Stats-Card
    st.markdown("""
        <div style="display: flex; justify-content: center;">
            <img src="https://duolingo-stats-card.vercel.app/api?username=_Kay___&theme=dracula" alt="Duolingo Stats"/>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("Gallery")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(style_image("./image/exo.JPG"), unsafe_allow_html=True)
    with col2:
        st.markdown(style_image("./image/play_together.JPG"), unsafe_allow_html=True)
    with col3:
        st.markdown(style_image("./image/kiminitodoke.jpg"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "<p style='text-align: center; color: #888; font-style: italic;'>Have a nice day!</p>",
        unsafe_allow_html=True
    )


def projects_page():
    """Render the Projects page content."""
    st.title("Projects 🌟")

    st.caption(
        "Here are some of the projects I've worked on. For more projects and information, please [click here](https://drive.google.com/drive/folders/19y3QbREaLSkC-R5D7zhEChK0XPsMqsmT?usp=sharing)")

    # Project 1
    st.subheader("Project 1: Sentiment Analysis on COVID-19 Booster Vaccines, 2022")
    skills = ["Python", "NLTK", "Excel", "Power BI", "snscrape", "BeautifulSoup", "Selenium", "Data Analysis",
              "Machine Learning", "Visualization"]
    create_skill_tags(skills)
    st.write(
        "A machine learning project focused on sentiment analysis of public opinion on COVID-19 booster vaccines using Twitter data.")
    st.write(
        "\n - Analyzed over 80,000 data using Python (NLTK) and Excel"
        "\n - Conducted sentiment analysis, exploratory data analysis, and machine learning modeling"
        "\n - Leveraged Microsoft Power BI to transform raw data into visually appealing and meaningful representations to discover trends and insights."
        "\n - Created Python scripts that utilized snscrape and BeautifulSoup to collect data from Twitter, Shopee, and LinkedIn as well as used Selenium for handling dynamic content.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(style_image("./image/sentiment1.jpg"), unsafe_allow_html=True)
    with col2:
        st.markdown(style_image("./image/sentiment2.jpg"), unsafe_allow_html=True)
    with col3:
        st.markdown(style_image("./image/sentiment3.jpg"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Project 2
    st.subheader("Project 2: Pet Adoption Management System, 2024")
    skills = ["Java", "Spring Boot", "MySQL", "Spring Data JPA", "Spring Security", "Maven", "Thymeleaf"]
    create_skill_tags(skills)
    st.write(
        "A user-friendly, efficient pet adoption management system that streamlines the adoption process for both users and administrators, improving the overall experience and increasing successful pet adoptions."
        "\n\nThis was a group project task as required for Yayasan Peneraju Java Professional Program.")
    st.write(
        "\n - Engineered robust RESTful APIs"
        "\n - Implemented comprehensive features including login, signup, pet listings, adoption applications, application dashboards, and administrative functions"
        "\n - Utilized Thymeleaf templating engine, integrated MySQL database, and designed intuitive user and admin interfaces")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(style_image("./image/pet_adoption2.jpg"), unsafe_allow_html=True)
    with col2:
        st.markdown(style_image("./image/pet_adoption1.jpg"), unsafe_allow_html=True)
    with col3:
        st.markdown(style_image("./image/pet_adoption3.jpg"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)


def main():
    """Main function to run the Streamlit app."""
    setup_page_config()
    selected = sidebar()

    if selected == "About":
        about_page()
    elif selected == "Projects":
        projects_page()


if __name__ == "__main__":
    main()
