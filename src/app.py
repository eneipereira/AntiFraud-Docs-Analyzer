import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analize_credit_card

def configure_interface():
  st.title("Upload de Arquivo DIO - Desafio 1 - Azure - Fake Docs")
  uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

  if uploaded_file is not None:
    filename = uploaded_file.name
    blob_url = upload_blob(uploaded_file, filename)

    if blob_url:
      st.write(f"Arquivo {filename} enviado com sucesso para o Azure Blob Storage!")
      credit_card_info = analize_credit_card(blob_url)
      show_image_and_validation(blob_url, credit_card_info)
    else:
      st.write(f"Erro ao enviar o arquivo {filename} para o Azure Blob Storage")

def show_image_and_validation(blob_url, credit_card_info):
  st.image(blob_url, caption="Imagem enviada", use_container_width=True)
  st.write("Resultado da validação:")
  if credit_card_info and credit_card_info["card_name"]:
    st.markdown(f"<h1 style='color: green;'>Cartão de Crédito Válido</h1>", unsafe_allow_html=True)
    st.write(f"Nome do Cartão: {credit_card_info['card_name']}")
    st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
    st.write(f"Data de Expiração: {credit_card_info['expiration_date']}")
  else:
    st.markdown(f"<h1 style='color: red;'>Cartão de Crédito Inválido</h1>", unsafe_allow_html=True)
    st.write("Não foi possível identificar o cartão de crédito na imagem ou o cartão é inválido")


if __name__ == "__main__":
  configure_interface()