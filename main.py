import streamlit as st
import pandas as pd
from datetime import datetime

# --- إعدادات النظام ---
st.set_page_config(page_title="Axion Omni-System 2026", page_icon="🛡️", layout="wide")

# --- قائمة التنقل ---
st.sidebar.title("🛡️ Axion Omni-System")
st.sidebar.markdown("---")
choice = st.sidebar.radio("اختر النظام الفرعي:", [
    "⚖️ ميزان المقاصة والقيم (للتجار)", 
    "🎓 أكاديمية أكسيون (للأطفال)", 
    "📅 جدولة المساعدات (للاجئين)"
])

# ---------------------------------------------------------
# 1. نظام المقاصة وحماية القيم (التجار)
# ---------------------------------------------------------
if choice == "⚖️ ميزان المقاصة والقيم (للتجار)":
    st.header("⚖️ نظام تصفية الديون وحماية القيمة")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📝 تسجيل دين جديد")
        debtor = st.text_input("اسم المدين (حامد مثلاً)")
        amount = st.number_input("المبلغ الحالي", min_value=1000)
        currency = st.selectbox("العملة", ["شلن أوغندي", "جنيه سوداني"])
        pegged = st.checkbox("تفعيل حماية القيمة (ربط بالذهب/الدولار)")
        if st.button("تسجيل وحماية"):
            st.success(f"تم تسجيل الدين على {debtor}. القيمة محمية ضد التضخم.")

    with col2:
        st.subheader("🔄 محرك البحث عن دوائر مغلقة")
        st.info("السيستم يبحث عن سلاسل (أ يطلب ب، ب يطلب ج، ج يطلب أ) لشطب الدين.")
        if st.button("بدء المقاصة التلقائية"):
            # محاكاة لإيجاد دائرة
            st.warning("وجدنا دائرة مغلقة: حامد يطلب (عثمان) وعثمان يطلبك أنت!")
            if st.button("تأكيد شطب الدين المتبادل"):
                st.balloons()
                st.success("تمت التصفية بنجاح! تم توفير الكاش للجميع.")

# ---------------------------------------------------------
# 2. أكاديمية أكسيون (مستقبل الأطفال)
# ---------------------------------------------------------
elif choice == "🎓 أكاديمية أكسيون (للأطفال)":
    st.header("🎓 سجل الكفاءة التعليمية الرقمي")
    st.write("حماية مستقبل الأطفال الدراسي عند الهجرة لبلد ثالث.")
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        child_name = st.text_input("اسم الطفل")
        grade = st.selectbox("الصف المستحق", ["الصف الرابع", "الصف السادس", "ثانوي"])
        skill = st.multiselect("المهارات المثبتة", ["الرياضيات", "اللغة الإنجليزية", "البرمجة"])
    
    with col_b:
        st.subheader("📸 محفظة الأدلة (Evidence)")
        st.file_uploader("ارفع صوراً للدفاتر أو التمارين كدليل للمنظمة")
        
    if st.button("إصدار جواز السفر الأكاديمي"):
        st.markdown(f"""
        <div style="border:3px solid #0089D1; padding:15px; border-radius:10px;">
            <h3 style="text-align:center;">Passport of Academic Competency</h3>
            <p><b>Student:</b> {child_name}</p>
            <p><b>Level:</b> {grade}</p>
            <p><b>Status:</b> Verified by Axion Field Experts</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. جدولة المساعدات (اللاجئين)
# ---------------------------------------------------------
else:
    st.header("📅 نظام المواعيد والكرامة")
    st.info("هذا الجزء يبهر المنظمات بقدرتك على تنظيم الحشود.")
    
    user_id = st.text_input("أدخل رقم ملف اللجوء الخاص بك")
    if user_id:
        st.write(f"مرحباً بك، صاحب الملف {user_id}")
        st.metric(label="موعدك القادم لاستلام المساعدة", value="20 مارس - 10:00 صباحاً")
        st.write("📍 المكان: مركز كمبالا الرئيسي")
        st.progress(80) # شريط تقدم يوضح اكتمال ملفك للهجرة
        st.write("اكتمال ملف الهجرة بناءً على كفاءتك التقنية: 80%")

# --- التذييل ---
st.sidebar.markdown("---")
st.sidebar.write("Developed by Axion Team")
st.sidebar.caption("إصدار 2026 - مخصص لحالات الطوارئ واللجوء")
