from huggingface_hub import hf_hub_download

repo_id = "Qwen/Qwen2.5-0.5B-Instruct-GGUF" # model adı

filename = "qwen2.5-0.5b-instruct-q4_k_m.gguf" # Dosya adı (Quantization formatı)

model_path = hf_hub_download(
    repo_id=repo_id,
    filename=filename,
    local_dir="./ai/models", # Modeli 'models' klasörüne indirecek
    local_dir_use_symlinks=False
)