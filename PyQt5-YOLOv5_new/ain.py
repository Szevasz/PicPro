def show_popup(content):
    # 创建主窗口
    root = tk.Tk()

    # 隐藏主窗口
    root.withdraw()

    popup = tk.Toplevel(root)
    popup.title("弹窗标题")

    # 创建文本标签，显示 content 内容
    label = tk.Label(popup, text=content)
    label.pack(padx=10, pady=10)

    # 创建关闭按钮
    close_button = tk.Button(popup, text="关闭", command=lambda: on_close_button(root, popup))
    close_button.pack(pady=10)

    # 运行弹窗主循环
    popup.mainloop()

def on_close_button(root, popup):
    # 销毁弹窗
    popup.destroy()

    # 恢复主窗口的显示
    root.deiconify()



match = re.match(r'([a-zA-Z-]+)', label)
if match:
    disease_name = match.group(1)
    print(f'病害信息: {disease_name}')
    self.disease_info_signal.emit(disease_name)

    # 设置对应的prompt
    if disease_name == 'blasst':
        prompt = "当水稻出现稻瘟病，其诱因，防治措施，以后的防治措施有哪些。分别50字叙述"
    elif disease_name == 'brown-Spot':
        prompt = "当水稻出现褐斑病，其诱因，防治措施，以后的防治措施有哪些。分别50字叙述"
    elif disease_name == 'blight':
        prompt = "当水稻出现枯萎病，其诱因，防治措施，以后的防治措施有哪些。分别50字叙述"
    elif disease_name == 'Dead Heart':
        prompt = "当水稻出现枯心病，其诱因，防治措施，以后的防治措施有哪些。分别50字叙述"
    elif disease_name == 'Downy':
        prompt = "当水稻出现露珠病，其诱因，防治措施，以后的防治措施有哪些。分别50字叙述"
    elif disease_name == 'False':
        prompt = "当水稻出现假烟病，其诱因，防治措施，以后的防治措施有哪些。分别50字叙述"
    elif disease_name == 'Sheath Blight':
        prompt = "当水稻出现鞘病，其诱因，防治措施，以后的防治措施有哪些。分别50字叙述"
    elif disease_name == 'Streak':
        prompt = "当水稻出现叶纹病，其诱因，防治措施，以后的防治措施有哪些。分别50字叙述"
    elif disease_name == 'Tungro':
        prompt = "当水稻出现东南亚稻田病，其诱因，防治措施，以后的防治措施有哪些。分别50字叙述"
    else:
        prompt = "未知病害"

    content = chat(prompt)
    show_popup(content)