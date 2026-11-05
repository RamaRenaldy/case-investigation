import streamlit as st

st.set_page_config(
    page_title="Case File #027",
    page_icon="🔐",
    layout="wide"
)

PASSWORD = "110101001011"

st.title("🔐 CASE FILE #027")
st.subheader("Murder Investigation — Restricted Access")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.write(
        "Sistem mengunci evidence terakhir. "
        "Masukkan authentication key yang diperoleh dari perhitungan CBC."
    )

    entered = st.text_input(
        "Authentication Key",
        type="password",
        placeholder="Masukkan password hexadecimal..."
    )

    if st.button("ACCESS EVIDENCE"):
        if entered.strip().upper() == PASSWORD:
            st.session_state.authenticated = True
            st.success("ACCESS GRANTED")
            st.rerun()
        else:
            st.error("ACCESS DENIED — Periksa kembali perhitungan CBC.")

else:
    st.success("ACCESS GRANTED")
    st.markdown("### 🗂️ FINAL EVIDENCE")
    st.info(
        "Truth is not always hidden inside the words. "
        "Sometimes it is hidden at the beginning of every story."
    )

    # -------------------------------------------------------------
    # MENAMPILKAN GAMBAR CLUE
    # Ganti "clue.png" dengan path/nama file gambar Anda
    # -------------------------------------------------------------
    st.image("puisi.png", caption="Evidence Clue #027", use_container_width=True)

    st.divider()

    answer = st.text_input(
        "Siapa pelakunya?",
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
