import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- إعدادات النظام الاحترافية ---
st.set_page_config(page_title="Axion Nexus v3.0", page_icon="🛡️", layout="wide")

# --- نظام الحماية ---
def check_password():
    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>Axion Nexus 🛡️</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>نظام تأمين التجارة وإدارة الأصول في ظروف الحرب</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            pwd = st.text_input("أدخل مفتاح الدخول الآمن", type="password")
            if st.button("فتح النظام"):
                if pwd == "1234": # غيره لباسوردك الخاص
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("❌ المفتاح غير صحيح")
        return False
    return True

if not check_password():
    st.stop()

# --- واجهة النظام الرئيسية ---
st.sidebar.title("💎 Axion Control")
st.sidebar.info(f"المستخدم: مدير المشروع\nالتاريخ: {datetime.now().strftime('%Y-%m-%d')}")

menu = ["🌐 بوابة التأمين (Escrow)", "⚖️ مقاصة الديون (Debt Offset)", "📦 توثيق الأصول والسلع", "📊 سجل الثقة (Reputation)"]
choice = st.sidebar.radio("اختر المهمة:", menu)

# --- 1. بوابة التأمين (حل مشكلة الثقة) ---
if choice == "🌐 بوابة التأمين (Escrow)":
    st.header("🌐 نظام تأمين الصفقات العابرة للحدود")
    col1, col2 = st.columns(2)
    
    with col1:
        buyer = st.text_input("اسم المشتري")
        seller = st.text_input("اسم البائع")
        item = st.selectbox("نوع السلعة", ["صندل", "بخور", "تحويل مالي", "مواد تموينية"])
    
    with col2:
        amount_usd = st.number_input("القيمة المثبتة (USD)", min_value=0)
        lock_rate = st.checkbox("تثبيت القيمة ضد تذبذب العملة", value=True)
    
    if st.button("توليد عقد الأمان الذكي"):
        if buyer and seller:
            secure_code = f"AX-{random.randint(1000, 9999)}-{random.randint(10, 99)}"
            st.success("✅ تم قفل الصفقة وتوليد كود التأمين")
            st.markdown(f"""
            <div style="background-color:#E0F2FE; padding:20px; border-radius:10px; border-left: 5px solid #0369A1;">
                <h2 style="color:#0369A1; text-align:center;">{secure_code}</h2>
                <p style="text-align:center; color:#1E3A8A;"><b>الضامن:</b> Axion Pay System</p>
                <p style="text-align:center;">القيمة: {amount_usd} USD (مثبتة)</p>
            </div>
            """, unsafe_allow_html=True)
            st.caption("لا يُسلم الكود إلا عند التأكد من وصول البضاعة للحدود.")

# --- 2. مقاصة الديون (حل مشكلة السيولة) ---
elif choice == "⚖️ مقاصة الديون (Debt Offset)":
    st.header("⚖️ نظام تسييل الديون المتقاطعة")
    st.write("حل مشكلة 'لا توجد سيولة' عبر تبادل الديون.")
    
    with st.expander("تسجيل دين جديد"):
        d1 = st.text_input("الطرف الأول (المدين)")
        d2 = st.text_input("الطرف الثاني (الدائن)")
        val = st.number_input("المبلغ المطلوب")
        if st.button("تسجيل في قاعدة المقاصة"):
            st.info("تم الحفظ. سيقوم النظام بالبحث عن 'دائرة ديون' لتصفيتها ورقياً.")

# --- 3. توثيق الأصول (حل مشكلة النهب والضياع) ---
elif choice == "📦 توثيق الأصول والسلع":
    st.header("📦 الخزنة الرقمية للأصول")
    st.write("توثيق قانوني للبضاعة قبل أو أثناء الشحن.")
    
    uploaded_file = st.file_uploader("ارفع صورة الفاتورة أو البضاعة أو بوليصة الشحن")
    location = st.text_input("موقع المخزن الحالي (مثلاً: كمبالا - كيسيني)")
    
    if st.button("ختم التوثيق الرقمي"):
        if uploaded_file:
            st.success(f"تم الختم! المعرف الرقمي للأصل: #IMG-{random.randint(10000,99999)}")
            st.write(f"الحالة: موثق بتاريخ {datetime.now()}")

# --- 4. سجل الثقة ---
elif choice == "📊 سجل الثقة (Reputation)":
    st.header("📊 القائمة البيضاء للتجار والوسطاء")
    data = {
        "الاسم": ["تاجر كمبالا أ", "سائق جوبا ب", "مورد بورتسودان"],
        "التقييم": ["⭐⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐"],
        "الحالة": ["موثق", "تحت المراجعة", "موثق"]
    }
    st.table(pd.DataFrame(data))

# --- تذييل ---
st.sidebar.write("---")
if st.sidebar.button("خروج آمن"):
    del st.session_state["password_correct"]
    st.rerun()
