from enum import Enum

class OpenAIModel(Enum):
    EMBEDDING_ADA_002 = "text-embedding-ada-002"
    EMBEDDING_3_LARGE = "text-embedding-3-large"
    GPT_3_5_4K = "gpt-3.5-turbo"
    GPT_3_5_TURBO_INSTRUCT = "gpt-3.5-turbo-instruct"
    GPT_4_TURBO = "gpt-4-turbo"
    GPT_4_OMNI = "gpt-4o"
    GPT_4_OMNI_MINI = "gpt-4o-mini"

class AnthropicModel(Enum):
    CLAUDE_3_OPUS_20240229 = "claude-3-opus-20240229"
    CLAUDE_3_SONNET_20240229 = "claude-3-sonnet-20240229"
    CLAUDE_3_HAIKU_20240307 = "claude-3-haiku-20240307"
