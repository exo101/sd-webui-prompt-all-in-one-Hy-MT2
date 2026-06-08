import os
import time
import warnings
from scripts.physton_prompt.get_lang import get_lang

# 忽略 transformers 的警告
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', message='.*token_type_ids.*')

model = None
tokenizer = None
model_name = "Tencent-Hunyuan/Hy-MT2-1.8B"
# 模型目录设置在 webui 的 models 目录下
# 从 scripts/physton_prompt/ 到 webui/models 需要 4 个 ../
cache_dir = os.path.normpath(os.path.dirname(os.path.abspath(__file__)) + '/../../../../models')
model_path = os.path.join(cache_dir, "Hy-MT2-1.8B")
loading = False

def initialize(reload=False):
    global model, tokenizer, model_name, cache_dir, model_path, loading
    
    # 延迟导入 torch，只在需要时导入
    import torch
    
    if loading:
        while loading:
            time.sleep(0.1)
            pass
        if model is None or tokenizer is None:
            raise Exception('error')
        return
    if not reload and model is not None:
        return
    loading = True
    model = None
    tokenizer = None

    # 检查本地模型是否存在
    local_model_path = model_path
    model_file = os.path.join(local_model_path, "pytorch_model.bin")
    config_file = os.path.join(local_model_path, "config.json")
    
    if os.path.exists(local_model_path) and os.path.exists(config_file):
        model_name = local_model_path
        print(f'[sd-webui-prompt-all-in-one] Loading local model from {local_model_path}...')
    else:
        print(f'[sd-webui-prompt-all-in-one] Local model not found at {local_model_path}, will download from ModelScope...')
        # 如果本地不存在，尝试从 ModelScope 下载
        model_name = "Tencent-Hunyuan/Hy-MT2-1.8B"

    try:
        from transformers import AutoTokenizer, AutoModelForCausalLM
        
        print(f'[sd-webui-prompt-all-in-one] Loading model {model_name}...')
        tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir if not os.path.exists(local_model_path) else None, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            model_name, 
            cache_dir=cache_dir if not os.path.exists(local_model_path) else None,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            trust_remote_code=True
        )
        model.eval()
        print(f'[sd-webui-prompt-all-in-one] Model {model_name} loaded.')
        loading = False
    except Exception as e:
        loading = False
        raise e

def translate(text, src_lang, target_lang):
    global model, tokenizer
    
    # 在翻译时导入 torch
    import torch

    if not text:
        if isinstance(text, list):
            return []
        else:
            return ''

    if model is None:
        raise Exception(get_lang('model_not_initialized'))

    if tokenizer is None:
        raise Exception(get_lang('model_not_initialized'))

    if src_lang == target_lang:
        return text

    # 语言代码映射到目标语言名称
    lang_map = {
        'zh_CN': '英语',
        'zh_HK': '英语',
        'zh_TW': '英语',
        'en_US': '中文',
        'en_GB': '中文',
        'ja_JP': '中文',
        'ko_KR': '中文',
        'de_DE': '中文',
        'fr_FR': '中文',
        'ru_RU': '中文',
        'es_ES': '中文',
        'pt_PT': '中文',
        'it_IT': '中文',
        'ar_SA': '中文',
        'hi_IN': '中文',
        'id_ID': '中文',
        'vi_VN': '中文',
        'th_TH': '中文',
        'ms_MY': '中文',
        'tr_TR': '中文',
    }
    
    # 使用 from_lang 作为目标语言
    tgt = lang_map.get(src_lang, '英语')

    if isinstance(text, list):
        results = []
        for t in text:
            prompt = f"将以下文本翻译成{tgt},注意只需要输出翻译后的结果,不要额外解释:\n\n{t}"
            print(f'[sd-webui-prompt-all-in-one] Hunyuan translating: {prompt}')
            try:
                messages = [{"role": "user", "content": prompt}]
                input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
                
                with torch.no_grad():
                    outputs = model.generate(
                        input_ids=input_ids,
                        max_new_tokens=500,
                        temperature=0.7,
                        top_p=0.6,
                        top_k=20,
                        repetition_penalty=1.05,
                    )
                result = tokenizer.decode(outputs[0][input_ids.shape[-1]:], skip_special_tokens=True)
                print(f'[sd-webui-prompt-all-in-one] Hunyuan result: {result}')
                results.append(result.strip())
            except Exception as e:
                print(f'[sd-webui-prompt-all-in-one] Hunyuan translate error: {str(e)}')
                import traceback
                traceback.print_exc()
                results.append(t)  # 如果翻译失败，返回原文
        return results
    else:
        prompt = f"将以下文本翻译成{tgt},注意只需要输出翻译后的结果,不要额外解释:\n\n{text}"
        print(f'[sd-webui-prompt-all-in-one] Hunyuan translating: {prompt}')
        try:
            messages = [{"role": "user", "content": prompt}]
            input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
            
            with torch.no_grad():
                outputs = model.generate(
                    input_ids=input_ids,
                    max_new_tokens=500,
                    temperature=0.7,
                    top_p=0.6,
                    top_k=20,
                    repetition_penalty=1.05,
                )
            result = tokenizer.decode(outputs[0][input_ids.shape[-1]:], skip_special_tokens=True)
            print(f'[sd-webui-prompt-all-in-one] Hunyuan result: {result}')
            return [result.strip()]
        except Exception as e:
            print(f'[sd-webui-prompt-all-in-one] Hunyuan translate error: {str(e)}')
            import traceback
            traceback.print_exc()
            return [text]  # 如果翻译失败，返回原文