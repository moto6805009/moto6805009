from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.utils import platform
import os
import requests

# ===== ป้องกันไม่เจอฟอนต์ =====
FONT_NAME = "THSarabunNew"
FONT_PATH = "THSarabunNew.ttf"
if os.path.exists(FONT_PATH):
    LabelBase.register(name=FONT_NAME, fn_regular=FONT_PATH)
else:
    FONT_NAME = None  # fallback ถ้าไม่เจอฟอนต์

# ===== Discord Webhook =====
DISCORD_WEBHOOK_URL = "https://discordapp.com/api/webhooks/1372026730109468672/1Zsl1q-dST8NTXEKs2CuUK-fEgEKTb_wB6wbRbRqG5tfYLsUKiEpAv6WzRuFaMlEKO5Q"

class RepairForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.name = TextInput(hint_text="👤 ชื่อผู้แจ้ง", font_name=FONT_NAME)
        self.branch = TextInput(hint_text="🏢 บริษัท / สาขา", font_name=FONT_NAME)
        self.device = TextInput(hint_text="💻 อุปกรณ์ที่เสีย", font_name=FONT_NAME)
        self.detail = TextInput(hint_text="📝 รายละเอียดปัญหา", multiline=True, font_name=FONT_NAME)
        self.contact = TextInput(hint_text="📞 ช่องทางติดต่อกลับ", font_name=FONT_NAME)

        self.add_widget(self.name)
        self.add_widget(self.branch)
        self.add_widget(self.device)
        self.add_widget(self.detail)
        self.add_widget(self.contact)

        submit = Button(text="✅ ส่งแจ้งซ่อม", background_color=(0, 0.6, 0, 1), font_name=FONT_NAME)
        submit.bind(on_press=self.send_report)
        self.add_widget(submit)

        self.status_label = Label(text="", font_name=FONT_NAME)
        self.add_widget(self.status_label)

    def send_report(self, instance):
        content = f"""🔧 **แจ้งซ่อมอุปกรณ์**

👤 ผู้แจ้ง: {self.name.text}
🏢 บริษัท / สาขา: {self.branch.text}
💻 อุปกรณ์ที่เสีย: {self.device.text}
📝 รายละเอียด: {self.detail.text}
📞 ช่องทางติดต่อกลับ: {self.contact.text}
"""

        try:
            response = requests.post(DISCORD_WEBHOOK_URL, json={"content": content})
            if response.status_code in (200, 204):
                self.status_label.text = "✅ ส่งข้อมูลเรียบร้อยแล้ว"
                self.name.text = ""
                self.branch.text = ""
                self.device.text = ""
                self.detail.text = ""
                self.contact.text = ""
            else:
                self.status_label.text = f"❌ ผิดพลาด: {response.status_code}"
        except Exception as e:
            self.status_label.text = f"❌ ผิดพลาด: {str(e)}"

class RepairApp(App):
    def build(self):
        return RepairForm()

if __name__ == '__main__':
    RepairApp().run()
