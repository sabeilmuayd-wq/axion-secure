import streamlit as st
import secrets
import string
import pandas as pd
from datetime import datetime
import os

# إعدادات الصفحة
st.set_page_config(page_title="Axion Secure", page_icon="🛡️", layout="centered")

# دالة لتوليد الأكواد
def generate_key(length=8):
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))

# دالة لحفظ البيانات في ملف CSV على الهاتف
def save_to_db(data):
    file_path = 'deals_db.csv'
    df = pd.DataFrame([data])
    if not os.path.isfile(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode='a', header=False, index=False)

# الواجهة
st.title("🛡️ Axion Secure v1.6")
st.write("نظام الضمان الرقمي - سجلاتك محفوظة ومؤمنة")

tab1, tab2, tab3 = st.tabs(["🚀 صفقة جديدة", "🔍 تحقق", "📊 السجلات"])

with tab1:
    merchant = st.text_input("اسم التاجر")
    amount = st.number_input("المبلغ (USD)", min_value=0)
    
    if st.button("تفعيل القفل وحفظ البيانات"):
        b_key = generate_key() # كود المشتري
        v_key = generate_key() # كود الوسيط (أنت)
        deal_id = f"AXN-{datetime.now().strftime('%M%S')}"
        
        # حفظ في القاعدة
        new_data = {
            "ID": deal_id,
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Merchant": merchant,
            "Amount": amount,
            "Buyer_Key": b_key,
            "Your_Key": v_key,
            "Status": "Locked"
        }
        save_to_db(new_data)
        
        st.success(f"تم الحفظ! رقم العملية: {deal_id}")
        st.error(f"🔴 كود المشتري (للسودان): {b_key}")
        st.warning(f"🟢 كود الوسيط (لك): {v_key}")

with tab3:
    st.write("### سجل العمليات السابقة")
    if os.path.isfile('deals_db.csv'):
        df_display = pd.read_csv('deals_db.csv')
        st.dataframe(df_display[['ID', 'Date', 'Merchant', 'Amount', 'Status']])
    else:
        st.info("لا توجد عمليات مسجلة بعد.")
