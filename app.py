import random
import streamlit as st


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Fake News Headline Generator",
    page_icon="📰",
    layout="centered"
)


# =========================
# NEWS DATA
# =========================

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
            "an unusual scientific discovery",
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


# =========================
# SESSION STATE
# =========================

if "headlines" not in st.session_state:
    st.session_state.headlines = []


# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main {
    max-width: 900px;
}

.hero {
    text-align: center;
    padding: 25px 10px 10px 10px;
}

.hero-title {
    font-size: 45px;
    font-weight: 800;
    margin-bottom: 5px;
}

.hero-text {
    font-size: 18px;
    color: #777;
}

.headline-card {
    padding: 22px;
    margin: 15px 0;
    border-radius: 14px;
    border: 1px solid #ddd;
    background-color: #fafafa;
    font-size: 22px;
    font-weight: 600;
}

.small-text {
    color: #777;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# HEADER
# =========================

st.markdown("""
<div class="hero">

<div class="hero-title">
📰 Fake News Headline Generator
</div>

<div class="hero-text">
Generate random fictional and satirical news headlines using Python.
</div>

</div>
""", unsafe_allow_html=True)


st.divider()


# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.header("⚙️ Generator Settings")

    category = st.selectbox(
        "Choose News Category",
        list(news_data.keys())
    )

    headline_count = st.slider(
        "Number of Headlines",
        min_value=1,
        max_value=10,
        value=1
    )

    st.divider()

    st.write("### 📊 Generator Info")

    st.write(f"Category: **{category}**")

    st.write(
        f"Available words: "
        f"**{len(news_data[category]['subjects']) + len(news_data[category]['actions']) + len(news_data[category]['topics'])}**"
    )


# =========================
# GENERATOR FUNCTION
# =========================

def generate_headline(category):

    data = news_data[category]

    subject = random.choice(data["subjects"])
    action = random.choice(data["actions"])
    topic = random.choice(data["topics"])

    return f"{subject} {action} {topic}"


# =========================
# GENERATE BUTTON
# =========================

if st.button(
    "🚀 Generate Headlines",
    use_container_width=True
):

    for _ in range(headline_count):

        headline = generate_headline(category)

        st.session_state.headlines.insert(0, {
            "category": category,
            "headline": headline
        })


# =========================
# DISPLAY CURRENT HEADLINES
# =========================

if st.session_state.headlines:

    st.subheader("✨ Generated Headlines")

    for item in st.session_state.headlines[:headline_count]:

        st.markdown(
            f"""
            <div class="headline-card">
                📰 {item["headline"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption(
            f"Category: {item['category']}"
        )


else:

    st.info(
        "Choose a category and click **Generate Headlines** to create your first headline."
    )


# =========================
# CLEAR HISTORY
# =========================

if st.session_state.headlines:

    st.divider()

    if st.button(
        "🗑️ Clear Generated Headlines",
        use_container_width=True
    ):
        st.session_state.headlines = []
        st.rerun()


# =========================
# FOOTER
# =========================

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#888;">
        Fake News Headline Generator • Built with Python & Streamlit
        <br>
        <span style="font-size:12px;">
        Fictional content for entertainment and educational purposes.
        </span>
    </div>
    """,
    unsafe_allow_html=True
)