
AL使用streamlit快速搭建一个前端


```python
# streamlit

https://docs.streamlit.io

import streamlit as st

## 文字

st.header("创建测试项目")

st.subheader("脚本列表")

st.write('测试规范:')

st.markdown()

markdown_css = """
<style>
.markdown-text-container {
    background-color: black;
    color: white;
    padding: 1em;
    border-radius: 5px;
}
</style>
"""
st.markdown(markdown_css, unsafe_allow_html=True)

markdown_content = """
<div class="markdown-text-container">
text
</div>
"""
st.markdown(markdown_content, unsafe_allow_html=True)

## 输入

title = st.text_input("测试编号", "1") # 标题 , 默认值

title1 = st.text_area("项目具体描述", "USI",height=400) # 标题 , 默认值



## 按钮

st.link_button('确认创建',url='/rule',type='primary')



## 进度

with st.status("生成测试规范...", expanded=True) as status:
    st.write("识别...")
    time.sleep(0.1)
    st.write("生成...")
    time.sleep(1)
    st.write("反思优化...")
    status.update(
        label="生成测试规范完成!", state="complete", expanded=False
    )
    

word = st.empty()
#文字占位符
bar=st.progress(0)
# 进度条 
for i in range(100):
    word.text('生成测试脚本进度:'+str(i+1))
    if i < 10:
        bar.progress(i+1)
        time.sleep(0.1)



## 数据

st.data_editor()



## 结构

fake2
----app.py
----pages
--------create.py
--------detail.py
--------progress1.py
--------progress2.py
--------rule.py
--------script.py


%%writefile app.py
import streamlit as st
rule = st.Page("pages/rule.py", title="规范及脚本生成", icon=":material/dashboard:")
script = st.Page("pages/script.py", title="脚本管理", icon=":material/dashboard:")
create = st.Page("pages/create.py", title="创建测试项目", icon=":material/dashboard:")
detail = st.Page("pages/detail.py", title=" ", icon="")
subdetail = st.Page("pages/subdetail.py", title=" ", icon="")
progress1 = st.Page("pages/progress1.py", title=" ", icon="")
progress2 = st.Page("pages/progress2.py", title=" ", icon="")



pg = st.navigation(
    {
        "超级SIM测试脚本自动生成系统": [create,rule,script,detail,subdetail,progress1,progress2]
    }
)

pg.run()


```


```python

import streamlit as st


from config import BianxieConfig

llm_config = BianxieConfig()
llm = OpenAI(
    model="gpt-4o",
    api_key=llm_config.api_key,
    api_base=llm_config.api_base,
    temperature=0.1,
)


# 配置页面
st.set_page_config(
    page_title="AI工具集",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 定义导航菜单
PAGES = {
    "模板类": "web/temps.py",
    "编码类": "web/writer.py",
    "聊天":"web/chat.py"
}

# 显示导航
st.sidebar.title("工具导航")
page = st.sidebar.selectbox(
    "请选择工具",
    options=list(PAGES.keys()),
    index=0,
)

# 加载对应的页面
import importlib.util
page_script = PAGES[page]
spec = importlib.util.spec_from_file_location("page", page_script)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.app()



```