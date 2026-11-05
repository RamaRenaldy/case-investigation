import streamlit as st

st.set_page_config(
    page_title="Case File #027",
    page_icon="🔐",
    layout="wide"
)

PASSWORD = "110101001011"

st.title("HAHAHAHA 🤡👅")
st.subheader("Not Everyone Can Come In")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.write(
        "Sistem mengunci petunjuk terakhir. "
        "Masukkan jawaban Anda."
    )

    entered = st.text_input(
        "Authentication Key",
        type="password",
        placeholder="Masukkan Jawaban Anda..."
    )

    if st.button("ACCESS EVIDENCE"):
        if entered.strip().upper() == PASSWORD:
            st.session_state.authenticated = True
            st.success("SELAMAT ANDA BERHASIL MASUK HAHAHAHA")
            st.rerun()
        else:
            st.error("ACCESS DENIED.")

else:
    st.success("ACCESS GRANTED")
    st.markdown("### 🗂️ FINAL ROUND")
    st.info(
        "Selamat, Detektif. Kau berhasil bertahan hingga babak final. Sangat sedikit orang di kota ini yang memiliki ketajaman akal untuk melangkah sejauh ini, melampaui kepanikan masal dan analisis dangkal para aparat Gotham."
        "Di hadapanmu sekarang tergelar teka-teki terakhir—sebuah mahakarya simetri yang kurancang khusus untuk menguji batas kecerdasanmu. Setiap baris puisi yang kau baca bukanlah sekadar ratapan atau ancaman kosong, melainkan deretan petunjuk transparan yang sengaja kutelanjangi di hadapan matamu. Rahasia terbesar tidak pernah tersembunyi di kedalaman malam, melainkan terpampang jelas di garis paling awal."
        "Sekarang, tunjukkan padaku... siapa aku sebenarnya?"
    )
    st.info("Truth is not always hidden inside the words.")

    st.image("puisi.png", caption="Look First", use_container_width=True)

    st.divider()

    
    st.subheader("Siapa Pelakunya??")
    answer = st.text_input(
        "Siapa Pelakunya?",
        placeholder="Masukkan nama tersangka..."
    )

    if st.button("SUBMIT FINAL ANSWER"):
        normalized = "".join(answer.lower().split())
        # Ubah jawaban di bawah jika pelakunya adalah Edward Nygma (edwardnygma)
        if normalized == "edwardnygma":
            st.balloons()
            st.success("CASE SOLVED — Edward Nygma adalah pelakunya.")
        else:
            st.warning("Jawaban belum tepat. Periksa kembali pola pada evidence.")
