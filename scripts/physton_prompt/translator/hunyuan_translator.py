from scripts.physton_prompt.translator.base_translator import BaseTranslator
from scripts.physton_prompt.get_lang import get_lang
from scripts.physton_prompt.hunyuan import initialize as hunyuan_initialize, translate as hunyuan_translate


class HunyuanTranslator(BaseTranslator):
    def __init__(self):
        super().__init__('hunyuan')

    def translate(self, text):
        if not text:
            if isinstance(text, list):
                return []
            else:
                return ''

        # 确保模型已初始化
        hunyuan_initialize()

        result = hunyuan_translate(text=text, src_lang=self.from_lang, target_lang=self.to_lang)
        if not result:
            raise Exception(get_lang('response_is_empty', {'0': 'Hunyuan MT2'}))

        if isinstance(text, list):
            return result
        else:
            return result[0]

    def translate_batch(self, texts):
        return self.translate(texts)