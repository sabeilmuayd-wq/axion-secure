import streamlit as st
import random
from datetime import datetime

# --- إعدادات الصفحة ---
st.set_config(page_title="Axion Nexus v3.0", layout="wide")

# --- 1. نظام الحماية (البوابة) ---
if "password_correct" not in st.session_state:
    st.markdown("<h1 style='text-align: center;'>🛡️ Axion Nexus System</h1>", unsafe_allow_html=True)
    pwd = st.text_input("أدخل مفتاح الدخول الآمن", type="password")
    if st.button("فتح النظام"):
        if pwd == "1234":
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("❌ المفتاح غير صحيح")
    st.stop()

# --- 2. واجهة العمل الميداني (تظهر بالترتيب) ---
st.title("🛡️ لوحة التحكم الشاملة - Axion")
st.write(f"تاريخ اليوم: {datetime.now().strftime('%Y-%m-%d')}")
st.write("---")

# --- القسم الأول: بوابة التأمين (Escrow) ---
st.header("🌐 1. تأمين الصفقات (Escrow)")
col1, col2 = st.columns(2)
with col1:
    buyer = st.text_input("اسم المشتري")
    seller = st.text_input("اسم البائع")
    item = st.selectbox("نوع السلعة", ["صندل", "بخور", "تحويل مالي", "بضاعة عامة"])
with col2:
    driver_name = st.text_input("🚚 اسم السائق المسئول")
    truck_no = st.text_input("🆔 رقم الشاحنة / العربة")
    amount_usd = st.number_input("القيمة المثبتة (USD)", min_value=0)

if st.button("توليد كود التأمين الآن"):
    if buyer and driver_name:
        code = f"AX-{random.randint(1000, 9999)}"
        st.success(f"✅ تم الحجز! كود التأمين هو: {code}")
        st.info(f"البيانات الموثقة: المشتري ({buyer}) | السائق ({driver_name})")
    else:
        st.warning("يرجى ملء بيانات المشتري والسائق.")

st.write("---")

# --- القسم الثاني: مقاصة الديون (Debt Offset) ---
st.header("⚖️ 2. مقاصة وتصفية الديون")
col3, col4 = st.columns(2)
with col3:
    debtor = st.text_input("اسم المدين (عليه دين)")
with col4:
    creditor = st.text_input("اسم الدائن (يطلب مال)")
debt_val = st.number_input("مبلغ الدين للتصفية", min_value=0)

if st.button("إجراء مقاصة رقمية"):
    st.info("جاري البحث في السجلات عن ديون متقابلة لتصفيتها...")
    st.success(f"تم تسجيل طلب المقاصة لـ {debtor} و {creditor}. سيتم الإخطار عند اكتمال الدائرة.")

st.write("---")

# --- القسم الثالث: توثيق الأصول (Asset Vault) ---
st.header("📦 3. توثيق الأصول والسلع")
asset_desc = st.text_area("وصف البضاعة (مثلاً: 50 كيلو صندل نخب أول)")
uploaded_file = st.file_uploader("ارفع صورة الفاتورة أو البضاعة للتوثيق")

if st.button("ختم التوثيق الرقمي"):
    if uploaded_file:
        asset_id = f"ASSET-{random.randint(100, 999)}"
        st.success(f"✅ تم التوثيق! معرف الأصل: {asset_id}")
        st.write(f"الحالة: موثق رقمياً بتاريخ {datetime.now()}")
    else:
        st.error("يرجى رفع صورة للتوثيق.")

st.write("---")
st.caption("Axion Nexus v3.0 - جميع الحقوق محفوظة للقائد")
