import streamlit as st

# Title of the web app
st.title('HeroKimit: Your Assistant to Learn About Ancient Egypt هيروكيميت: مساعدك الرقمي لتعلم الحضارة المصرية القديمة')

st.image('bot.jpeg')

col1, col2, col3 = st.columns([2, 1, 2])  # The middle column (col2) is twice as wide

# Add the button inside the middle column (col2)
with col2:
    if st.button("Go to Login"):
        st.switch_page("pages/login.py")


# Display a brief introductory message in Egyptian Arabic dialect
st.markdown("""
# مرحبا في هيروكيميت
ده مساعدك لو عايز تتعلم عن مصر القديمة.
لو إنت حابب تعرف عن الفراعنة، الأهرامات، أو حتى حياة المصريين زمان، إحنا هنا عشان نساعدك.

من خلال هيروكيميت هتكتشف أسرار الحضارة المصرية القديمة، وكل ما هو مثير عن الفراعنة، الدين، والفن اللي كانوا بيعيشوا بيه.

## ليه هيروكيميت?
احنا هنا علشان نبسطلك المعلومات ونتكلم معاك زي ما بنتكلم مع بعض في حياتنا اليومية. هنسهّل عليك الفهم بالعربية البسيطة عن الموضوعات دي كلها.

إستعد لرحلة مليانة بالمعرفة والمتعة!
""")

# Add some more content to provide context about the site
st.markdown("""
### دي شوية معلومات تقدر تستفيد بيها:
- الحضارة المصرية القديمة واحدة من أقدم وأعظم الحضارات في التاريخ.
- المصريين الأوائل أسسوا نظم كتابة متقدمة، زي الهيروغليفية.
- أهرامات الجيزة تعتبر من عجائب الدنيا السبع القديمة.

وتأكد إنك مش لوحدك، هنبقى معاك في كل خطوة لو حابب تعرف أكتر!
""")

# You can include an image if needed
# st.image('path_to_image.jpg', caption='Explore the wonders of Ancient Egypt')

# Footer with a brief description
st.markdown("""
## هاتمشي معانا في سفر طويل وممتع للتعرف على حضارة مصر.
""")