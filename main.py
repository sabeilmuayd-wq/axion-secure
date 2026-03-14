import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- إعدادات النظام ---
st.set_page_config(page_title="Axion Nexus v3.0", page_icon="🛡️", layout="wide")

# --- نظام الحماية ---
if "password_correct" not in st.session_state:
    st.markdown("<h1 style='text-align: center;'>Axion Nexus 🛡️</h1>", unsafe_allow_html=True)
    pwd = st.text_input("أدخل مفتاح الدخول الآمن", type="password")
    if st.button("فتح النظام"):
        if pwd == "1234":
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("❌ المفتاح غير صحيح")
    st.stop()

# --- واجهة النظام ---
st.sidebar.title("💎 Axion Control")
menu = ["🌐 بوابة التأمين (Escrow)", "⚖️ مقاصة الديون", "📦 توثيق الأصول"]
choice = st.sidebar.radio("اختر المهمة:", menu)

# --- 1. بوابة التأمين (مع إضافة بيانات السائق) ---
if choice == "🌐 بوابة التأمين (Escrow)":
    st.header("🌐 نظام تأمين الصفقات")
    
    col1, col2 = st.columns(2)
    with col1:
        buyer = st.text_input("اسم المشتري")
        seller = st.text_input("اسم البائع")
        item = st.selectbox("نوع السلعة", ["صندل", "بخور", "تحويل مالي", "بضاعة عامة"])
    
    with col2:
        driver_name = st.text_input("🚚 اسم السائق المسئول")
        truck_no = st.text_input("🆔 رقم الشاحنة / العربة")
        amount_usd = st.number_input("القيمة المثبتة (USD)", min_value=0)

    if st.button("توليد عقد الأمان وتوثيق السائق"):
        if buyer and driver_name:
            secure_code = f"AX-{random.randint(1000, 9999)}"
            st.success("✅ تم حجز الصفقة وتوثيق بيانات السائق")
            
            st.markdown(f"""
            <div style="background-color:#F0F9FF; padding:20px; border-radius:10px; border: 2px solid #0284C7;">
                <h2 style="text-align:center; color:#0369A1;">كود التأمين: {secure_code}</h2>
                <p style="text-align:right;"><b>السائق:</b> {driver_name}</p>
                <p style="text-align:right;"><b>رقم العربة:</b> {truck_no}</p>
                <hr>
                <p style="text-align:center;"><b>المشتري:</b> {buyer} | <b>المبلع:</b> ${amount_usd}</p>
            </div>
            """, unsafe_allow_html=True)
            st.info("💡 ملاحظة: لا تعطِ الكود للسائق، الكود يُسلم للمشتري فقط عند الوصول.")

# (باقي الأقسام تظل كما هي في النسخة السابقة)
