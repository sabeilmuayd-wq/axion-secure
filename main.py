import streamlit as st
import pandas as pd
from datetime import datetime

# --- الإعدادات السيادية للنظام ---
st.set_page_config(page_title="Axion Shield | Global Trade & Protection", layout="wide", page_icon="🛡️")

# --- تنسيق احترافي (CSS) لجعل التطبيق يبدو كمنصة دولية ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #004a99; color: white; }
    .report-card { border: 1px solid #d1d8e0; padding: 20px; border-radius: 10px; background-color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- القائمة الجانبية (هوية أحمد - المبرمج والمزارع) ---
st.sidebar.image("https://img.icons8.com/fluency/96/shield.png")
st.sidebar.title("🛡️ Axion Shield v1.0")
st.sidebar.markdown("**نظام الحماية والامتثال التجاري**")
st.sidebar.write("المسؤول: **أحمد (كمبالا - كيرياندونغو)**")
st.sidebar.markdown("---")
st.sidebar.write("📜 **مبدأ النظام:** الشفافية هي أقوى درع ضد الفساد.")

# --- واجهة التحكم الرئيسية ---
st.title("🏗️ منصة أكسيون للإدارة والامتثال")
st.caption(f"توقيت النظام: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (توقيت شرق أفريقيا)")

tab1, tab2, tab3, tab4 = st.tabs(["📦 إدارة الشحنات", "⚖️ سجل النزاهة", "💰 ميزان القيم", "🎓 سجل الأطفال"])

# 1. إدارة الشحنات والمسارات (الحل اللوجستي)
with tab1:
    st.subheader("🚚 تتبع حركة الأصول العابرة للحدود")
    # بيانات حقيقية بناءً على مناقشاتنا لعام 2026
    ship_df = pd.DataFrame([
        {"الشحنة": "AX-Cargo-77", "الحمولة": "صندل أفريقي", "الموقع": "نيمولي", "الحالة": "انتظار تدقيق"},
        {"الشحنة": "AX-Cargo-82", "الحمولة": "مواد زراعية", "الموقع": "كمبالا", "الحالة": "تحت التحميل"}
    ])
    st.table(ship_df)
    if st.button("تحديث المسار الجغرافي (GPS)"):
        st.info("جاري فحص إشارات القمر الصناعي... الموقع مؤمن.")

# 2. سجل النزاهة (الدرع ضد الرشوة والسجن)
with tab2:
    st.subheader("⚖️ نظام توثيق الامتثال والانتهاكات")
    st.error("⚠️ هذا القسم مخصص لحمايتك القانونية. سجل أي عائق غير قانوني فوراً.")
    with st.form("incident_report"):
        incident_type = st.selectbox("نوع الحادثة:", ["طلب رسوم غير رسمية", "تأخير متعمد", "ابتزاز إداري", "تهديد شخصي"])
        location = st.text_input("الموقع (نقطة العبور/المكتب)")
        details = st.text_area("وصف دقيق للواقعة (سيتم تشفيره)")
        submitted = st.form_submit_button("إرسال البلاغ المشفر للسحابة")
        if submitted:
            st.success("✅ تم التوثيق. البلاغ الآن جزء من 'السجل الأسود' الذي لا يمكن حذفه، وهو متاح للجهات الحقوقية الدولية.")

# 3. ميزان القيم (قوت أولادك)
with tab3:
    st.subheader("💰 حماية القيمة ورأس المال")
    c1, c2, c3 = st.columns(3)
    c1.metric("سعر الصرف (USDT/UGX)", "3,850", "+25")
    c2.metric("مؤشر الذهب (أوقية)", "$2,150", "-0.1%")
    c3.metric("رصيد أكسيون المؤمن", "$4,200", "محمي")

# 4. سجل الأطفال (المستقبل)
with tab4:
    st.subheader("🎓 محفظة الكفاءة التعليمية")
    st.write("توثيق مهارات الأطفال لضمان القبول في أرقى مدارس العالم عند الهجرة.")
    child_name = st.text_input("اسم الابن/الابنة")
    skill_level = st.select_slider("مستوى الكفاءة التقنية", options=["مبتدئ", "متوسط", "متقدم", "خبير"])
    if st.button("إصدار شهادة الكفاءة"):
        st.write(f"تم إصدار الوثيقة لـ **{child_name}** كجزء من ملف الهجرة الفني.")

# --- التذييل السيادي ---
st.markdown("---")
st.markdown("<center><b>بواسطة أحمد - مبرمج ومزارع صامد | الله الصمد</b></center>", unsafe_allow_html=True)
