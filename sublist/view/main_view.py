from flet import *
import time

def main(page: Page):
    inputText = TextField(label="Text", on_change=lambda e: addText())
    viewText = ResponsiveRow()
    inputPattren = TextField(label="Pattren", on_change=lambda e: addPattern())
    viewPattren = ResponsiveRow()
    pattrenMsg = AlertDialog()

    # Fungsi enambahkan text
    def addText():
        viewText.clean()
        dataText = list(map(str,inputText.value))
        for text in dataText:
            viewText.controls.append( Container(
                    content=Text(value=text,text_align=TextAlign.CENTER,weight=FontWeight.BOLD, size=28),
                    col = {"md":0.4, "sm":0.8},
                    bgcolor=colors.CYAN,
                    border_radius=5,
                    shadow=BoxShadow(1,2,colors.WHITE)
                ),)
        page.update()

    # Fungsi enambahkan pattren
    def addPattern():
        viewPattren.clean()
        dataPattren = list(map(str,inputPattren.value))
        for pattern in dataPattren:
            viewPattren.controls.append(Container(
                    content=Text(value=pattern,text_align=TextAlign.CENTER,weight=FontWeight.BOLD, size=28, color=colors.BLACK),
                    col = {"md":0.4, "sm":0.8},
                    bgcolor=colors.WHITE,
                    border_radius=5,
                    shadow=BoxShadow(1,2,colors.BLACK)
                ),)
        page.update()

    # Fungsi Visualisasi Sublist
    def sublistVisual():
        page.update()
        dataText = list(map(str,inputText.value))
        dataPattren = list(map(str,inputPattren.value))
        if not dataText:
            inputText.error_text = "Mohon masukan text"
            page.update()
        elif not dataPattren:
            inputText.error_text = None
            inputPattren.error_text = "Mohon masukan pattren"
            page.update()
        elif dataText and dataPattren:
            inputPattren.error_text = None
            page.update()
            i = 0
            datVaild = []
            for dti, dt in enumerate(dataText):
                time.sleep(1)
                viewText.controls[dti].scale = 1.3
                page.update()
                while i < len(dataPattren):
                    time.sleep(1)
                    viewPattren.controls[i].scale = 1.3
                    page.update()
                    if dt != dataPattren[i]:
                        time.sleep(1)
                        viewText.controls[dti].bgcolor = colors.RED
                        viewPattren.controls[i].bgcolor = colors.RED
                        page.update()
                        time.sleep(1)
                        viewPattren.controls[i].scale = 1
                        viewText.controls[dti].scale = 1
                        page.update()
                        time.sleep(1)
                        viewText.controls[dti].bgcolor = colors.CYAN
                        viewPattren.controls[i].bgcolor = colors.WHITE
                        page.update()
                        i = 0
                        datVaild = []
                        break

                    elif dt == dataPattren[i]:
                        time.sleep(1)
                        viewText.controls[dti].bgcolor = colors.GREEN
                        viewPattren.controls[i].bgcolor = colors.GREEN
                        page.update()
                        time.sleep(1)
                        viewPattren.controls[i].scale = 1
                        viewText.controls[dti].scale = 1
                        page.update()
                        time.sleep(1)
                        viewText.controls[dti].bgcolor = colors.CYAN
                        viewPattren.controls[i].bgcolor = colors.WHITE
                        page.update()
                        datVaild.append(dataPattren[i])
                        i+=1
                        break
                time.sleep(1)
                viewText.controls[dti].scale = 1
                page.update()
                if datVaild == dataPattren:
                    break  

            if datVaild == dataPattren:
                    msg = ""
                    for dp in dataPattren:
                        msg += dp
                    pattrenMsg.icon = Icon(name="CHECK_CIRCLE",color="GREEN", size=50)
                    pattrenMsg.title = Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            Text(value="List Found",color=colors.GREEN,size=24, weight=FontWeight.BOLD, text_align=TextAlign.CENTER),
                            Text(value=f"{msg} Tedapat Didalam List Text",color=colors.WHITE,size=14, weight=FontWeight.W_500, text_align=TextAlign.CENTER),
                        ]
                    )
                    page.dialog = pattrenMsg
                    pattrenMsg.open = True
                    page.update()
            else:
                msg = ""
                for dp in dataPattren:
                    msg += dp
                pattrenMsg.icon = Icon(name="DANGEROUS_ROUNDED",color="RED", size=50)
                pattrenMsg.title = Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Text(value="List Not Found",color=colors.RED,size=24, weight=FontWeight.BOLD, text_align=TextAlign.CENTER),
                        Text(value=f"{msg} Tidak Tedapat Didalam List Text",color=colors.WHITE,size=14, weight=FontWeight.W_500, text_align=TextAlign.CENTER),
                    ]
                )
                page.dialog = pattrenMsg
                pattrenMsg.open = True
                page.update()   
                    
    # Manambahkan setiap element
    page.add(
        
        Container(
            expand=True,
            gradient=LinearGradient(
                begin=alignment.top_center,
                end=alignment.bottom_center,
                colors=[
                    colors.PURPLE_500,
                    colors.CYAN_500,
                    # colors.with_opacity(0.8,colors.PURPLE_500),
                    # colors.with_opacity(0.8,colors.CYAN_500),
                ],
            ),
            margin=-10,
            padding=40,
            content=ResponsiveRow(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Container(
                        Text(value="Visualization Sublits Search", weight=FontWeight.BOLD, size=32, text_align=TextAlign.CENTER)
                    ),
                    Container(
                        viewText,
                    ),
                    Container(
                        inputText,  
                    ),
                    Container(
                        viewPattren
                    ),
                    Container(
                          inputPattren,
                        
                    ),
                    Container(
                        col={"md":1.5,"sm":3},
                        content=ElevatedButton(text="Start",scale=1.2, on_click=lambda e : sublistVisual()),
                    )
                ]
            )
            
        )
    )





