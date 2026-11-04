import streamlit as st
import random

# 1. إعدادات الصفحة الأساسية بطابع بوليسي تحذيري
st.set_page_config(
    page_title="مكتب التحقيق: المحقق زقزوقي", 
    page_icon="🕵️‍♂️", 
    layout="centered"
)

# 2. كود الـ CSS لتصميم واجهة زقزوقي (أسود، أصفر تحذيري، وأحمر للقصف)
st.markdown("""
    <style>
    .stApp {
        background-color: #0d0f14;
        color: #ffffff;
    }
    .police-badge {
        background-color: #ffcc00;
        color: #000000;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-weight: bold;
        font-size: 24px;
        border: 3px solid #000000;
        margin-bottom: 25px;
        box-shadow: 0px 0px 15px rgba(2ff, 204, 0, 0.4);
        direction: rtl;
    }
    .roast-box {
        background-color: #ff3333;
        color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        border: 2px solid #ffffff;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0px 0px 15px rgba(255, 51, 51, 0.5);
        direction: rtl;
    }
    div.stButton > button:first-child {
        background-color: #ffcc00 !important;
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border: 2px solid #000000 !important;
        border-radius: 8px !important;
        width: 100% !important;
        padding: 10px !important;
    }
    div.stButton > button:hover {
        background-color: #e6b800 !important;
        box-shadow: 0px 0px 10px #ffcc00 !important;
    }
    /* ضبط القوائم والمدخلات لتكون متناسقة جهة اليمين */
    .stSelectbox, .stTextInput, .stNumberInput, p, h1, h2, h3, label {
        direction: rtl !important;
        text-align: right !important;
    }
    </style>
""", unsafe_allow_html=True)

# بنك التحقيق والقصف الخاص بالمحقق زقزوقي
zaqzouqi_database = {
    "الاسم": [
        "اسمك شيك، بصح المحضر نتاعك يوحي بالهجرة غير الشرعية نحو الفشل الدراسي! 📄",
        "حتى دالة الـ input تعبت وهي تقرأ هذا الاسم البائس برمجياً! 🖥️",
        "الاسم ما شاء الله، والواقع يحتاج لإعادة صياغة وفرمطة شاملة لجبهتك العريضة! 💥"
    ],
    "المهنة/الدراسة": [
        "تدرس آداب وفلسفة؟ وتكتب 4 صفحات سفسطة في الفرض بدون جملة واحدة مفيدة! عقلك يحتاج لـ فرمطة! 🧠",
        "بما أنك في هذه السنة، البكالوريا تقترب وأنت مازلت تظنها مجرد إشاعة أطلقتها الوزارة! 📚",
        "سنتك الدراسية الحالية تعاني من سكتة قلبية ونومك المستمر هدم الأمن الفكري للقسم بالكامل! 🛌"
    ],
    "الهواية": [
        "الهواية نتاعك هذي تحتاج إلى 'System Update' عاجل لأنها تستهلك طاقة والنتيجة صفر! 🎮",
        "تضيع الوقت وتسميها هواية؟ المحقق زقزوقي يسجل هذه الجريمة في ملف الـ Junk للويندوز فوراً! 🗑️",
        "هواية جميلة، لكن لو استثمرت هذا الوقت في مراجعة كرامتك الدراسية لكان أفضل! 💥"
    ],
    "المعدل الدراسي": [
        "هذا المعدل لا يصلح حتى ليكون نسبة شحن بطارية هاتف قديم! ارفع كرامتك البرمجية شوية! 📉",
        "معدل يوحي بأنك واقف في وضعية Format مستمر منذ بداية السنة الدراسية! 💀",
        "أستاذ المعلوماتية يبحث عن بقايا كرامتك الدراسية في ملفات الـ Cache بسبب هذا المعدل! 🔎"
    ]
}

