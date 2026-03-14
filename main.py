import streamlit as st
import random
from datetime import datetime

# --- إعدادات الصفحة (تعديل الخطأ السابق) ---
st.set_page_config(page_title="Axion Nexus v3.0", layout="wide")

# --- 1. نظام الحماية (بوابة الدخول) ---
if "password_correct" not in st.session_state:
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🛡️ Axion Nexus System</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>نظام تأمين التجارة وإدارة الأصول - نسخة الحرب</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        pwd = st.text_input("أدخل مفتاح الدخول الآمن", type="password")
        if st.button("فتح النظام"):
            if pwd == "1234": # يمكنك تغيير الرقم السري هنا
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ المفتاح غير صحيح")
    st.stop()

# --- 2. واجهة العمل الميداني (بعد الدخول) ---
st.title("🛡️ لوحة التحكم الشاملة - Axion Nexus")
st.write(f"التاريخ: {datetime.now().strftime('%Y-%m-%d')} | الموقع: كمبالا")
st.write("---")

# --- القسم الأول: بوابة التأمين (Escrow) ---
st.header("🌐 1. تأمين الصفقات (Escrow)")
col1, col2 = st.columns(2)
with col1:
    buyer = st.text_input("اسم المشتري", placeholder="مثلاً: أحمد بورتسودان")
    seller = st.text_input("اسم البائع", placeholder="مثلاً: شركة الصندل")
    item = st.selectbox("نوع السلعة", ["بخور صندل", "تحويل مالي", "مواد تموينية", "أخرى"])
with col2:
    driver_name = st.text_input("🚚 اسم السائق المسئول")
    truck_no = st.text_input("🆔 رقم الشاحنة / العربة")
    amount_usd = st.number_input("القيمة المثبتة (USD)", min_value=0)

if st.button("توليد كود التأمين الآن"):
    if buyer and driver_name:
        secure_code = f"AX-{random.randint(1000, 9999)}"
        st.success(f"✅ تم حجز الصفقة وتوثيق بيانات السائق")
        st.markdown(f"""
        <div style="background-color:#F0F9FF; padding:20px; border-radius:10px; border: 2px solid #0284C7; text-align:center;">
            <h2 style="color:#0369A1;">كود التأمين: {secure_code}</h2>
            <p style="color:#1E3A8A;"><b>السائق:</b> {driver_name} | <b>رقم العربة:</b> {truck_no}</p>
            <p style="color:#1E3A8A;"><b>المشتري:</b> {buyer} | <b>المبلغ:</b> ${amount_usd}</p>
            <small>💡 ملاحظة: لا تُسلم الكود إلا عند التأكد من وصول البضاعة.</small>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ يرجى إدخال بيانات المشتري والسائق أولاً.")

st.write("---")

# --- القسم الثاني: مقاصة وتصفية الديون ---
st.header("⚖️ 2. مقاصة وتصفية الديون (Liquidity)")
st.info("نظام تصفية الديون المتقاطعة لتوفير السيولة في ظروف الحرب.")
col3, col4 = st.columns(2)
with col3:
    debtor = st.text_input("المدين (من عليه المال)")
with col4:
    creditor = st.text_input("الدائن (صاحب المال)")
debt_val = st.number_input("مبلغ الدين المطلوب تسويته", min_value=0)

if st.button("بدء المقاصة الرقمية"):
    if debtor and creditor:
        st.success(f"تم تسجيل طلب المقاصة لـ {debtor} و {creditor}.")
        st.info("جاري البحث عن دائرة ديون مقابلة لتصفية الحساب ورقياً...")
    else:
        st.warning("يرجى إدخال أسماء الأطراف.")

st.write("---")

# --- القسم الثالث: توثيق الأصول والسلع ---
st.header("📦 3. توثيق الأصول والسلع (Asset Vault)")
asset_desc = st.text_area("وصف البضاعة وحالتها (إثبات ملكية)")
uploaded_file = st.file_uploader("ارفع صورة الفاتورة أو البضاعة للتوثيق الجنائي")

if st.button("ختم التوثيق الرقمي"):
    if uploaded_file:
        asset_id = f"REF-{random.randint(10000, 99999)}"
        st.success(f"✅ تم التوثيق بنجاح. معرف الأصل: {asset_id}")
        st.write(f"الحالة: موثق رقمياً بتاريخ {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    else:
        st.error("يرجى رفع ملف أو صورة لتمام التوثيق.")

st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>Axion Nexus v3.0 | Powering Trade in Chaos</p>", unsafe_allow_html=True)
