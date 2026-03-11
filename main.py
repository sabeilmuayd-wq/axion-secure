import streamlit as st
import secrets
import string
import pandas as pd
from datetime import datetime
import os

# إعدادات الصفحة
st.set_page_config(page_title="Axion Secure", page_icon="🛡️")

DB_FILE = 'deals_db.csv'

# دالة توليد الأكواد
def generate_key():
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(8))

# دالة الحفظ
def save_deal(deal):
    df = pd.DataFrame([deal])
    if not os.path.isfile(DB_FILE):
        df.to_csv(DB_FILE, index=False)
    else:
        df.to_csv(DB_FILE, mode='a', header=False, index=False)

# الواجهة الرئيسية
st.title("🛡️ Axion Secure v1.7")

tab1, tab2, tab3 = st.tabs(["🚀 إنشاء صفقة", "🔍 التحقق والتحرير", "📊 السجلات"])

with tab1:
    merchant = st.text_input("اسم التاجر")
    amount = st.number_input("المبلغ (USD)", min_value=0)
    if st.button("تفعيل وحفظ"):
        b_key, v_key = generate_key(), generate_key()
        deal = {
            "ID": f"AXN-{datetime.now().strftime('%M%S')}",
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Merchant": merchant,
            "Amount": amount,
            "Buyer_Key": b_key,
            "Your_Key": v_key,
            "Status": "Locked"
        }
        save_deal(deal)
        st.success(f"تم الحفظ! رقم العملية: {deal['ID']}")
        st.error(f"كود المشتري (للسودان): {b_key}")
        st.warning(f"كود الوسيط (لك): {v_key}")

with tab2:
    st.subheader("تحرير المبلغ")
    input_b = st.text_input("أدخل كود المشتري")
    input_v = st.text_input("أدخل كود الوسيط")
    
    if st.button("تحقق وتحرير"):
        if os.path.isfile(DB_FILE):
            df = pd.read_csv(DB_FILE)
            # البحث عن صفقة تطابق الكودين معاً
            match = df[(df['Buyer_Key'] == input_b) & (df['Your_Key'] == input_v)]
            
            if not match.empty:
                st.balloons()
                st.success("✅ تطابق مذهل! الصفقة صحيحة ومؤمنة.")
                st.info(f"التاجر المستحق: {match.iloc[0]['Merchant']} | المبلغ: {match.iloc[0]['Amount']}$")
            else:
                st.error("❌ فشل التحقق! الأكواد غير صحيحة أو غير متطابقة.")
        else:
            st.warning("لا توجد قاعدة بيانات حالياً.")

with tab3:
    if os.path.isfile(DB_FILE):
        st.dataframe(pd.read_csv(DB_FILE)[['ID', 'Date', 'Merchant', 'Amount', 'Status']])
    else:
        st.info("السجل فارغ.")
