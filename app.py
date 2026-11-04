import streamlit as st
import random

# 1. إعدادات الصفحة الأساسية بطابع تحذيري
st.set_page_config(
    page_title="تحذير: بوت قصف الجبهات", 
    page_icon="⚠️", 
    layout="centered"
)

# 2. كود الـ CSS لتصميم واجهة مرعبة ومخصصة بالأصفر والأسود التحذيري
st.markdown("""
    <style>
    .stApp {
        background-color: #111111;
        color: #ffffff;
    }
    .warning-box {
        background-color: #ffcc00;
        color: #000000;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-weight: bold;
        font-size: 24px;
        border: 4px dashed #000000;
        margin-bottom: 25px;
        box-shadow: 0px 0px 15px #ffcc00;
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
        box-shadow: 0px 0px 10px #ff3333;
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
        color: #000000 !important;
        box-shadow: 0px 0px 10px #ffcc00 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. إدارة واجهات التطبيق والبيانات عبر الـ Session State
if "page" not in st.session_state:
    st.session_state.page = 1
if "level" not in st.session_state:
    st.session_state.level = ""
if "roast_msg" not in st.session_state:
    st.session_state.roast_msg = ""

# بنك القصف المخصص لكل سؤال وحسب مستويات الصدمة
roasts_database = {
    "name": {
        "خفيف": ["اسمك جميل، لكنه الخيار الوحيد الجميل في ملفك الدراسي بالكامل!", "حتى دالة الـ input أصيبت بالملل وهي تقرأ هذا الاسم."],
        "متوسط": ["اسمك يوحي بالهيبة، لكن معدلك الأخير في ثانوية بار بن قانة يوحي بالهجرة غير الشرعية!", "الاسم شيك والواقع بائس.. جبهتك طارت لبلدية قلتة زرقاء من الآن!"],
        "قوي": ["هذا الاسم يجب أن يُدرج في ملفات الـ Junk للويندوز فوراً متبوعاً بقصف نووي!", "صاحب هذا الاسم يملك جبهة عريضة تتسع لتخزين كود ذكاء اصطناعي كامل وبجودة 4K!"]
    },
    "age": {
        "خفيف": ["عمرك 15 سنة؟ ما زلت صغيراً على هذا الحجم من الدمار البرمجي المفاجئ!", "في هذا السن يفترض أنك تدرس، وليس واقفاً هنا تتلقى الإهانات من بوت!"],
        "متوسط": ["عمرك مناسب جداً لتستيقظ من غيبوبتك الدراسية وتبتعد عن السرير قسرياً!", "بهذا العمر وعقلك مازال يعاني من فقر دم برمجى حاد وفي وضعية Format مستمر!"],
        "قوي": ["بهذا السن وجبهتك ممسوحة تماماً.. أستاذة المعلوماتية تبحث عن بقايا كرامتك الدراسية في ملفات الـ Cache!", "عمرك صغير لكن ذنوبك الدراسية كافية لتشفير حاسوبك بـ فيروس الفدية!"]
    },
    "grade": {
        "خفيف": ["تدرس في هذه السنة? كان الله في عون الأساتذة الذين يحاولون فك شفرات خطك السري!", "سنتك الدراسية تحتاج إلى تحديث نظام (System Update) عاجل."],
        "متوسط": ["هذه السنة مصيرية، وأنت تقضيها في هز رأسك للأستاذ متظاهراً بالفهم العميق كأنك أرسطو!", "بما أنك في هذه السنة، البكالوريا تقترب وأنت مازلت تظنها مجرد إشاعة أطلقتها الوزارة!"],
        "قوي": ["أنت تدرس آداب وفلسفة في هذه السنة وتكتب 4 صفحات سفسطة في الفرض بدون جملة واحدة مفيدة.. عقلك يحتاج لـ فرمطة شاملة!", "سنتك الدراسية الحالية تعاني من سكتة قلبية ونومك المستمر هدم الأمن الفكري للقسم بالكامل!"]
    }
}

# -------------------------------------------------------------
# الواجهة 1: الواجهة الرئيسية والتعريف بالبوت
# -------------------------------------------------------------
if st.session_state.page == 1:
    st.markdown('<div class="warning-box">⚠️ تَحْذِيرْ: أُدْخُلْ عَلَى مَسْؤُولِيتِكَ.. بُوتْ يَقْصِفْ جَبْهَتَكْ! ⚠️</div>', unsafe_allow_html=True)
    st.title("💥 بوت قصف الجبهات العالمي v2.0")
    st.write("أهلاً بك في منصة الدمار الشامل القائمة على تدمير كرامة المستخدمين بذكاء ساخر وخفة دم جزائرية.")
    st.write("تحت رعاية المطور المشاغب الحصري: **AssoumiDev** 😎")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚪 دخول إلى البوت"):
        st.session_state.page = 2
        st.rerun()

# -------------------------------------------------------------
# الواجهة 2: اختيار مستويات القصف
# -------------------------------------------------------------
elif st.session_state.page == 2:
    st.title("⚙️ اختر مستوى الصدمة والدمار")
    st.write("حدد قوة القصف التي تستطيع جبهتك تحملها قبل البدء الاستجواب:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🟢 خفيف"):
            st.session_state.level = "خفيف"
            st.session_state.page = 3
            st.rerun()
    with col2:
        if st.button("🟠 متوسط"):
            st.session_state.level = "متوسط"
            st.session_state.page = 3
            st.rerun()
    with col3:
        if st.button("🔴 قوي (نووي)"):
            st.session_state.level = "قوي"
            st.session_state.page = 3
            st.rerun()

# -------------------------------------------------------------
# الواجهة 3: سؤال الاسم والقصف
# -------------------------------------------------------------
elif st.session_state.page == 3:
    st.title("👤 السؤال الأول: الهوية")
    name_input = st.text_input("اكتب اسمك الحقيقي هنا بدون كذب:")
    
    if name_input:
        if st.session_state.roast_msg == "":
            st.session_state.roast_msg = random.choice(roasts_database["name"][st.session_state.level])
        
        st.markdown(f'<div class="roast-box">💥 قصف جبهة {name_input}:<br>{st.session_state.roast_msg}</div>', unsafe_allow_html=True)
        
        if st.button("➡️ الانتقال للسؤال التالي"):
            st.session_state.roast_msg = ""  # تفريغ القصف السابق تمهيداً للمرحلة التالية
            st.session_state.page = 4
            st.rerun()

# -------------------------------------------------------------
# الواجهة 4: سؤال العمر والقصف (تم إصلاح الخلل)
# -------------------------------------------------------------
elif st.session_state.page == 4:
    st.title("⏳ السؤال الثاني: خريف العمر")
    age_input = st.number_input("كم عمرك حالياً بالسنوات؟", min_value=1, max_value=100, value=15)
    
    if st.button("💥 أرسل العمر واستقبل القصف"):
        st.session_state.roast_msg = random.choice(roasts_database["age"][st.session_state.level])

    if st.session_state.roast_msg:
        st.markdown(f'<div class="roast-box">💥 قصف جبهة العمر ({age_input} سنة):<br>{st.session_state.roast_msg}</div>', unsafe_allow_html=True)
        
    # تم إخراج زر الانتقال خارج شرط عرض الرسالة ليعمل بشكل سليم دائماً
    if st.button("➡️ الانتقال للسؤال الأخير"):
        st.session_state.roast_msg = ""
        st.session_state.page = 5
        st.rerun()

# -------------------------------------------------------------
# الواجهة 5: سؤال السنة الدراسية والقصف الختامي (تم إصلاح الخلل)
# -------------------------------------------------------------
elif st.session_state.page == 5:
    st.title("📚 السؤال الثالث: الكارثة الدراسية")
    grade_input = st.selectbox("في أي سنة تدرس حالياً في الثانوية؟", ["الأولى ثانوي", "الثانية ثانوي آداب وفلسفة", "الثانية ثانوي علوم", "الثالثة ثانوي (بكالوريا ريبوت)"])
    
    if st.button("💀 اقصف جبهتي الختامية"):
        st.session_state.roast_msg = random.choice(roasts_database["grade"][st.session_state.level])

    if st.session_state.roast_msg:
        st.markdown(f'<div class="roast-box">💥 القصف النهائي لـ {grade_input}:<br>{st.session_state.roast_msg}</div>', unsafe_allow_html=True)
        
    # تم إخراج زر الإعادة خارج شرط عرض الرسالة لضمان استجابة التطبيق
    if st.button("🔄 إعادة التحدي من جديد"):
        st.session_state.page = 1
        st.session_state.level = ""
        st.session_state.roast_msg = ""
        st.rerun()

st.markdown("---")
st.caption("💥 تم التدمير والتطوير بكل قسوة بواسطة **AssoumiDev** 💥")
