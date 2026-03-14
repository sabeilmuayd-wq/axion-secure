import streamlit as st
import random
import time

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Axion Secure v2.0", page_icon="🔐")

# --- نظام الحماية ---
def check_password():
    if "password_correct" not in st.session_state:
        st.markdown("<h2 style='text-align: center;'>نظام Axion Pay المؤمن</h2>", unsafe_allow_html=True)
        pwd = st.text_input("أدخل كلمة المرور للدخول إلى لوحة التحكم", type="password")
        if st.button("دخول"):
            if pwd == "1234": # الباسورد الخاص بك
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ كلمة المرور خاطئة")
        return False
    return True

if not check_password():
    st.stop()

# --- المهمة الأساسية (توليد كود المشتري) ---
st.title("🛡️ بوابة Axion Secure للوساطة")
st.write("---")

st.subheader("📦 إنشاء معاملة جديدة (توليد كود)")

# مدخلات العملية
buyer_name = st.text_input("اسم المشتري / التاجر")
amount = st.number_input("مبلغ المعاملة ($)", min_value=0)

if st.button("توليد كود التأمين الآن"):
    if buyer_name:
        with st.spinner('جاري تشفير البيانات وتوليد الكود...'):
            time.sleep(1.5)
            # توليد كود عشوائي فريد
            secure_code = f"AX-{random.randint(1000, 9999)}-{random.randint(10, 99)}"
            
            st.success("✅ تم توليد الكود بنجاح!")
            st.markdown(f"""
            <div style="background-color:#f0f2f6;padding:20px;border-radius:10px;border:2px solid #0e1117;text-align:center;">
                <h3 style="color:#0e1117;">كود المشتري الخاص بـ {buyer_name}</h3>
                <h1 style="color:#ff4b4b;letter-spacing: 5px;">{secure_code}</h1>
                <p>مبلغ العملية: <b>{amount} دولار</b></p>
                <small>يرجى تزويد المشتري بهذا الكود لإتمام العملية</small>
            </div>
            """, unsafe_allow_html=True)
            
            # زر لمشاركة الكود (محاكاة)
            st.info("قم بتصوير الشاشة وإرسالها للتاجر لضمان حقه.")
    else:
        st.warning("يرجى إدخال اسم المشتري أولاً.")

st.write("---")
st.caption("Axion Pay v2.0 - نظام حماية الوسيط والتاجر")
