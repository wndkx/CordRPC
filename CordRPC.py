import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent
import pypresence
import time
def main(page: ft.Page) -> None:
    page.title = "CordRPC" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False
    page.scroll = True
    page.theme_mode = "light"
    text = Text(value="CordRPC")
    client_id = TextField(label="Client ID", text_align=ft.TextAlign.LEFT, width=200)
    large_image = TextField(label="Large Image", text_align=ft.TextAlign.LEFT, width=200)
    large_text = TextField(label="Large Text", text_align=ft.TextAlign.LEFT, width=200)
    details = TextField(label="Details", text_align=ft.TextAlign.LEFT, width=200)
    state = TextField(label="State", text_align=ft.TextAlign.LEFT, width=200)
    update_time = TextField(label="Update time", text_align=ft.TextAlign.LEFT, width=200)
    btn1_text = Text(value="Button 1: ", text_align=ft.TextAlign.LEFT, width=200)
    btn1_name = TextField(label="Name", text_align=ft.TextAlign.LEFT, width=200)
    btn1_url = TextField(label="URL", text_align=ft.TextAlign.LEFT, width=200)
    btn2_text = Text(value="Button 2(Optional): ", text_align=ft.TextAlign.LEFT, width=200)
    btn2_name = TextField(label="Name", text_align=ft.TextAlign.LEFT, width=200)
    btn2_url = TextField(label="URL", text_align=ft.TextAlign.LEFT, width=200)
    checkbox = Checkbox(label="I agree to ToS", value=False)
    btn = ElevatedButton(text="Run", width=200, disabled=True)
    def validate(e: ControlEvent):
        if all([client_id.value,large_image.value, large_text.value, details.value, btn1_name.value, btn1_url.value, update_time.value,state.value, checkbox.value]):
            btn.disabled = False
        else:
            btn.disabled = True
        page.update()
    def RPC(e: ControlEvent):
        try:
            RPC = pypresence.Presence(client_id.get())
            RPC.connect()
            start = int(time.time())

            while True:
                btns = [
                    {
                        "label": btn1_name.value(),
                        "url": btn1_url.value()
                    }
                ]
                if all(btn2_name.value, btn2_url.value):
                    btns.append({
                        "label": btn2_name.value(),
                        "url": btn2_url.value()
                    })
                RPC.update(
                large_image=large_image.value,
                large_text=large_text.value,
                details=details.value,
                state=state.value,
                start=start,
                buttons=btns
                )
                time.sleep(int(update_time.value))
        except Exception as e:
            pass
    checkbox.on_change = validate
    client_id.on_change = validate
    large_image.on_change = validate
    large_text.on_change = validate
    details.on_change = validate
    state.on_change = validate
    update_time.on_change = validate
    btn1_name.on_change = validate
    btn1_url.on_change = validate
    btn.on_click = RPC
    page.add(
        Row([
            Column([
                text,
                client_id,
                large_image,
                large_text,
                details,
                state,
                update_time,
                btn1_text,
                btn1_name,
                btn1_url,
                btn2_text,
                btn2_name,
                btn2_url,
                checkbox,
                btn
            ])
        ], alignment=ft.MainAxisAlignment.CENTER)
    )
ft.app(target=main)