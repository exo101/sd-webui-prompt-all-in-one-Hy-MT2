# sd-webui-prompt-all-in-one-Hy-MT2

[![GitHub](https://img.shields.io/github/stars/exo101/sd-webui-prompt-all-in-one-Hy-MT2?style=social)](https://github.com/exo101/sd-webui-prompt-all-in-one-Hy-MT2)

基于 [sd-webui-prompt-all-in-one](https://github.com/physton/sd-webui-prompt-all-in-one) 插件增强版本，集成了腾讯混元 Hy-MT2 系列翻译模型，支持多种模型选择，实现高质量的离线翻译功能。

---

## 🎯 功能特性

### 核心功能
- ✅ **多模型支持**：集成 5 种混元翻译模型，满足不同性能需求
- ✅ **离线翻译**：模型本地运行，无需 API 密钥，保护隐私
- ✅ **多语言支持**：支持 18 种语言互译（中文、英文、日文、韩文、德文、法文、俄文、西班牙文、葡萄牙文、意大利文、阿拉伯文、印地文、印尼文、越南文、泰文、马来文、土耳其文）
- ✅ **自动检测语言**：智能识别输入文本语言
- ✅ **批量翻译**：支持批量处理多条文本

### 新增混元模型
| 模型名称 | 模型标识 | 显存要求 | 特点 |
|---------|---------|---------|------|
| Hy-MT2-1.8B | `Tencent-Hunyuan/Hy-MT2-1.8B` | 4-6GB | 基础版，速度最快，适合低显存环境 |
| Hy-MT2-7B-FP8 | `Tencent-Hunyuan/Hy-MT2-7B-FP8` | 8GB+ | 7B 版本，FP8 量化，平衡性能和质量 |
| Hy-MT2-7B | `Tencent-Hunyuan/Hy-MT2-7B` | 10GB+ | 7B 版本，全精度，更高翻译质量 |
| Hy-MT2-30B-A3B | `Tencent-Hunyuan/Hy-MT2-30B-A3B` | 16GB+ | 30B 版本，A3B 量化，适合高端显卡 |
| Hy-MT2-30B-A3B-FP8 | `Tencent-Hunyuan/Hy-MT2-30B-A3B-FP8` | 20GB+ | 30B 版本，A3B+FP8 量化，最优性能 |

---

## 📁 目录结构

```
sd-webui-prompt-all-in-one-Hy-MT2/
├── .github/                    # GitHub 配置文件
│   ├── ISSUE_TEMPLATE/         # Issue 模板
│   └── workflows/              # CI/CD 工作流
├── group_tags/                 # 分组标签数据
│   ├── zh_CN.yaml              # 中文标签
│   ├── en_US.yaml              # 英文标签
│   ├── ja_JP.yaml              # 日文标签
│   └── ...                     # 其他语言标签
├── models/                     # 模型存放目录（自动创建）
├── scripts/                    # Python 后端脚本
│   ├── physton_prompt/         # 核心模块
│   │   ├── translator/         # 翻译器实现
│   │   │   ├── hunyuan_translator.py    # 混元翻译器
│   │   │   ├── baidu_translator.py      # 百度翻译
│   │   │   ├── google_translator.py     # Google 翻译
│   │   │   └── ...                      # 其他翻译器
│   │   ├── hunyuan.py          # 混元模型核心逻辑
│   │   ├── translate.py        # 翻译主入口
│   │   └── ...                 # 其他工具模块
│   └── on_app_started.py       # 应用启动时初始化
├── src/                        # 前端源代码（Vue.js）
│   ├── components/             # Vue 组件
│   ├── mixins/                 # Vue 混入
│   ├── utils/                  # 工具函数
│   ├── App.vue                 # 主应用组件
│   └── main.js                 # 入口文件
├── storage/                    # 存储目录
├── styles/                     # 样式扩展
├── translate_apis.json         # 翻译 API 配置
├── i18n.json                   # 国际化配置
├── install.py                  # 安装脚本
├── style.css                   # 全局样式
└── README.md                   # 项目说明
```

---

## 🚀 快速开始

### 1. 安装插件

将插件放入 SD WebUI 的 `extensions` 目录：

```bash
cd /path/to/webui/extensions
git clone https://github.com/your-repo/sd-webui-prompt-all-in-one-Hy-MT2.git
```

### 2. 安装依赖

插件会自动安装所需依赖，但建议手动确认：

```bash
pip install transformers torch accelerate sentencepiece
```

### 3. 下载模型

模型支持两种加载方式：

#### 方式一：自动下载（首次使用时自动下载）
选择模型后，插件会自动从 HuggingFace 下载模型到 `webui/models/` 目录。

#### 方式二：手动放置
将下载好的模型放入以下目录：

```
webui/models/
├── Hy-MT2-1.8B/
├── Hy-MT2-7B-FP8/
├── Hy-MT2-7B/
├── Hy-MT2-30B-A3B/
└── Hy-MT2-30B-A3B-FP8/
```

### 4. 使用方法

1. 启动 SD WebUI
2. 打开 "Prompt All in One" 插件
3. 在翻译设置中选择 `Tencent-Hunyuan / Hy-MT2`
4. 在模型配置中选择所需的模型
5. 开始翻译！

---

## ⚡ 模型优势

### 混元 Hy-MT2 系列特点

#### 1. 高质量翻译
- 基于腾讯混元大模型技术，翻译质量达到业界领先水平
- 支持丰富的专业术语和上下文理解
- 准确处理复杂句子结构

#### 2. 多语言覆盖
- 支持 18 种语言互译
- 特别优化了中日韩等亚洲语言的翻译质量
- 支持小语种翻译

#### 3. 离线运行
- 无需联网，保护隐私
- 无需 API 密钥，零使用成本
- 模型本地化，响应速度快

#### 4. 灵活部署
- 提供多种模型规格，适配不同硬件配置
- 支持 FP8/A3B 量化，降低显存占用
- 支持自动选择最优模型

#### 5. 开源免费
- 基于 Apache 2.0 协议
- 完全免费使用
- 支持商业场景

---

## 📊 模型选择建议

| 显卡显存 | 推荐模型 | 推荐场景 |
|---------|---------|---------|
| 4-6GB | Hy-MT2-1.8B | 入门级配置，快速翻译 |
| 8-10GB | Hy-MT2-7B-FP8 | 主流配置，平衡速度和质量 |
| 10-16GB | Hy-MT2-7B | 高质量翻译需求 |
| 16-20GB | Hy-MT2-30B-A3B | 专业级翻译 |
| 20GB+ | Hy-MT2-30B-A3B-FP8 | 极致翻译质量 |

---

## 🔧 配置说明

### 模型配置

在 `translate_apis.json` 中可以看到混元翻译的配置：

```json
{
  "key": "hunyuan",
  "name": "Tencent-Hunyuan / Hy-MT2",
  "config": [
    {
      "key": "model",
      "title": "Model",
      "type": "select",
      "default": "Tencent-Hunyuan/Hy-MT2-1.8B",
      "options": [
        "Tencent-Hunyuan/Hy-MT2-1.8B",
        "Tencent-Hunyuan/Hy-MT2-7B-FP8",
        "Tencent-Hunyuan/Hy-MT2-7B",
        "Tencent-Hunyuan/Hy-MT2-30B-A3B",
        "Tencent-Hunyuan/Hy-MT2-30B-A3B-FP8"
      ]
    }
  ]
}
```

### 模型缓存目录

模型默认存储在 `webui/models/` 目录下，可通过修改 `scripts/physton_prompt/hunyuan.py` 中的 `cache_dir` 变量更改存储位置。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📄 许可证

本项目基于 [sd-webui-prompt-all-in-one](https://github.com/physton/sd-webui-prompt-all-in-one)，遵循原项目许可证。

混元模型遵循 Apache 2.0 许可证，请遵守相关开源协议。

---

## 📞 支持

如有问题或建议，请提交 Issue 或联系开发者。

---

**注意**：使用前请确保已安装所有必要依赖，并根据您的硬件配置选择合适的模型。大型模型可能需要较长的加载时间和较高的显存。
