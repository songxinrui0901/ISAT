import cv2
import gradio as gr
import time
from pathlib import Path

# 自定义 CSS 动画和样式
custom_css = """
/* 初始加载动画 */
@keyframes cloud_enter {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

.cloud-animation {
    animation: cloud_enter 1.5s ease-out;
    text-align: center;
    font-size: 3em;
    color: #2c7be5;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

/* 点击后过渡动画 */
@keyframes expand {
    0% { clip-path: circle(0% at 50% 50%); }
    100% { clip-path: circle(150% at 50% 50%); }
}

.transition-screen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #2c7be5 0%, #6a11cb 100%);
    animation: expand 1s ease-in-out forwards;
    z-index: 9999;
}

/* 主容器样式 */
#main-container {
    display: none; /* 初始隐藏主界面 */
}
"""


# 加载动画页面 HTML
def load_animation_html():
    return f"""
    <div class="cloud-animation">
        <div style="margin-bottom:20px;">☁️</div>
        <div>云防智控</div>
        <div style="font-size:0.8em;margin-top:20px;color:#666;">点击任意位置开始</div>
    </div>
    """


# 主功能页面（复用之前的AI界面）
def create_main_interface():
    with gr.Blocks(analytics_enabled=False) as main_interface:
        # 原始代码中的AI自动化界面组件
        with gr.Row():
            gr.Markdown("## AI自动化代理控制面板")

        with gr.Row():
            original = gr.Image(label="实时画面", streaming=True)
            processed = gr.Image(label="智能分析", streaming=True)

        with gr.Row():
            level = gr.Dropdown(["KR-1","KR-16" ], label="关卡选择")
            btn = gr.Radio(["启动代理系统", "停止系统"], label="控制中心")

        status = gr.Textbox("系统待机", label="系统状态")

    return main_interface


# 创建完整应用
with gr.Blocks(css=custom_css, title="云防智控") as app:
    # 初始动画层
    gr.HTML(load_animation_html(), elem_id="splash-screen")

    # 过渡动画层
    transition = gr.HTML("""<div class="transition-screen"></div>""", visible=False)

    # 主功能界面
    with gr.Column(elem_id="main-container"):
        main_interface = create_main_interface()

    # JavaScript交互
    app.load(
        None,
        None,
        None,
        js="""
        () => {
            // 初始加载完成显示动画
            document.getElementById("splash-screen").style.opacity = 1;

            // 点击任意位置触发过渡
            document.body.onclick = () => {
                // 播放过渡动画
                document.querySelector(".transition-screen").style.display = "block";

                // 1秒后切换界面
                setTimeout(() => {
                    document.getElementById("splash-screen").style.display = "none";
                    document.getElementById("main-container").style.display = "block";
                }, 1000);
            }
        }
        """
    )


# 模拟AI处理函数（复用之前的逻辑）
def ai_processing(frame):
    # 实际应替换为真实AI处理逻辑
    processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return processed_frame


# 启动应用
if __name__ == "__main__":
    app.launch(
        server_port=7860,
        favicon_path="cloud.ico",  # 自定义图标
        inbrowser=True
    )