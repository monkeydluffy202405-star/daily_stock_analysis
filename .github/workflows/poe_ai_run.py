import poe
import os

# 自动读取 GitHub 密钥
client = poe.Client(os.getenv("POE_API_KEY"))

# ===================== 你可以改这里的提问内容 =====================
prompt = "你好，我正在使用 GitHub Actions + Poe AI，帮我确认配置是否成功"
# =================================================================

# 选择 Poe 模型（不改也能跑）
model = "claude_3_haiku"

# 发送消息并输出结果
print("🤖 Poe AI 正在回复...")
for chunk in client.send_message(model, prompt, timeout=120):
    print(chunk["text"], end="", flush=True)

print("\n\n✅ GitHub Actions + Poe AI 配置成功！")
