pytest -m slow # 运行带有 `slow` 标记的测试
pytest -m "not slow"  # 运行不带有 `slow` 标记的测试

pytest test_example.py::test_add

@pytest.mark.slow

| 运行失败的测试 | pytest --lf                                   |
| ------- | --------------------------------------------- |
| 运行失败的测试 | pytest --lf                                   |
| 查看详细输出  | pytest -v                                     |
| 对标记物测试  | pytest -m slow                                |





## 意像

### 当前时刻
```python
current_date = datetime.now()

formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
formatted_date = current_date.strftime("%Y-%m-%d")

```

### today
```python
def get_today():
	# 获取本地时间
	local_time = datetime.today()
	# print("本地时间:", local_time)
	return local_time
```