import streamlit as st

st.set_page_config(
    page_title="Case File #027",
    page_icon="🔐",
    layout="wide"
)

PASSWORD = "110101001011"

paragraphs = ['The investigation began with a message that appeared meaningless at first, but every character seemed to have been placed deliberately.', 'Hours later, the recovered records pointed toward a hidden trail that was not stored in the usual evidence archive.', 'Every fragment of information seemed to reveal another fragment, suggesting that the creator expected someone to follow the trail carefully.', 'Keeping the clues in their original order became important because moving even one piece could change the meaning of the evidence.', 'Investigators noticed that the digital trail contained references to places, names, and timestamps that did not immediately identify anyone.', 'Late in the investigation, a previously overlooked record suggested that the answer might be hidden in plain sight.', 'Local system notes described unusual activity around the time the incident was reported, although they did not identify the person responsible.', 'Evidence collected from the investigation was incomplete, yet the pattern across the records was becoming clearer.', 'Records from several sources appeared unrelated until they were examined together as parts of the same story.', 'In one archive, a short note mentioned that beginnings sometimes reveal more than endings.', 'Several entries repeated the same idea: do not focus only on the information in the middle.', 'Just before the final record was opened, the investigators realized that the arrangement of the evidence itself could carry a message.', 'A careful reading of the collected notes revealed a pattern that had been invisible during the first examination.', 'Security logs confirmed that someone had accessed the system, but the logs alone were not enough to identify the intruder.', 'One remaining question was whether the final clue contained the name directly or concealed it through another simple pattern.', 'No additional files were found, so the investigators returned to the text they had already collected.', 'The first words of the records suddenly seemed more important than the sentences that followed them.', 'Another review showed that the beginning of each paragraph followed a deliberate sequence rather than random wording.', 'Yet the meaning was still incomplete until the initial letters were written down in their original order.', 'Later, the investigators arranged those letters without changing their position and finally saw a recognizable statement.', 'Only then did the hidden identity become clear enough to report as the final conclusion.', 'Remember that in an investigation, the smallest structural detail can sometimes reveal what the obvious evidence does not.']

st.title("🔐 CASE FILE #027")
st.subheader("Murder Investigation — Restricted Access")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.write(
        "Sistem mengunci evidence terakhir."
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

    for paragraph in paragraphs:
        st.write(paragraph)

    st.divider()

    answer = st.text_input(
        "Siapa pelakunya?",
        placeholder="Masukkan nama tersangka..."
    )

    if st.button("SUBMIT FINAL ANSWER"):
        normalized = "".join(answer.lower().split())
        if normalized == "jasontaylor":
            st.balloons()
            st.success("CASE SOLVED — Jason Taylor adalah pelakunya.")
        else:
            st.warning("Jawaban belum tepat. Periksa kembali pola pada evidence.")