# 3. واجهة التطبيق
st.markdown('<div class="police-badge">🕵️‍♂️ مَكْتَبْ التَّحْقِيقْ الصَّارِمْ: المُحَقِّقْ زَقْزُوقِي 🕵️‍♂️</div>', unsafe_allow_html=True)

st.write("أهلاً بك في زنزانة الاستجواب. أنا **المحقق زقزوقي**، خبير في كشف الحقائق وقصف الجبهات بدون رحمة.")
st.write("اختر مجال التحقيق الذي تريد أن أستجوبك فيه من القائمة بالأسفل، واستعد لتلقي الصدمة!")

st.markdown("---")

# خيارات التحقيق في الأسفل التفاعلية
st.subheader("📁 اختر ملف التحقيق والاستجواب:")
choice = st.selectbox(
    "ما هو الموضوع الذي تريد أن يحقق فيه زقزوقي الآن؟",
    ["اختر ملفاً...", "👤 التحقيق في هويتك واسمك", "📚 الاستجواب حول سنتك الدراسية ومهنتك", "🎨 التحقيق في هواياتك وتضييع وقتك", "📊 كشف حقيقة معدلك الدراسي الأخير"]
)

# معالجة الاختيارات وعرض صناديق القصف التفاعلية
if choice == "👤 التحقيق في هويتك واسمك":
    name_input = st.text_input("اكتب اسمك الحقيقي هنا للمحضر:")
    if st.button("💥 ابدأ الاستجواب وقصف الهوية"):
        if name_input:
            roast = random.choice(zaqzouqi_database["الاسم"])
            st.markdown(f'<div class="roast-box">🕵️‍♂️ المحقق زقزوقي يقصف جبهة {name_input}:<br><br>{roast}</div>', unsafe_allow_html=True)
        else:
            st.warning("المحقق زقزوقي يرفض استجواب شخص مجهول! اكتب اسمك.")

elif choice == "📚 الاستجواب حول سنتك الدراسية ومهنتك":
    grade_input = st.selectbox("اختر مستواك الحالي بكل صراحة:", ["الأولى ثانوي", "الثانية ثانوي (آداب وفلسفة)", "الثانية ثانوي (علوم تجريبية)", "الثالثة ثانوي (بكالوريا ريبوت)", "جامعي عاطل عن العمل"])
    if st.button("💀 اضغط لاستلام التقرير النووي"):
        roast = random.choice(zaqzouqi_database["المهنة/الدراسة"])
        st.markdown(f'<div class="roast-box">🕵️‍♂️ تقرير المحقق زقزوقي عن ({grade_input}):<br><br>{roast}</div>', unsafe_allow_html=True)

elif choice == "🎨 التحقيق في هواياتك وتضييع وقتك":
    hobby_input = st.text_input("ما هي الهواية التي تضيع فيها وقتك الثمين؟")
    if st.button("🔍 تحليل الجريمة الهوايتية"):
        if hobby_input:
            roast = random.choice(zaqzouqi_database["الهواية"])
            st.markdown(f'<div class="roast-box">🕵️‍♂️ زقزوقي يحلل هواية ({hobby_input}):<br><br>{roast}</div>', unsafe_allow_html=True)
        else:
            st.warning("اكتب هوايتك لكي لا يضع لك زقزوقي تهمة عشوائية!")

elif choice == "📊 كشف حقيقة معدلك الدراسي الأخير":
    score_input = st.number_input("أدخل معدلك الأخير (من 20) بدون تزوير:", min_value=0.0, max_value=20.0, value=10.0, step=0.5)
    if st.button("💥 قصف الجبهة المعدلية"):
        roast = random.choice(zaqzouqi_database["المعدل الدراسي"])
        st.markdown(f'<div class="roast-box">🕵️‍♂️ المحقق زقزوقي يفحص معدل ({score_input}):<br><br>{roast}</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("🚨 تم إعداد المحضر والتدمير بواسطة المطور المشاغب **AssoumiDev** 🚨")
