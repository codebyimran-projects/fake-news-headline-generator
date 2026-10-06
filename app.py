import random
import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Fake News Headline Generator",
    layout="centered"
)


# =========================================================
# NEWS DATA
# =========================================================

news_data = {

    "Technology": {

        "subjects": [
            "Scientists",
            "Engineers",
            "Researchers",
            "Tech Experts",
            "Developers",
            "AI Researchers",
            "Technology Companies"
        ],

        "actions": [
            "Discover",
            "Reveal",
            "Develop",
            "Launch",
            "Create",
            "Announce",
            "Uncover",
            "Introduce"
        ],

        "topics": [
            "a mysterious technology",
            "a revolutionary machine",
            "a secret AI system",
            "a powerful new computer",
            "a strange device",
            "a futuristic robot",
            "a new energy source",
            "an advanced smartphone"
        ]
    },


    "Science": {

        "subjects": [
            "Scientists",
            "Researchers",
            "Astronomers",
            "Biologists",
            "Physicists",
            "Medical Researchers",
            "Science Experts"
        ],

        "actions": [
            "Discover",
            "Detect",
            "Reveal",
            "Confirm",
            "Uncover",
            "Identify",
            "Announce",
            "Find"
        ],

        "topics": [
            "a mysterious signal",
            "a new species",
            "an unknown planet",
            "a strange biological phenomenon",
            "a hidden ocean",
            "a mysterious substance",
            "an unusual discovery",
            "a new form of energy"
        ]
    },


    "Sports": {

        "subjects": [
            "Football Stars",
            "Cricket Players",
            "Local Teams",
            "Sports Experts",
            "Championship Teams",
            "Famous Athletes",
            "Team Coaches"
        ],

        "actions": [
            "Break",
            "Announce",
            "Reveal",
            "Achieve",
            "Celebrate",
            "Create",
            "Claim",
            "Discover"
        ],

        "topics": [
            "a shocking new record",
            "an unbelievable victory",
            "a secret training method",
            "a surprising strategy",
            "a historic achievement",
            "an unexpected championship",
            "a mysterious sports technique",
            "a record-breaking performance"
        ]
    },


    "World": {

        "subjects": [
            "Government Officials",
            "World Leaders",
            "International Experts",
            "Officials",
            "Global Researchers",
            "News Agencies",
            "International Scientists"
        ],

        "actions": [
            "Announce",
            "Reveal",
            "Confirm",
            "Discover",
            "Launch",
            "Introduce",
            "Uncover",
            "Declare"
        ],

        "topics": [
            "a surprising new plan",
            "a secret international project",
            "a mysterious agreement",
            "a major global discovery",
            "an unexpected decision",
            "a strange new policy",
            "a shocking international event",
            "a revolutionary global project"
        ]
    }
}


# =========================================================
# SESSION STATE
# =========================================================

if "headlines" not in st.session_state:
    st.session_state.headlines = []


# =========================================================
# DARK THEME
# =========================================================

st.markdown(
    """
    <style>

    /* Application */

    .stApp {
        background-color: #080808;
        color: #ffffff;
    }

    .block-container {
        max-width: 850px;
        padding-top: 55px;
        padding-bottom: 50px;
    }


    /* Hide Streamlit branding */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }


    /* Main title */

    .app-title {
        text-align: center;
        color: #ffffff;
        font-size: 44px;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 10px;
    }

    .app-subtitle {
        text-align: center;
        color: #777777;
        font-size: 16px;
        margin-bottom: 40px;
    }


    /* Generator panel */

    .panel {
        background-color: #111111;
        border: 1px solid #242424;
        border-radius: 16px;
        padding: 28px;
        margin-bottom: 20px;
    }


    /* Streamlit labels */

    label {
        color: #dddddd !important;
        font-weight: 600 !important;
    }


    /* Select box */

    div[data-baseweb="select"] > div {
        background-color: #181818 !important;
        border: 1px solid #303030 !important;
        color: #ffffff !important;
        border-radius: 9px !important;
    }


    /* Buttons */

    .stButton > button {
        width: 100%;
        height: 46px;
        background-color: #ffffff !important;
        color: #080808 !important;
        border: none !important;
        border-radius: 9px !important;
        font-weight: 700 !important;
    }

    .stButton > button:hover {
        background-color: #dcdcdc !important;
        color: #000000 !important;
    }


    /* Results heading */

    .results-title {
        color: #ffffff;
        font-size: 24px;
        font-weight: 700;
        margin-top: 35px;
        margin-bottom: 18px;
    }


    /* Disclaimer */

    .disclaimer {
        text-align: center;
        color: #555555;
        font-size: 12px;
        margin-top: 40px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="app-title">Fake News Headline Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="app-subtitle">'
    'Generate fictional headlines by combining random subjects, actions, and topics.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# GENERATOR SETTINGS
# =========================================================

# st.markdown(
#     '<div class="panel">',
#     unsafe_allow_html=True
# )

category = st.selectbox(
    "News Category",
    list(news_data.keys())
)

number_of_headlines = st.slider(
    "Number of Headlines",
    min_value=1,
    max_value=10,
    value=3
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# BUTTONS
# =========================================================

generate_col, clear_col = st.columns(2)


with generate_col:

    generate_button = st.button(
        "Generate Headlines",
        use_container_width=True
    )


with clear_col:

    clear_button = st.button(
        "Clear Results",
        use_container_width=True
    )


# =========================================================
# CLEAR
# =========================================================

if clear_button:

    st.session_state.headlines = []

    st.rerun()


# =========================================================
# GENERATE
# =========================================================

if generate_button:

    data = news_data[category]

    st.session_state.headlines = []

    for _ in range(number_of_headlines):

        subject = random.choice(data["subjects"])

        action = random.choice(data["actions"])

        topic = random.choice(data["topics"])

        headline = f"{subject} {action} {topic}"

        st.session_state.headlines.append(
            {
                "headline": headline,
                "category": category
            }
        )


# =========================================================
# RESULTS
# =========================================================

if st.session_state.headlines:

    st.markdown(
        '<div class="results-title">Generated Headlines</div>',
        unsafe_allow_html=True
    )

    for item in st.session_state.headlines:

        # Actual Streamlit text
        st.subheader(item["headline"])

        st.caption(
            f"{item['category']} / Fictional News"
        )

        st.divider()


else:

    st.write(
        "Select a category and click Generate Headlines."
    )


# =========================================================
# DISCLAIMER
# =========================================================

st.markdown(
    """
    <div class="disclaimer">
        Fictional content generated for educational and entertainment purposes.
    </div>
    """,
    unsafe_allow_html=True
)