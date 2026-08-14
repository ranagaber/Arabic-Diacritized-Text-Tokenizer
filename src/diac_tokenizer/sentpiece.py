from huggingface_hub import hf_hub_download
import sentencepiece as spm

model_path = hf_hub_download(
    repo_id="RanaGaber/Diacritized_Arabic_Tokenizer_1M",
    filename="spiece.model",   
)

sp = spm.SentencePieceProcessor(model_file=model_path)
def get_tokens(text: str):
    return sp.encode_as_pieces(text)