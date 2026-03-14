import streamlit as st
import random
from datetime import datetime

# --- إعدادات الصفحة الاحترافية ---
st.set_page_config(page_title="Axion Nexus v3.0", layout="wide")

# --- 1. نظام الحماية (بوابة الدخول الآمنة) ---
if "password_correct" not in st.session_state:
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🛡️ Axion Nexus System</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>نظام تأمين التجارة وإدارة الأصول - إصدار الميدان</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        pwd = st.text_input("أدخل مفتاح الدخول الآمن", type="password")
        if st.button("فتح النظام"):
            if pwd == "1234": # كلمة المرور الخاصة بك
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ المفتاح غير صحيح")
    st.stop()

# --- 2. واجهة العمل الميداني ---
st.title("🛡️ لوحة التحكم الشاملة - Axion Nexus")
st.write(f"التاريخ: {datetime.now().strftime('%Y-%m-%d')} | الموقع: كمبالا")
st.write("---")

# --- القسم الأول: بوابة التأمين وحساب العمولة (Escrow) ---
st.header("🌐 1. تأمين الصفقات والرسوم (Escrow)")
col1, col2 = st.columns(2)

with col1:
    buyer = st.text_input("اسم المشتري", placeholder="أحمد بورتسودان")
    seller = st.text_input("اسم البائع", placeholder="شركة الصندل")
    item = st.selectbox("نوع السلعة", ["بخور صندل", "تحويل مالي", "مواد تموينية", "بضاعة عامة"])
    amount_usd = st.number_input("قيمة الصفقة (USD)", min_value=0.0)

with col2:
    driver_name = st.text_input("🚚 اسم السائق المسئول")
    truck_no = st.text_input("🆔 رقم الشاحنة / العربة")
    # إعداد نسبة العمولة (مثلاً 1% - يمكنك تغييرها هنا)
    fee_percentage = 0.01 
    service_fee = amount_usd * fee_percentage
    total_amount = amount_usd + service_fee
    
    st.markdown(f"""
    <div style="background-color:#FFFBEB; padding:15px; border-radius:10px; border: 1px solid #F59E0B;">
        <p style="margin:0; color:#B45309;">📊 <b>تفاصيل الرسوم التقنية:</b></p>
        <p style="margin:0;">رسوم تأمين النظام (1%): <b>${service_fee:,.2f}</b></p>
        <p style="margin:0; font-size:1.2em;">الإجمالي المطلوب: <b>${total_amount:,.2f}</b></p>
    </div>
    """, unsafe_allow_html=True)

if st.button("توليد عقد الأمان وتفعيل الرسوم"):
    if buyer and driver_name and amount_usd > 0:
        secure_code = f"AX-{random.randint(1000, 9999)}"
        st.success(f"✅ تم حجز الصفقة وتفعيل رسوم الخدمة (${service_fee})")
        st.markdown(f"""
        <div style="background-color:#F0F9FF; padding:20px; border-radius:10px; border: 2px solid #0284C7; text-align:center;">
            <h2 style="color:#0369A1;">كود التأمين: {secure_code}</h2>
            <p style="color:#1E3A8A;"><b>السائق:</b> {driver_name} | <b>رقم العربة:</b> {truck_no}</p>
            <p style="color:#1E3A8A;"><b>المشتري:</b> {buyer} | <b>المبلغ الصافي:</b> ${amount_usd}</p>
            <p style="color:#B45309;"><b>رسوم النظام المستحقة: ${service_fee:,.2f}</b></p>
            <hr>
            <small>⚠️ ملاحظة: الكود هو الضمان الوحيد لاستلام المال، لا يُسلم إلا عند الوصول.</small>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ يرجى إدخال كافة البيانات (المشتري، السائق، والمبلغ).")

st.write("---")

# --- القسم الثاني: مقاصة الديون ---
st.header("⚖️ 2. مقاصة وتصفية الديون (Liquidity)")
col3, col4 = st.columns(2)
with col3:
    debtor = st.text_input("المدين (من عليه المال)")
with col4:
    creditor = st.text_input("الدائن (صاحب المال)")
debt_val = st.number_input("مبلغ الدين للتسوية", min_value=0.0)

if st.button("تسجيل طلب المقاصة"):
    st.info(f"تم تسجيل طلب تصفية الدين بين {debtor} و {creditor}. جاري البحث عن دائرة مغلقة.")

st.write("---")

# --- القسم الثالث: توثيق الأصول ---
st.header("📦 3. توثيق الأصول والسلع (Asset Vault)")
uploaded_file = st.file_uploader("ارفع صورة البضاعة أو الفاتورة للتوثيق الرقمي")
if st.button("ختم التوثيق"):
    if uploaded_file:
        asset_id = f"REF-{random.randint(10000, 99999)}"
        st.success(f"✅ موثق! معرف الأصل: {asset_id}")
    else:
        st.error("يرجى رفع ملف.")

st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>Axion Nexus v3.0 | تأمين - توثيق - مقاصة</p>", unsafe_allow_html=True)
