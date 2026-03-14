import streamlit as st
import pandas as pd
from datetime import datetime

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Axion Secure v2.0", page_icon="🔐", layout="centered")

# --- نظام الحماية (v1.4 Secure) ---
def check_password():
    """التحقق من كلمة المرور لتأمين النظام"""
    if "password_correct" not in st.session_state:
        st.markdown("<h2 style='text-align: center;'>Axion Pay System</h2>", unsafe_allow_html=True)
        password = st.text_input("أدخل كلمة المرور الخاصة بك", type="password")
        if st.button("فتح النظام"):
            if password == "1234": # يمكنك تغيير الرقم السري هنا
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ كلمة المرور غير صحيحة")
        return False
    return True

# إذا لم يتم إدخال الباسورد، توقف هنا
if not check_password():
    st.stop()

# --- واجهة التطبيق الرئيسية (بعد الدخول) ---
st.title("🛡️ Axion Secure v2.0")
st.write(f"مرحباً بك يا قائد. التاريخ الحالي: {datetime.now().strftime('%Y-%m-%d')}")

# قائمة جانبية للتنقل
menu = ["لوحة التحكم", "تسجيل صفقة جديدة", "سجل المعاملات", "حول المشروع"]
choice = st.sidebar.selectbox("القائمة", menu)

if choice == "لوحة التحكم":
    st.subheader("📊 ملخص النشاط")
    col1, col2 = st.columns(2)
    col1.metric("إجمالي الصفقات", "0")
    col2.metric("الرصيد المتاح", "$100")
    
    st.info("جاهز لاستقبال معاملات تجار كمبالا غداً.")

elif choice == "تسجيل صفقة جديدة":
    st.subheader("📝 تسجيل معاملة مالية")
    with st.form("trade_form"):
        trader_name = st.text_input("اسم التاجر")
        item = st.selectbox("نوع السلعة", ["بخور صندل", "تحويل مالي", "وساطة تجارية"])
        amount = st.number_input("المبلغ (بالدولار أو الشلن)", min_value=0)
        notes = st.text_area("ملاحظات إضافية")
        
        submitted = st.form_submit_state = st.form_submit_button("حفظ الصفقة")
        if submitted:
            st.success(f"تم تسجيل صفقة {item} للتاجر {trader_name} بنجاح.")

elif choice == "سجل المعاملات":
    st.subheader("📋 تاريخ العمليات")
    st.warning("لا توجد معاملات مسجلة بعد. ابدأ أول صفقة غداً.")

elif choice == "حول المشروع":
    st.write("---")
    st.write("**مشروع Axion Pay:** نظام مالي مؤمن للوساطة التجارية بين أوغندا والسودان.")
    st.write("**المطور:** مشروع مبرمج عصامي (قيد التمكين).")

# --- تذييل الصفحة ---
st.sidebar.write("---")
if st.sidebar.button("تسجيل الخروج"):
    del st.session_state["password_correct"]
    st.rerun()
